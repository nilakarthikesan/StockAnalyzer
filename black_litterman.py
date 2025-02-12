from pypfopt import risk_models, expected_returns, BlackLittermanModel, EfficientFrontier
from data_fetching import start_date, end_date
import yfinance as yf
from data_fetching import tickers
import numpy as np
from OpenAI_stock_analyzer import assets

risk_free_rate = 0.001

# Download historical data
df = yf.download(tickers, start=start_date, end=end_date)
print("Available columns:", df.columns)  # Debugging step

if 'Adj Close' in df.columns:
    df = df['Adj Close']
else:
    print("Warning: 'Adj Close' column not found. Check ticker symbols.")
    df = None  # Handle missing data gracefully

# Proceed only if df is not None
if df is not None:
    mu = expected_returns.mean_historical_return(df)
    S = risk_models.sample_cov(df)

# Market Capitalization
mcap = {}

for ticker in tickers:
    try:
        stock = yf.Ticker(ticker)
        mcap[ticker] = stock.info.get('marketCap', None)  # Use `.get()` to avoid KeyError
    except Exception as e:
        print(f"Error fetching market cap for {ticker}: {e}")
        mcap[ticker] = None  # Default to None in case of error

mcap['SPY'] = 45000000000
print(mcap)

Q = np.array([0.05]) # Microsoft beats Google by 5% 
print(Q)
P = np.zeros((1, len(assets)))
print(P)
P[0, assets.index('MSFT')] = 1
P[0, assets.index('GOOGL')] = -1