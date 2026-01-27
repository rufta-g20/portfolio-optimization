import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, mean_absolute_percentage_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout, Input

def fetch_financial_data(tickers, start_date, end_date):
    print(f"Fetching data for {tickers}...")
    data = yf.download(tickers, start=start_date, end=end_date)
    return data['Adj Close'] if 'Adj Close' in data.columns else data['Close']

def clean_data(df):
    return df.interpolate(method='linear').dropna()

def perform_adf_test(series, name):
    result = adfuller(series)
    status = "Stationary" if result[1] <= 0.05 else "Non-Stationary"
    return {"Ticker": name, "ADF Statistic": round(result[0], 4), "p-value": round(result[1], 4), "Interpretation": status}

def calculate_risk_metrics(returns, annual_rf=0.02):
    daily_rf = annual_rf / 252 
    excess_returns = returns - daily_rf
    sharpe = (excess_returns.mean() / returns.std()) * np.sqrt(252)
    var_95 = np.percentile(returns, 5)
    return sharpe, var_95

def prepare_lstm_data(data, window_size=60):
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data.values.reshape(-1, 1))
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i-window_size:i, 0])
        y.append(scaled_data[i, 0])
    return np.array(X), np.array(y), scaler

def build_lstm_model(input_shape):
    """Modular function to define the LSTM architecture."""
    model = Sequential([
        Input(shape=input_shape), # Use Input layer to avoid warnings
        LSTM(units=50, return_sequences=True),
        Dropout(0.2),
        LSTM(units=50, return_sequences=False),
        Dropout(0.2),
        Dense(units=1)
    ])
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

def evaluate_model(actual, pred, model_name):
    # Ensure both are converted to numpy arrays and flattened
    actual, pred = np.array(actual).flatten(), np.array(pred).flatten()
    # Create a mask to remove any NaNs from either actual or pred
    mask = ~np.isnan(actual) & ~np.isnan(pred)
    actual_clean, pred_clean = actual[mask], pred[mask]
    
    if len(actual_clean) == 0:
        return {"Model": model_name, "MAE": np.nan, "RMSE": np.nan, "MAPE": np.nan}

    return {
        "Model": model_name,
        "MAE": mean_absolute_error(actual_clean, pred_clean),
        "RMSE": np.sqrt(mean_squared_error(actual_clean, pred_clean)),
        "MAPE": mean_absolute_percentage_error(actual_clean, pred_clean)
    }