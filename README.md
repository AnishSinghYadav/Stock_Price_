# Indian Stock Market Live Tracker

## 📌 Overview
The **Indian Stock Market Live Tracker** is a Streamlit-based web application that provides real-time stock market data for NSE stocks and indices. Since there is no official API for Indian stock markets, this project utilizes web scraping to fetch live prices, making it an essential tool for traders and investors.

## 🚀 Features
- **📈 Real-time NSE Stock Prices**: Live tracking of all NSE-listed stocks.
- **🔍 Stock Search Functionality**: Search for specific stocks and view real-time prices.
- **📊 NSE Indices Tracking**: View live prices of major indices like NIFTY 50 and BANK NIFTY.
- **📉 Interactive Data Visualizations**: Uses Plotly for dynamic stock price trends.
- **💾 Optimized Performance**: Data caching to improve performance.

## 🛠️ Technologies Used
- **Python** - Core programming language.
- **Streamlit** - For building the interactive web application.
- **Requests & BeautifulSoup** - Web scraping to fetch live stock data.
- **Pandas** - Data handling and analysis.
- **Plotly** - For interactive charts and visualizations.

## 📂 Project Structure
```
Indian-Stock-Market-Live-Tracker/
│── app.py             # Main Streamlit application
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
│── nse_logo.png       # NSE logo (used in sidebar)
```

## ⚙️ Installation & Setup
### Step 1: Clone the Repository
```sh
git clone https://github.com/your-username/Indian-Stock-Market-Live-Tracker.git
cd Indian-Stock-Market-Live-Tracker
```

### Step 2: Install Dependencies
```sh
pip install -r requirements.txt
```

### Step 3: Run the Application
```sh
streamlit run app.py
```

## 📸 Screenshots
- **🏠 Home Page**:
<img width="1710" alt="Screenshot 2025-02-12 at 6 16 53 PM" src="https://github.com/user-attachments/assets/98485fb0-97c6-4cec-9157-2630aa157672" />
- **🔍 Stock Search Feature**:
<img width="1710" alt="Screenshot 2025-02-12 at 6 17 17 PM" src="https://github.com/user-attachments/assets/0b4a9c45-83bc-43cd-baa6-afb9719eaf36" /> 
- **📊 NSE Indices Page**:
<img width="1710" alt="Screenshot 2025-02-12 at 6 17 49 PM" src="https://github.com/user-attachments/assets/fd92c1c3-4638-40c5-9e34-1a077b12d9b5" />

## ⚠️ Limitations
- **No Official API for Indian Stocks**: Web scraping is used since there is no free API.
- **BSE Data is Not Included**: Due to strict bot detection on BSE’s website, only NSE stocks and indices are available.

## 📌 Future Enhancements
- ✅ Add historical stock data trends.
- ✅ Expand coverage to more indices.
- ✅ Integrate stock news feed for better insights.


### 🏆 Contribute
Contributions are welcome! Feel free to fork this repository and submit a pull request.

💡 If you find this project helpful, don’t forget to **star ⭐ this repository!**

