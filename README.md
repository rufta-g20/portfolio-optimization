# Time Series Forecasting for Portfolio Management Optimization

## Business Objective

Guide Me in Finance (GMF) Investments is a forward-thinking financial advisory firm specializing in personalized portfolio management. The company leverages cutting-edge technology and data-driven insights to provide tailored investment strategies. By integrating advanced time series forecasting models, GMF aims to predict market trends, optimize asset allocation, and enhance portfolio performance. The primary goal is to help clients achieve financial objectives by minimizing risks and capitalizing on market opportunities.

## Project Overview

This project focuses on applying time series forecasting to historical financial data for three key assets: **Tesla (TSLA)**, **Vanguard Total Bond Market ETF (BND)**, and **S&P 500 ETF (SPY)**. The workflow involves data extraction, preprocessing, exploratory data analysis, and the development of predictive models (ARIMA and LSTM) to inform portfolio recommendations.

## Project Structure

```text
portfolio-optimization/
├── .vscode/
│   └── settings.json           # Editor settings
├── .github/
│   └── workflows/
│       └── unittests.yml       # CI/CD pipeline for automated testing 
├── .gitignore                  # Files to exclude from Git
├── requirements.txt            # Project dependencies 
├── README.md                   # Project documentation
├── data/
│   └── processed/              # Cleaned and processed datasets 
├── notebooks/
│   ├── __init__.py
│   ├── EDA_Financial_Data_Task1.ipynb         # Data exploration and analysis
│   ├── Time_Series_Forecasting_Task2.ipynb    # Forecasting model development
│   ├── Future_Forecasting_Task3.ipynb         # Future trend & risk projection
│   ├── Optimization_Task4.ipynb
│   ├── Backtesting_Task5.ipynb
│   └── README.md
├── src/
│   ├── __init__.py             # Source code for modular logic 
│   └── data_utils.py           # Modularized logic for scaling & modeling
├── models/
│   └── tsla_lstm_model.keras    # Saved trained LSTM model
├── tests/
│   └── __init__.py             # Unit tests 
└── scripts/
    └── __init__.py             # Execution scripts 

```

## Getting Started & Setting Up

### Prerequisites

* Python 3.8 or higher
* `pip` package manager

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/rufta-g20/portfolio-optimization.git
cd portfolio-optimization

```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```

3. **Install dependencies:**
```bash
pip install -r requirements.txt

```

### Usage

* To explore the data and preprocessing steps, open `notebooks/EDA_Financial_Data_Task1.ipynb`.
* To view or train the forecasting models, run `notebooks/Time_Series_Forecasting_Task2.ipynb`.

## Key Insights So Far

### Task 1: Preprocessing and EDA

* **Data Quality:** Cleaned historical data (2015-2026) using linear interpolation for missing values.
* **Stationarity:** Raw prices were found to be non-stationary, while daily returns are stationary (-value = 0.0000), justifying the use of differencing for modeling.
* **Risk Metrics:** Identified TSLA as a high-risk/high-reward asset (VaR -5.25%) compared to the stability of BND.

### Task 2: Forecasting Models

* **ARIMA:** Identified an ARIMA(0,1,0) "Random Walk" model as the baseline, which suggests that price movements are highly efficient and difficult to predict with linear statistical methods.
* **LSTM:** A Deep Learning LSTM model significantly outperformed ARIMA, capturing non-linear volatility clusters and momentum factors with a MAPE of approximately 5.07%.
* **Model Selection:** Selected LSTM for future forecasting due to its ability to capture non-linear volatility clusters.

![LSTM vs ARIMA](../notebooks/output5.png)

### Task 3: Future Market Trends

* **Forecast:** Generated a 6-month recursive forecast for TSLA with 95% confidence intervals.
* **Risk Assessment:** Identified a "Fan Chart" effect, where uncertainty increases over time, suggesting the model is most effective for tactical 30-day outlooks.
* **Opportunities:** Identified potential price momentum windows while quantifying the downside risk via widening lower bounds.

The LSTM model captures the "Fan Chart" effect, where uncertainty expands as the forecast horizon grows.
![TSLA Forecast](../notebooks/output6.png)

### Task 4: Portfolio Optimization

* **Optimization Framework:** Applied Modern Portfolio Theory (MPT) to combine the LSTM "Active View" of TSLA with historical data for BND and SPY.
* **Asset Correlation:** Identified a strong positive correlation between SPY and TSLA (0.86), while BND remains negatively correlated (-0.8), confirming its role as a hedge.
* **Optimal Allocation:** The Maximum Sharpe Ratio portfolio recommended a 100% allocation to SPY, effectively avoiding TSLA due to its negative forecasted return (-78.84%) and high volatility.
* **Risk-Return Tradeoff:** Successfully mapped the Efficient Frontier, identifying a portfolio with an expected annual return of 13.54% and a Sharpe Ratio of 0.24.

The Efficient Frontier identifies the Max Sharpe and Min Volatility portfolios based on forecasted returns.
![Efficient Frontier](../notebooks/output8.png)

### Task 5: Strategy Backtesting

* **Backtest Window:** Validated the optimized strategy against a 60/40 (SPY/BND) benchmark from January 2025 to January 2026.
* **Performance Results:** The 60/40 benchmark outperformed the 100% SPY optimized strategy (21.11% vs. 15.80% total return), highlighting the importance of diversification.
* **Risk Mitigation:** The LSTM-driven strategy successfully avoided a 100% loss exposure to TSLA's volatility, though it suffered a higher drawdown than the balanced benchmark.
* **Strategic Conclusion:** Future iterations should combine LSTM price forecasts with Risk Parity constraints to balance growth and capital preservation.

A comparison of the AI-Optimized strategy against a traditional 60/40 benchmark.
![Backtest Results](../notebooks/output9.png)