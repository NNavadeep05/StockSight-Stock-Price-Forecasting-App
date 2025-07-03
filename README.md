# 📈 Stock Market Analytics & Visualization 📊
**Tech:** Python (Streamlit, yfinance, Pandas, Matplotlib, scikit-learn) • Jupyter
**Role:** Data Analyst | Self-Project | July'25

## 🚀 Project Summary
Developed a web-based application for visualizing and analyzing historical stock market data. This solution enables users to fetch stock data, view historical trends, and analyze moving averages through an interactive Streamlit interface.

## 🔧 Key Contributions
- 🔗 **Automated Data Ingestion:** Implemented `yfinance` to automatically fetch historical stock data for any specified ticker.
- 📊 **Interactive Web UI:** Built a user-friendly web application using Streamlit for dynamic input and real-time visualization of stock data.
- 📈 **Trend Visualization:** Developed robust plotting functions using Matplotlib to display historical prices, 50-day, 100-day, and 200-day Simple Moving Averages (SMA) for comprehensive trend analysis.
- 🧮 **Data Preprocessing:** Utilized `scikit-learn`'s `MinMaxScaler` for efficient data scaling, a common practice in data analysis pipelines.

## 🧠 Notable Insights
- Moving averages (MA50, MA100, MA200) serve as crucial indicators for understanding market sentiment and potential support/resistance.
- Data visualization highlights seasonal trends and price patterns for various stock symbols.
- Efficient data handling with Pandas enables quick analysis of large datasets.

## 📂 Files
| File | Purpose |
|-----------------------------------|---------------------------------------------|
| `app.py` | Streamlit web application: Fetches data, performs analysis, and displays visualizations |
| `Stock_Market_Prediction_Model_Creation.ipynb` | Jupyter Notebook: Details the process of data preparation, trend analysis, and potentially early model exploration (though the model itself is not part of the final `app.py` in this README) |

## ▶️ How to Run
1.  **Install Dependencies:** Ensure you have Python 3.7+ and install all required libraries:
    ```bash
    pip install streamlit yfinance pandas numpy matplotlib scikit-learn
    ```
    *(Note: `tensorflow` is no longer strictly required if the Keras model is removed and no other ML models are used).*
2.  **Launch Application:** Navigate to the project directory in your terminal and run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
3.  **Explore!** Your browser will open the application. Enter any stock symbol (e.g., `GOOG`, `AAPL`) to start exploring historical data and moving average visualizations.

---

*(Consider adding a "License" section if applicable)*
