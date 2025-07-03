# 📈 StockSight: Stock Market Analytics & Visualization 📊
**Tech:** Python (Streamlit, yfinance, Pandas, Matplotlib, scikit-learn) • Jupyter
**Role:** Data Analyst | Self-Project | July'25

## 🚀 Project Summary
**StockSight** is a web application designed for comprehensive stock market analytics and visualization. It enables users to seamlessly fetch and analyze historical market data, providing interactive charting capabilities for trends and key indicators through an intuitive Streamlit interface.

## 🔧 Key Contributions
- 🔗 **Automated Data Ingestion:** Implemented `yfinance` to automatically fetch historical stock data for any specified ticker, ensuring fresh and relevant analysis.
- 📊 **Interactive Web UI:** Built a user-friendly web application using Streamlit for dynamic stock symbol input and real-time visualization of historical data.
- 📈 **Comprehensive Trend Visualization:** Developed robust plotting functions using Matplotlib to display historical prices alongside 50-day, 100-day, and 200-day Simple Moving Averages (SMA) for in-depth trend analysis.
- 🧮 **Optimized Data Preprocessing:** Utilized `MinMaxScaler` from `scikit-learn` for efficient data scaling, a common practice for preparing time-series data for analysis.

## 🧠 Notable Insights
- Moving averages (MA50, MA100, MA200) serve as crucial technical indicators for understanding market sentiment and identifying potential support/resistance levels.
- The interactive visualizations allow for quick identification of historical price patterns, volatility, and long-term trends.
- Efficient data handling with Pandas enables rapid analysis and manipulation of large datasets.

## 📂 Files
| File | Purpose |
|-----------------------------------|---------------------------------------------|
| `app.py` | Streamlit web application: Fetches data, performs analysis, and displays visualizations |
| `Stock_Market_Prediction_Model_Creation.ipynb` | Jupyter Notebook: Details the process of data preparation and trend analysis. (Note: The predictive model aspect of this notebook is not featured in the `app.py` description here.) |

## ▶️ How to Run
1.  **Install Dependencies:** Ensure you have Python 3.7+ and install all required libraries:
    ```bash
    pip install streamlit yfinance pandas numpy matplotlib scikit-learn
    ```
    *(Note: `tensorflow` is no longer listed as a strict dependency if no Keras model is used for prediction.)*
2.  **Launch Application:** Navigate to the project directory in your terminal and run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3.  **Explore!** Your browser will open the application. Enter any stock symbol (e.g., `GOOG`, `AAPL`) to start exploring historical data and moving average visualizations.

---

*(Consider adding a "License" section if applicable)*
