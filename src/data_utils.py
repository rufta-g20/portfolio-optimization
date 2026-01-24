import yfinance as yf
import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

def fetch_financial_data(tickers, start_date, end_date):
    """Fetches Adjusted Close price data from Yahoo Finance."""
    print(f"Fetching data for {tickers}...")
    
    # Download data
    data = yf.download(tickers, start=start_date, end=end_date)
    
    # Check if 'Adj Close' exists in the columns
    if 'Adj Close' in data.columns:
        return data['Adj Close']
    else:
        # Fallback: some versions use 'Close' which is already adjusted 
        # or have a MultiIndex where you need to slice it
        print("Note: 'Adj Close' not found, using 'Close' columns.")
        return data['Close']

def clean_data(df):
    """Handles missing values using linear interpolation."""
    return df.interpolate(method='linear').dropna()

def perform_adf_test(series, name):
    """Performs the Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(series)
    status = "Stationary" if result[1] <= 0.05 else "Non-Stationary"
    results_dict = {
        "Ticker": name,
        "ADF Statistic": round(result[0], 4),
        "p-value": round(result[1], 4),
        "Interpretation": status
    }
    return results_dict

def calculate_risk_metrics(returns, annual_rf=0.02):
    """Calculates Sharpe Ratio and 95% Value at Risk (VaR)."""
    daily_rf = annual_rf / 252 
    excess_returns = returns - daily_rf
    sharpe = (excess_returns.mean() / returns.std()) * np.sqrt(252)
    var_95 = np.percentile(returns, 5)
    return sharpe, var_95