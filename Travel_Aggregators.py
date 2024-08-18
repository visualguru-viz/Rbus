import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(layout="wide")

st.sidebar.title("Travel Aggregators")
df = pd.read_csv('routebusdetails_all_in_one.csv')
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

gov_list = bus_gov = pd.DataFrame(bus_gov[0].unique())
pvt_list = bus_pvt = pd.DataFrame(bus_pvt[0].unique())


st.write("Available Routes: ", routeCount, "No of Bus Services: ", busCount)
st.write("Total Buses: ", ubusCount, "Government Buses: ", len(bus_gov), "Private Buses: ", len(bus_pvt))

option2 = st.selectbox("Select Route: ", df['routeNameList'].unique())
df = df.loc[df['routeNameList']==option2]

df1= df[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
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

gov_list = bus_gov = pd.DataFrame(bus_gov[0].unique())
pvt_list = bus_pvt = pd.DataFrame(bus_pvt[0].unique())
st.write("Buses in this route: ", ubusCount, "Government Buses: ", len(bus_gov), "Private Buses: ", len(bus_pvt))

option3 = st.sidebar.radio("Select Bus: ", ('Government Bus', 'Private Bus'),horizontal=True)
st.write(option3)
if option3=="Government Bus":
    df1 = df[df1['busname'].isin(bus_gov[0])]
    df1['busfare'] = df1['busfare'].replace("INR ", "")

    ################
    option5 = st.sidebar.slider("Price range: ", max_value=1000, step=10)
    # st.write(option5)
    # df1['busfare']=pd.to_numeric(df1['busfare']) <option5
    df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
    df11 = df1[df1['busfare'].astype(int)<option5]

    st.sidebar.subheader("Bus Ratings")
    selected = st.sidebar.feedback("stars")
    df11['ratings'] = df11['ratings'].str.replace("New",'0')
    df12 = df11[df11['ratings'].astype(float)>=selected]
    # st.write(selected+1)
    # st.sidebar.markdown()

    st.write(df12)
    #################

    # df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]

    # st.write(df1)
elif option3 == "Private Bus":
    df1 = df[df1['busname'].isin(bus_pvt[0])]
    df1['busfare'] = df1['busfare'].replace("INR ", "")
    #######################
    option5 = st.sidebar.slider("Price range: ", max_value=1000, step=10)
    # st.write(option5)
    # df1['busfare']=pd.to_numeric(df1['busfare']) <option5
    df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
    df11 = df1[df1['busfare'].astype(int)<option5]

    st.sidebar.subheader("Bus Ratings")
    selected = st.sidebar.feedback("stars")
    df11['ratings'] = df11['ratings'].str.replace("New",'0')
    df12 = df11[df11['ratings'].astype(float)>=selected]
    # st.write(selected+1)
    # st.sidebar.markdown()

    st.write(df12)
    #######################

    # df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]

    # st.write(df1)
#######################################
# option5 = st.sidebar.slider("Price range: ", max_value=1000, step=10)
# # st.write(option5)
# # df1['busfare']=pd.to_numeric(df1['busfare']) <option5
# df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
# df11 = df1[df1['busfare'].astype(int)<option5]

# st.sidebar.subheader("Bus Ratings")
# selected = st.sidebar.feedback("stars")
# df1['ratings'] = df1['ratings'].str.replace("New",'0')
# df11 = df1[df1['ratings'].astype(float)>=selected]
# # st.write(selected+1)
# # st.sidebar.markdown()

# st.write(df11)
############################################

# df1.loc[df['busname_str'].isin]

# st.write(df1)

option4 = st.sidebar.radio("Bus Type: ", ('AC', 'Non AC'), horizontal=True)
# df1['bustypes'] = df1['bustypes'].to_string().__contains__("AC")
# df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]

# st.write(df1)


# df1 = df[str(df1['bustypes'])
df1= df1[['busname','bustypes','busfare','seatavail','wseatavail', 'ratings','ratingppl']]
############################################################################


# city_selected = st.sidebar.selectbox("FROM (City): ", (df_city['CityName']))


# # Define a function to connect to the database and fetch data
# def fetch_data_from_db():
#     # Database connection parameters
#     config = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password="iGetzy@123",
#         database = 'RedBus'
#     )
#     # Connect to the database
#     # conn = mysql.connector.connect(**config)
#     cursor = config.cursor()

#     # Define the SQL query
#     query = "SELECT RouteName,PriceStart,BusesCount,FirstBus,LastBus,RouteLink FROM routes"
    
#     # Execute the query
#     cursor.execute(query)
    
#     # Fetch all rows from the executed query
#     data = cursor.fetchall()
    
#     # Get column names
#     columns = [desc[0] for desc in cursor.description]
    
#     # Close the cursor and connection
#     cursor.close()
#     config.close()
    
#     # Convert to a DataFrame
#     df = pd.DataFrame(data, columns=columns)
    
#     return df


# def fetch_data_from_db3():
#     # Database connection parameters
#     config = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password="iGetzy@123",
#         database = 'RedBus'
#     )
#     # Connect to the database
#     # conn = mysql.connector.connect(**config)
#     cursor = config.cursor()

#     # Define the SQL query
#     query = "SELECT routeNameList,RouteLinks,busname,bustypes,dptimes,dplocs,runtime,bptimes,bplocs,nextday,ratings,ratingppl,busfare,oldfares,seatavail,wseatavail FROM bus_routes"
    
#     # Execute the query
#     cursor.execute(query)
    
#     # Fetch all rows from the executed query
#     data = cursor.fetchall()
    
#     # Get column names
#     columns = [desc[0] for desc in cursor.description]
    
#     # Close the cursor and connection
#     cursor.close()
#     config.close()
    
#     # Convert to a DataFrame
#     df3 = pd.DataFrame(data, columns=columns)
    
#     return df3

# def data_filter_by_city(city_selecte):
#     # Database connection parameters
#     config = mysql.connector.connect(
#         host='localhost',
#         user='root',
#         password="iGetzy@123",
#         database = 'RedBus'
#     )
#     # Connect to the database
#     # conn = mysql.connector.connect(**config)
#     cursor = config.cursor()

#     # Define the SQL query
#     query = "SELECT RouteName,PriceStart,BusesCount,FirstBus,LastBus,RouteLink FROM routes WHERE RouteName LIKE '{}%'".format(city_selecte)
    
#     # Execute the query
#     cursor.execute(query)
    
#     # Fetch all rows from the executed query
#     data = cursor.fetchall()
    
#     # Get column names
#     columns = [desc[0] for desc in cursor.description]
    
#     # Close the cursor and connection
#     cursor.close()
#     config.close()
    
#     # Convert to a DataFrame
#     df = pd.DataFrame(data, columns=columns)
    
#     return df5

# # Streamlit app layout
# # col1, col2 = st.columns([3, 1])
# # col1.subheader("Routes and Bus Details")
# # with col1:
# #     st.write("Busses from ",city_selected)

# ###Fetch data from MySQL database
# df = fetch_data_from_db()
# df5 = data_filter_by_city(city_selected)


# # # Display the DataFrame in the Streamlit app
# #     st.write(df)

# to_city = st.sidebar.selectbox("TO (City): ", (df['RouteName'].str.replace("{} to".format(city_selected),"")))
# df2 = df[df['RouteName'].str.contains(to_city)]
# st.write(df2)


# df3 = fetch_data_from_db3()



# df4 = df2['RouteName']
# routeselected = df4.to_list()
# st.write(routeselected[0])

# df3 = df3[df3['routeNameList'].str.contains(routeselected[0])]
# st.write(df3)

# # col2.subheader("ROUTE")
# # col2.write(routeselected[0])
# # col2.write("No of Buses: {}".format(df3['routeNameList'].count()))

# st.sidebar.title("BUS FILTERS")


# genre = st.sidebar.radio("", ["A/C", "Non-AC"],horizontal=True)

# option = st.sidebar.selectbox("Bus types",(df3['bustypes'].unique()),index=None,placeholder="Select bus type...")
# fare = st.sidebar.slider("Fares", 0, 2000, (100,200))
# st.sidebar.subheader("Bus Ratings")
# selected = st.sidebar.feedback("stars")

# # st.write(df['RouteName'].str.replace("{} to".format(city_selected),""))
