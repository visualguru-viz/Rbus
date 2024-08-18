import pandas as pd
import numpy as np
import streamlit as st
import altair as alt

st.set_page_config(layout="centered")
col1, col2 = st.columns((2,1))

with col1:

    df = pd.read_csv('RouteList_10_States.csv', index_col=False)
    st.write("# Number of Bus services - by State")

    # print(df.head())
    df[['From', 'To']] = df['RouteName'].str.split(" to ", expand=True)
    df['BusesCount'] = df['BusesCount'].str.replace(" bus options", "")
    df['BusesCount'] = pd.to_numeric(df['BusesCount'])
    df2 = df[['From', 'BusesCount']]
    df2_1 = pd.DataFrame(df2.groupby(['From']).sum())
    # st.write(df2_1)
    # print(df2)
    df3 = pd.read_csv('Indian Cities Database.csv', index_col=False)
    # st.write(df3)

    # chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["From", "To", "BusesCount"])
    # print(chart_data)
    # st.scatter_chart(chart_data)
    # datac = pd.DataFrame(df2.to_)

    # tmp = df.groupby("someCol")["someOtherCol"].mean().sort_values()

    # st.write(alt.Chart(df2).mark_bar().encode(
    #     x=alt.X('From', sort=None),
    #     y='BusesCount',
    # ))
    #
    temp = pd.DataFrame(df2.groupby(['From']).sum())
    temp2 = pd.DataFrame(df3.groupby(['City']).sum())
    # st.write(temp2)
    newdf = pd.concat([temp2, temp], axis=1, sort=True)
    # st.write(newdf.dropna())
    mapdata = newdf.dropna()
    statewise = pd.DataFrame(mapdata.groupby(['State']).sum())
    df7 = mapdata[['State', 'BusesCount']]
    temp3 = pd.DataFrame(df7.groupby(['State']).sum())
    # df10 = temp3[['State', 'BusesCount']]

    # st.write(temp3)
    st.bar_chart(temp3)

    # st.write(alt.Chart(df10).mark_bar().encode(
    #     x=alt.X('State', sort=None),
    #     y='BusesCount',
    # ))

    df6 = pd.DataFrame({"Lat": mapdata['Lat'], "Long":mapdata['Long'], "BusesCount": mapdata['BusesCount']*100,})
    # st.write(mapdata)
    # st.(temp)
    # st.bar_chart(df2.set_index('From'))
    st.map(df6, latitude='Lat', longitude='Long', size='BusesCount')

with col2:
    
    st.write(df2_1)
    st.write(temp3)