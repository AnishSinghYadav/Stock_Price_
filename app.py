import streamlit as st
import pandas as pd
import requests
import plotly.express as px
import time

# Page Configuration
st.set_page_config(
    page_title="Stock Market Tracker",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling with Aesthetic Black Theme
st.markdown("""
    <style>
        body {
            font-family: 'Roboto', sans-serif;
            background-color: #121212;
            color: #ffffff;
        }
        .stApp {
            background: linear-gradient(145deg, #000000, #1a1a1a);
        }
        .stSidebar {
            background: linear-gradient(145deg, #000000, #222222);
            color: white;
        }
        .stButton>button {
            background: linear-gradient(145deg, #00bcd4, #0097a7);
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 24px;
            font-size: 16px;
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(145deg, #0097a7, #00bcd4);
            transform: scale(1.05);
        }
        .card {
            background: #1e1e1e;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 255, 255, 0.2);
            transition: all 0.3s ease;
        }
        .card:hover {
            box-shadow: 0 8px 24px rgba(0, 255, 255, 0.3);
            transform: translateY(-5px);
        }
    </style>
""", unsafe_allow_html=True)

# Function to fetch all NSE-listed stocks
@st.cache_data(ttl=60)
def get_all_nse_stocks():
    url = "https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050"
    headers = {"User-Agent": "Mozilla/5.0"}
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame([{ "Company Name": stock['symbol'], "Live Price": stock['lastPrice'], "Previous Close": stock['previousClose'] } for stock in data['data']])
    return pd.DataFrame()

# Function to fetch NSE Indices
@st.cache_data(ttl=60)
def get_nse_indices():
    url = "https://www.nseindia.com/api/allIndices"
    headers = {"User-Agent": "Mozilla/5.0"}
    session = requests.Session()
    session.get("https://www.nseindia.com", headers=headers)
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame([{ "Index Name": index['index'], "Live Price": index['last'], "Previous Close": index['previousClose'] } for index in data['data']])
    return pd.DataFrame()

# Sidebar
with st.sidebar:
    st.image("nse_logo.png", width=300)
    st.markdown("<h2 style='color:#00bcd4;'>📊 Live Stock Tracker</h2>", unsafe_allow_html=True)

# Page Title
st.markdown("<h1 style='color:#00bcd4; text-align:center;'>📈 Indian Stock Market Live Tracker</h1>", unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📈 All NSE Stocks", "🔍 Search Stock", "📊 NSE Indices"])

# Tab 1: All NSE Stocks
with tab1:
    st.header("📊 All NSE Stocks")
    with st.spinner('Fetching live stock data...'):
        stock_df = get_all_nse_stocks()
        time.sleep(1)
    if not stock_df.empty:
        stock_df["% Change"] = ((stock_df["Live Price"] - stock_df["Previous Close"]) / stock_df["Previous Close"]) * 100
        stock_df["% Change"] = stock_df["% Change"].apply(lambda x: f"{x:.2f}%")
        st.dataframe(stock_df, height=500)

# Tab 2: Search Stock
with tab2:
    st.header("🔍 Search for a Specific Stock")
    search_query = st.text_input("Enter Stock Name (e.g., RELIANCE, TCS, INFY):")
    if search_query:
        filtered_df = stock_df[stock_df["Company Name"].str.contains(search_query, case=False, na=False)]
        if not filtered_df.empty:
            st.dataframe(filtered_df, height=250)
            fig = px.bar(filtered_df, x="Company Name", y="Live Price", text="Live Price", title="Live Price of Selected Stock", color="Live Price")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("Stock not found! Try another search.")

# Tab 3: NSE Indices
with tab3:
    st.header("📊 NSE Indices (NIFTY 50, BANK NIFTY, etc.)")
    with st.spinner('Fetching live indices data...'):
        indices_df = get_nse_indices()
        time.sleep(1)
    if not indices_df.empty:
        st.dataframe(indices_df, height=400)
        fig = px.line(indices_df, x="Index Name", y="Live Price", markers=True, title="NSE Indices Live Trend")
        st.plotly_chart(fig, use_container_width=True)
