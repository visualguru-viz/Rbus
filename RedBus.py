import streamlit as st

st.set_page_config(
    page_title="RedBus Data Insights",
    page_icon="👋",
)

st.write("# Redbus Data Scraping and Streamlit Visualization")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    It aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, 
    analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this libraries automates 
    the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability.
    By streamlining data collection and providing powerful interface for data-driven decision-making. 
    This data can significantly improve operational efficiency and strategic planning in the transportation industry. 
    ### Use Cases:
    - Travel Aggregators: Find real-time bus schedules and seat availability for customers.
    - Market Analysis: Details of ravel patterns and data driven analysis.
    - Competitor Analysis: Pricing and service levels comparison with competitors.

    ### Data Scraping:
    Automated the extraction of Redbus data including routes, schedules, prices, and seat availability by Python Selenium.
    Scraped data stored as civ files and then write into SQL to avoid and site latency.

    ### Data Storage:
    Stored the scraped data in MySQL database.

    ### Streamlit:
    Used Streamlit to for data visualisation and filter the scraped data.

    ### Data Set:
    Consist 10 Government State Bus Transport data from Redbus website including private bus information for the selected routes.
"""
)