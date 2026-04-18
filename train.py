import os
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dropout, Dense

ticker = "GOOG"
start_date = "2012-01-01"
end_date = "2022-12-31"

df = yf.download(ticker, start=start_date, end=end_date)
close_prices = df['Close'].values.reshape(-1, 1)

train_size = int(len(close_prices) * 0.8)
train_data = close_prices[:train_size]

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(train_data)

x_train = []
y_train = []
for i in range(100, len(scaled_data)):
    x_train.append(scaled_data[i-100:i, 0])
    y_train.append(scaled_data[i, 0])

x_train, y_train = np.array(x_train), np.array(y_train)
x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

model = Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=60, return_sequences=True))
model.add(Dropout(0.3))
model.add(LSTM(units=80, return_sequences=True))
model.add(Dropout(0.4))
model.add(LSTM(units=120))
model.add(Dropout(0.5))
model.add(Dense(units=1))
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(x_train, y_train, epochs=50, batch_size=32)

model_dir = os.path.join(os.path.dirname(__file__), "model")
os.makedirs(model_dir, exist_ok=True)

model_path = os.path.join(model_dir, "stock_predictions_model.keras")
model.save(model_path)
