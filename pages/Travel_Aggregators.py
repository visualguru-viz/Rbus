import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("Travel Aggregators")
df = pd.read_csv('routebusdetails_all_in_one.csv')
df = df.fillna(0)
df = df[['routeNameList','busname','bustypes','dptimes','dplocs','runtime','bptimes','bplocs','nextday','ratings','ratingppl','busfare','oldfares','seatavail','wseatavail']]

df[['From', 'To']] = df['routeNameList'].str.split(" to ", expand=True)
df['busfare'] = df['busfare'].str.replace("INR ", "")

from_cityList = df['From'].unique()
df_c = pd.DataFrame(from_cityList)


blankIndex = [''] * len(df)
df.index = blankIndex

routrList = df['routeNameList'].unique()    
df_r = pd.DataFrame(routrList)



option = st.sidebar.selectbox("Select City: ", df_c)
df = df.loc[df['From']==option]


routeCount = len(df['routeNameList'].unique())
busCount = len(df['busname'])
ubusCount = len(df['busname'].unique())

########## GOV / PVT BUS SPLIT ###########

BusList = df['busname'].unique()

Travels = pd.DataFrame(BusList)

bus_gov = []
bus_pvt = []

for i in range(len(Travels[0])):
    if str.__contains__(str(Travels[0][i]), "-"):
        bus_gov.append(Travels[0][i])
    else:
        bus_pvt.append(Travels[0][i])


bus_gov = pd.DataFrame(bus_gov)
bus_pvt = pd.DataFrame(bus_pvt)
if bus_gov.empty:
    print("Route not available")
else:
    gov_list = bus_gov = pd.DataFrame(bus_gov[0].unique())

if bus_pvt.empty:
    print("Route not available")
else:
    pvt_list = bus_pvt = pd.DataFrame(bus_pvt[0].unique())


st.write("Available Routes: ", routeCount, "No of Bus Services: ", busCount)
st.write("Total Buses: ", ubusCount, "Government Buses: ", len(bus_gov), "Private Buses: ", len(bus_pvt))

option2 = st.selectbox("Select Route: ", df['routeNameList'].unique())
df = df.loc[df['routeNameList']==option2]

df1 = df[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
df1['busfare'] = df1['busfare'].replace("INR ", "")
ubusCount = len(df1['busname'].unique())

BusList = df1['busname'].unique()

Travels = pd.DataFrame(BusList)
bus_gov = []
bus_pvt = []

for i in range(len(Travels[0])):
    if str.__contains__(str(Travels[0][i]), "-"):
        bus_gov.append(Travels[0][i])
    else:
        bus_pvt.append(Travels[0][i])


bus_gov = pd.DataFrame(bus_gov)
bus_pvt = pd.DataFrame(bus_pvt)
if bus_gov.empty:
    print("Bus not found in this route")
elif bus_pvt.empty:
    print("Bus not available")
else:
    gov_list = bus_gov = pd.DataFrame(bus_gov[0].unique())
    pvt_list = bus_pvt = pd.DataFrame(bus_pvt[0].unique())

st.write("Buses in this route: ", ubusCount, "Government Buses: ", len(bus_gov), "Private Buses: ", len(bus_pvt))

option3 = st.sidebar.radio("Select Bus: ", ('Government Bus', 'Private Bus'),horizontal=True)

option4 = st.sidebar.radio("Bus type: ", {'AC', 'Non-AC'}, horizontal=True, )





st.write(f"{option3}  ::  {option4}")

if option3=="Government Bus":
    if bus_gov.empty:
        print("Bus not available")
    else:
        df1 = df[df1['busname'].isin(bus_gov[0])]
    
    df1['busfare'] = df1['busfare'].replace("INR ", "")
    

    ################
    option5 = st.sidebar.slider("Price range: ", max_value=1000, step=10, value=800)
    # st.write(option5)
    # df1['busfare']=pd.to_numeric(df1['busfare']) <option5
    df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
    df11 = df1[df1['busfare'].astype(int)<=option5]

    st.sidebar.subheader("Bus Ratings")
    selected = 0
    selected = st.sidebar.feedback("stars")
    df11['ratings'] = df11['ratings'].str.replace("New",'0.0')
    if selected is None:
        if option4=="Non-AC":
            df11 = df11[df11['bustypes'].str.contains('|'.join(['Non AC', 'Non A/C']))]
            st.write(df11)

        elif option4 == "AC":
            df11 = df11[~df11['bustypes'].str.contains("Non")]
            st.write(df11)

        # st.write(df11)
    else:
        if option4=="Non-AC":
            df11 = df11[df11['bustypes'].str.contains("Non")]
            df12 = df11[df11['ratings'].astype(float).astype(int)==selected]

            st.write(df12)

        elif option4 == "AC":
            
            df11 = df11[~df11['bustypes'].str.contains("Non")]
            df12 = df11[df11['ratings'].astype(float).astype(int)==selected]

            st.write(df12)
        # st.write(df12)
    
elif option3 == "Private Bus":
    if bus_pvt.empty:
        print("Bus not available")
    else:

        df1 = df[df1['busname'].isin(bus_pvt[0])]
    df1['busfare'] = df1['busfare'].replace("INR ", "")
    option5 = st.sidebar.slider("Price range: ", max_value=1000, step=10, value=800)
    df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
    df11 = df1[df1['busfare'].astype(int)<=option5]
    
    st.sidebar.subheader("Bus Ratings")
    selected = st.sidebar.feedback("stars")
    df11['ratings'] = df11['ratings'].str.replace("New",'0')
    if selected is None:
        if option4=="Non-AC":
            df11 = df11[df11['bustypes'].str.contains('|'.join(['Non AC', 'Non A/C']))]
            st.write(df11)
        else:
            df11 = df11[df11['bustypes'].str.contains('|'.join(['Non AC', 'Non A/C']))==False]
            st.write(df11)
        # st.write(df11)
    else:
        if option4=="Non-AC":
            df11 = df11[df11['bustypes'].str.contains('|'.join(['Non AC', 'Non A/C']))==True]
            df12 = df11[df11['ratings'].astype(float).astype(int)==selected]

            st.write(df12)

        elif option4 == "AC":
            
            df11 = df11[df11['bustypes'].str.contains('|'.join(['Non AC', 'Non A/C']))==False]
            df12 = df11[df11['ratings'].astype(float).astype(int)==selected]

            st.write(df12)
        # df12 = df11[df11['ratings'].astype(float).astype(int)==selected]
        # st.write(df12)

