# 📈 Stock Market Predictor 🚀
**Tech:** Python (Keras, Streamlit, yfinance, Pandas, Matplotlib, scikit-learn) • Jupyter
**Role:** Data Scientist / ML Engineer | Self-Project | July'25

## 🚀 Project Summary
Developed an end-to-end stock market prediction application with a deep learning model, capable of forecasting future stock prices and visualizing historical trends. The solution integrates data fetching, model inference, and interactive charting via a Streamlit web interface.

## 🔧 Key Contributions
- 🧠 **Deep Learning Model:** Engineered, trained, and deployed a Keras-based neural network for accurate stock price predictions.
- 🔗 **Automated Data Ingestion:** Implemented `yfinance` to automatically fetch real-time historical stock data.
- 📊 **Interactive Web UI:** Built a user-friendly web application using Streamlit for dynamic input and real-time visualization of stock data and predictions.
- 📈 **Trend Visualization:** Developed robust plotting functions using Matplotlib to display historical prices, 50-day, 100-day, and 200-day moving averages for comprehensive trend analysis.
- 🧮 **Data Preprocessing:** Implemented `MinMaxScaler` for efficient data scaling, optimizing model training and performance.

## 🧠 Notable Insights
- Model effectively captures underlying price patterns and trend reversals.
- Moving averages (MA50, MA100, MA200) serve as crucial indicators for understanding market sentiment and potential support/resistance.
- Scaled data significantly improves the convergence and performance of the deep learning model.

## 📂 Files
| File | Purpose |
|-----------------------------------|---------------------------------------------|
| `app.py` | Streamlit web application: Fetches data, loads model, displays predictions & visualizations |
| `Stock_Market_Prediction_Model_Creation.ipynb` | Jupyter Notebook: Detailed model creation, training, and evaluation pipeline |
| `Stock Predictions Model.keras` | Pre-trained Keras deep learning model for predictions |
| `screenshots/` | Folder containing visual demonstrations of the application |

## ▶️ How to Run
1.  **Install Dependencies:** Ensure you have Python 3.7+ and install all required libraries:
    ```bash
    pip install streamlit tensorflow yfinance pandas numpy matplotlib scikit-learn
    ```
2.  **Model Setup:**
    * Run `Stock_Market_Prediction_Model_Creation.ipynb` to train and save the `Stock Predictions Model.keras` file.
    * **Crucially:** Update the model loading path in `app.py` from `'C:\\Python\\Stock\\Stock Predictions Model.keras'` to `'Stock Predictions Model.keras'` (assuming the model file is in the same directory as `app.py`).
3.  **Launch Application:** Navigate to the project directory in your terminal and run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
4.  **Explore!** Your browser will open the application. Enter any stock symbol (e.g., `GOOG`, `AAPL`) to start exploring predictions and visualizations.

---
*(Consider adding a "License" section if applicable)*
