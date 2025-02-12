import yfinance as yf
import pandas as pd

# Define the list of tickers
tickers = ['AAPL', 'AMZN', 'BTC-USD', 'GOOGL', 'META', 'MSFT', 'NVDA', 'SPY', 'TSLA']

# Define the start and end dates
start_date = '2022-01-01'
end_date = '2023-12-31'

# Create an empty dictionary to store the data
stock_data = {}

# Download the data for each ticker
for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    stock_data[ticker] = yf.download(ticker, start=start_date, end=end_date)

# Optionally, you can save the data to CSV files
for ticker, data in stock_data.items():
    data.to_csv(f"{ticker}_data.csv")

# If you want to combine all data into a single DataFrame
combined_data = pd.concat(stock_data, axis=1)

# Display the first few rows of the combined data
print(combined_data.head())