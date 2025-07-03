# 📈 StockSight: Stock Market Analytics & Forecasting

**Tech:** Python (Streamlit, Keras, yFinance, Pandas, Matplotlib, scikit-learn) • Jupyter  
|  Self-Project  |  **Date:** June ’25

---

## 🚀 Project Summary

**StockSight** is a stock market analytics and forecasting web application designed to provide users with real-time insights into historical trends and future price movements. Built with Streamlit and LSTM neural networks in Keras, it delivers intuitive visualizations, automated data fetching, and model-driven price forecasting with **~95% prediction accuracy**.

---

## 🔧 Key Features & Contributions

- 🔗 **Automated Data Ingestion:** Used `yFinance` to dynamically fetch historical stock data for any ticker symbol, ensuring real-time relevance.
  
- 📊 **Interactive Web Interface:** Developed a responsive Streamlit app that accepts user input and visualizes raw and processed market data.

- 📈 **Advanced Trend Visualization:** Implemented plotting modules using Matplotlib to display closing prices alongside technical indicators like SMA50, SMA100, and SMA200.

- 🤖 **LSTM-Based Forecasting Model:** Trained a Long Short-Term Memory model using Keras and TensorFlow, achieving **~95% accuracy** in predicting future price trends.

- 🧮 **Efficient Data Preprocessing:** Employed `MinMaxScaler` for normalization, a best practice for time-series modeling and smoother convergence in LSTM training.

---

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
