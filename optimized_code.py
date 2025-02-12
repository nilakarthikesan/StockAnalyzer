import numpy as np  # For numerical operations and matrix calculations
import pandas as pd  # For handling stock data
import yfinance as yf  # For fetching stock market data
import matplotlib.pyplot as plt  # For visualizations
import seaborn as sns  # For enhanced visualizations
from scipy.optimize import minimize  # For portfolio optimization
from pypfopt import risk_models, expected_returns, EfficientFrontier  # For Modern Portfolio Theory
from langchain_openai import ChatOpenAI  # For AI-driven summarization
# List of assets to analyze
assets = [
    "Apple (AAPL)",
    "Amazon (AMZN)",
    "Bitcoin (BTC-USD)",
    "Alphabet (GOOGL)",
    "Meta (META)",
    "Microsoft (MSFT)",
    "Nvidia (NVDA)",
    "S&P 500 index (SPY)",
    "Tesla (TSLA)"
]

# Define the start and end years for the analysis
start_year = 2022
end_year = 2023
# Analysis period
start_date = '2022-01-01'
end_date = '2023-12-31'
key = "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"

llm = ChatOpenAI(model = "gpt-4o", 
                 temperature = 0, 
                 api_key = key,)

prompt = f"""
Can you provide a python code that uses the yfinance library to download stock data. The stocks and tickers that I specfically want data for {assets} from {start_year} to {end_year}
"""

response = llm.invoke(prompt)

print("\nGenerated Python Code:\n")
print("=" * 40)
print(response.content)
print("=" * 40)


def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetches adjusted closing prices for the given tickers from Yahoo Finance.

    Parameters:
        tickers (list): List of stock tickers.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame containing adjusted closing prices for each ticker.
    """
    df = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return df

def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetches adjusted closing prices for the given tickers from Yahoo Finance.

    Parameters:
        tickers (list): List of stock tickers.
        start_date (str): Start date in 'YYYY-MM-DD' format.
        end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: DataFrame containing adjusted closing prices for each ticker.
    """
    df = yf.download(tickers, start=start_date, end=end_date)
    
    # Check if 'Adj Close' exists and extract it
    if ('Adj Close', '') in df.columns:
        return df['Adj Close']
    elif 'Adj Close' in df.columns:
        return df['Adj Close']
    else:
        print("Warning: 'Adj Close' column not found, returning full dataset.")
        return df

prices = fetch_stock_data(assets, start_date, end_date)
print(prices.head())

def compute_daily_returns(prices):
    """
    Computes daily returns for stock price data.

    Parameters:
        prices (pd.DataFrame): DataFrame of stock prices.

    Returns:
        pd.DataFrame: DataFrame of daily returns.
    """
    return prices.pct_change().dropna()

def optimize_portfolio(mean_returns, cov_matrix, risk_free_rate=0.04):
    """
    Optimizes portfolio allocation using the Sharpe Ratio maximization.

    Parameters:
        mean_returns (pd.Series): Expected returns of assets.
        cov_matrix (pd.DataFrame): Covariance matrix of asset returns.
        risk_free_rate (float): Risk-free rate, default is 0.04.

    Returns:
        dict: Optimized weights for each asset.
    """
    num_assets = len(mean_returns)
    init_guess = num_assets * [1. / num_assets]
    bounds = tuple((0, 1) for _ in range(num_assets))
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})

    def neg_sharpe_ratio(weights):
        ret = np.sum(mean_returns * weights) * 252
        std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
        return -(ret - risk_free_rate) / std

    opt_results = minimize(neg_sharpe_ratio, init_guess, method='SLSQP', bounds=bounds, constraints=constraints)
    optimal_weights = opt_results.x
    return {ticker: round(weight, 2) for ticker, weight in zip(mean_returns.index, optimal_weights)}

def get_stock_kpis(ticker):
    """
    Fetches key performance indicators (KPIs) for a given stock ticker.

    Parameters:
        ticker (str): Stock ticker.

    Returns:
        dict: KPI values including P/E Ratio, EPS, Dividend Yield, ROE, P/B Ratio, etc.
    """
    stock = yf.Ticker(ticker)
    kpis = {}

    try:
        info = stock.info
        history = stock.history(period="2y")

        kpis['PE Ratio'] = history['Close'] / info.get('trailingEps', np.nan)
        kpis['EPS'] = history['Close'] / info.get('sharesOutstanding', np.nan)
        kpis['Dividend Yield'] = stock.dividends / history['Close']
        kpis['ROE'] = info.get('returnOnEquity', np.nan)
        kpis['PB Ratio'] = history['Close'] / info.get('bookValue', np.nan)
        kpis['Debt-to-Equity Ratio'] = info.get('debtToEquity', np.nan)
        kpis['Current Ratio'] = info.get('currentRatio', np.nan)
        kpis['Free Cash Flow'] = info.get('freeCashflow', np.nan)
        kpis['Beta'] = info.get('beta', np.nan)
        kpis['Market Capitalization'] = history['Close'] * info.get('sharesOutstanding', np.nan)

    except Exception as e:
        print(f"Error fetching KPIs for {ticker}: {e}")

    return kpis

# List of assets for analysis
assets = ['AAPL', 'AMZN', 'BTC-USD', 'GOOGL', 'META', 'MSFT', 'NVDA', 'SPY', 'TSLA']

# Analysis period
start_date = '2022-01-01'
end_date = '2023-12-31'

# Risk-free rate
risk_free_rate = 0.04

# OpenAI API Key (Replace with your own)
api_key = "sk-proj-XXXXXXX"

# AI Model for summarization
llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=api_key)

# Fetch stock data
prices = fetch_stock_data(assets, start_date, end_date)

# Compute returns and covariance
returns = compute_daily_returns(prices)
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Optimize portfolio
portfolio_weights = optimize_portfolio(mean_returns, cov_matrix, risk_free_rate)
print("Optimal Portfolio Weights:", portfolio_weights)

def plot_pe_ratio(ticker):
    """
    Plots the Price-to-Earnings (P/E) Ratio over time for a stock.

    Parameters:
        ticker (str): Stock ticker.
    """
    stock = yf.Ticker(ticker)
    pe_ratio = stock.history(period="2y")['Close'] / stock.info.get('trailingEps', np.nan)
    
    plt.figure(figsize=(10, 5))
    plt.plot(pe_ratio, label="P/E Ratio")
    plt.title(f'{ticker} P/E Ratio Over Time')
    plt.xlabel('Date')
    plt.ylabel('P/E Ratio')
    plt.legend()
    plt.show()

# Example usage
plot_pe_ratio('AAPL')

def plot_eps(ticker):
    """
    Plots the Earnings Per Share (EPS) over time for a stock.

    Parameters:
        ticker (str): Stock ticker.
    """
    stock = yf.Ticker(ticker)
    eps = stock.history(period="2y")['Close'] / stock.info.get('sharesOutstanding', np.nan)
    
    plt.figure(figsize=(10, 5))
    plt.plot(eps, label="EPS", color='green')
    plt.title(f'{ticker} EPS Over Time')
    plt.xlabel('Date')
    plt.ylabel('EPS')
    plt.legend()
    plt.show()

# Example usage
plot_eps('AAPL')


