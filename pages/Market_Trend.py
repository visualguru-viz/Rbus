import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
import streamlit as st
import holoviews as hv
from holoviews import opts, dim
import streamlit.components.v1 as components
from bokeh.plotting import show


st.write("# Bus Routes and Services - State wise")
df = pd.read_csv('RouteList_10_States.csv', index_col=False)
df = df[['RouteName', 'BusesCount']]

df[['source', 'target']] = df['RouteName'].str.split(" to ", expand=True)
df['count'] = df['BusesCount'].str.replace(" bus options", "").astype(int)

df = df[['source', 'target', 'count']]

df1 = pd.read_csv('Indian Cities Database.csv', index_col=False)
df1['source'] = df1['City'].rename('source')
# df1['State'] = df1['State'].str.replace("$", "")

# print(df1)

temp = pd.DataFrame(df)
temp2 = pd.DataFrame(df1)

df3 = pd.merge(df, df1, on=['source'])

SelectedState = "Odisha"    

# df3 = df3[df3['State'].astype(str)=="Punjab"]
df3= df3[['source', 'target', 'count', 'State']]
SelectedState = st.selectbox("Select State", df3['State'].unique())
# df3 = df3[df3['count'].isin(['Odisha'])]
# df3= df3[['source', 'target', 'count']]
# df3 = df3.query(State=="Odisha)
df3 = df3.loc[df3['State'].str.contains(SelectedState)]

hv.extension("bokeh")
hv.output(size=260)

nodes = hv.Dataset(pd.DataFrame(df3['source']), 'index')
chord = hv.Chord(df3).select(value=(1,None))
chord.opts(
    opts.Chord(cmap='viridis', edge_cmap='viridis', edge_color = dim('source').str(), labels = 'index', node_color = dim('index').str())
)

# show(hv.render(chord))
hv.save(chord, 'fig.html')

HtmlFile = open("fig.html", 'r', encoding='utf-8')
source_code = HtmlFile.read()
components.html(source_code, width=800, height=1200, scrolling=True)

# st.write(hv.render(chord, backend='bokeh'))
# st.bokeh_chart(chord)