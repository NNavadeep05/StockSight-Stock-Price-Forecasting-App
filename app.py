import os
import datetime
import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from keras.models import load_model

st.set_page_config(page_title="StockSight", layout="wide")

plt.style.use('dark_background')

st.title("StockSight: Stock Price Forecasting App")

ticker = st.text_input("Enter Stock Ticker", value="GOOG")

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Start Date", value=datetime.date(2012, 1, 1))
with col2:
    end_date = st.date_input("End Date", value=datetime.date.today())

df = yf.download(ticker, start=start_date, end=end_date)

st.subheader("Raw Data")
st.write(df)

df['MA50'] = df['Close'].rolling(window=50).mean()
df['MA100'] = df['Close'].rolling(window=100).mean()
df['MA200'] = df['Close'].rolling(window=200).mean()

st.subheader("Close Price vs MA50")
fig1, ax1 = plt.subplots(figsize=(12, 5))
ax1.plot(df.index, df['Close'], label='Close Price', color='blue')
ax1.plot(df.index, df['MA50'], label='MA50', color='orange')
ax1.set_title("Close Price vs MA50")
ax1.set_xlabel("Date")
ax1.set_ylabel("Price USD")
ax1.legend()
st.pyplot(fig1)

st.subheader("Close Price vs MA50 and MA100")
fig2, ax2 = plt.subplots(figsize=(12, 5))
ax2.plot(df.index, df['Close'], label='Close Price', color='blue')
ax2.plot(df.index, df['MA50'], label='MA50', color='orange')
ax2.plot(df.index, df['MA100'], label='MA100', color='green')
ax2.set_title("Close Price vs MA50 and MA100")
ax2.set_xlabel("Date")
ax2.set_ylabel("Price USD")
ax2.legend()
st.pyplot(fig2)

st.subheader("Close Price vs MA100 and MA200")
fig3, ax3 = plt.subplots(figsize=(12, 5))
ax3.plot(df.index, df['Close'], label='Close Price', color='blue')
ax3.plot(df.index, df['MA100'], label='MA100', color='green')
ax3.plot(df.index, df['MA200'], label='MA200', color='red')
ax3.set_title("Close Price vs MA100 and MA200")
ax3.set_xlabel("Date")
ax3.set_ylabel("Price USD")
ax3.legend()
st.pyplot(fig3)

st.subheader("Model Predictions")

model_path = os.path.join(os.path.dirname(__file__), "model", "stock_predictions_model.keras")

if os.path.exists(model_path):
    model = load_model(model_path)
    
    close_prices = df['Close'].values.reshape(-1, 1)
    
    train_size = int(len(close_prices) * 0.8)
    train_data = close_prices[:train_size]
    test_data = close_prices[train_size:]
    test_dates = df.index[train_size:]
    
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaler.fit(train_data)
    
    last_100_train = train_data[-100:]
    inputs = np.concatenate((last_100_train, test_data), axis=0)
    inputs_scaled = scaler.transform(inputs)
    
    x_test = []
    y_test = []
    for i in range(100, len(inputs_scaled)):
        x_test.append(inputs_scaled[i-100:i, 0])
        y_test.append(inputs_scaled[i, 0])
        
    x_test, y_test = np.array(x_test), np.array(y_test)
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    
    predictions = model.predict(x_test)
    
    predictions_inv = scaler.inverse_transform(predictions)
    y_test_inv = scaler.inverse_transform(y_test.reshape(-1, 1))
    
    fig4, ax4 = plt.subplots(figsize=(12, 5))
    ax4.plot(test_dates, y_test_inv, label='Original Price', color='blue')
    ax4.plot(test_dates, predictions_inv, label='Predicted Price', color='orange')
    ax4.set_title("Original Price vs Predicted Price")
    ax4.set_xlabel("Date")
    ax4.set_ylabel("Price USD")
    ax4.legend()
    st.pyplot(fig4)
else:
    st.error("Model file not found. Please run train.py first.")