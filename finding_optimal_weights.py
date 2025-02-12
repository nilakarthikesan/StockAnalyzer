import numpy as np
import pandas as pd
import yfinance as yf
from scipy.optimize import minimize

# Define the assets and the time period
assets = ['AAPL', 'AMZN', 'BTC-USD', 'GOOGL', 'META', 'MSFT', 'NVDA', 'SPY', 'TSLA']
start_date = '2022-01-01'
end_date = '2023-12-31'
risk_free_rate = 0.04

# Fetch the adjusted closing prices of the assets
data = yf.download(assets, start=start_date, end=end_date)

# Print data columns to debug
print("Available columns:", data.columns)
print(data.head())

# Ensure we have data
if data.empty:
    print("Error: No data retrieved. Check the ticker symbols or the date range.")
    exit()

# Use 'Close' if 'Adj Close' is not available
if 'Adj Close' in data.columns:
    prices = data['Adj Close']
else:
    prices = data['Close']

# Check if we are missing tickers
missing_tickers = [ticker for ticker in assets if ticker not in data.columns]
if missing_tickers:
    print("Warning: No data found for these tickers:", missing_tickers)

# Calculate daily returns
returns = prices.pct_change().dropna()

# Calculate the mean returns and the covariance matrix
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Function to calculate portfolio performance
def portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate):
    returns = np.sum(mean_returns * weights) * 252
    std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = (returns - risk_free_rate) / std
    return std, returns, sharpe_ratio

# Function to minimize (negative Sharpe Ratio)
def neg_sharpe_ratio(weights, mean_returns, cov_matrix, risk_free_rate):
    return -portfolio_performance(weights, mean_returns, cov_matrix, risk_free_rate)[2]

# Constraints and bounds
constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})
bounds = tuple((0, 1) for _ in range(len(assets)))

# Initial guess (equal distribution)
init_guess = len(assets) * [1. / len(assets)]

# Optimize the portfolio
opt_results = minimize(neg_sharpe_ratio, init_guess, args=(mean_returns, cov_matrix, risk_free_rate),
                       method='SLSQP', bounds=bounds, constraints=constraints)

# Get the optimal weights
optimal_weights = opt_results.x

# Print the weights with two decimal cases
weights_dict = {asset: round(weight, 2) for asset, weight in zip(assets, optimal_weights)}
print("Optimal Weights:", weights_dict)
