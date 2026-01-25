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
│   ├── Task_1_EDA.ipynb        # Data exploration and analysis
│   ├── Task_2_Modeling.ipynb   # Forecasting model development
│   └── README.md
├── src/
│   ├── __init__.py             # Source code for modular logic 
│   └── data_utils.py           # Helper functions for data processing
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
git clone https://github.com/your-username/portfolio-optimization.git
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

* To explore the data and preprocessing steps, open `notebooks/Task_1_EDA.ipynb`.
* To view or train the forecasting models, run `notebooks/Task_2_Modeling.ipynb`.

## Key Insights So Far

### Task 1: Preprocessing and EDA

* 
**Data Quality:** Cleaned historical data (2015-2026) using linear interpolation for missing values.


* 
**Stationarity:** Raw prices were found to be non-stationary, while daily returns are stationary (-value = 0.0000), justifying the use of differencing for modeling.


* 
**Risk Metrics:** Identified TSLA as a high-risk/high-reward asset (VaR -5.25%) compared to the stability of BND.



### Task 2: Forecasting Models

* 
**ARIMA:** Identified an ARIMA(0,1,0) "Random Walk" model as the baseline, which suggests that price movements are highly efficient and difficult to predict with linear statistical methods.


* 
**LSTM:** A Deep Learning LSTM model significantly outperformed ARIMA, capturing non-linear volatility clusters and momentum factors with a MAPE of approximately 4.7%.



## Future Tasks

* **Task 3:** Generate future market trend forecasts (6-12 months).
* 
**Task 4:** Portfolio optimization using the Efficient Frontier.
* 
**Task 5:** Strategy backtesting against a 60/40 benchmark portfolio.