### 1) Price-to-Earnings Ratio (P/E Ratio)

import yfinance as yf
import matplotlib.pyplot as plt

def plot_pe_ratio(ticker):
    stock = yf.Ticker(ticker)
    pe_ratio = stock.history(period="2y")['Close'] / stock.info['trailingEps']
    pe_ratio.plot(title=f'{ticker} P/E Ratio Over Time')
    plt.xlabel('Date')
    plt.ylabel('P/E Ratio')
    plt.show()

# Example usage
plot_pe_ratio('AAPL')

### 2) Earnings Per Share (EPS)

def plot_eps(ticker):
    stock = yf.Ticker(ticker)
    eps = stock.history(period="2y")['Close'] / stock.info['sharesOutstanding']
    eps.plot(title=f'{ticker} EPS Over Time')
    plt.xlabel('Date')
    plt.ylabel('EPS')
    plt.show()

# Example usage
plot_eps('AAPL')

### 3) Dividend Yield

def plot_dividend_yield(ticker):
    stock = yf.Ticker(ticker)
    dividends = stock.dividends
    dividend_yield = dividends / stock.history(period="2y")['Close']
    dividend_yield.plot(title=f'{ticker} Dividend Yield Over Time')
    plt.xlabel('Date')
    plt.ylabel('Dividend Yield')
    plt.show()

# Example usage
plot_dividend_yield('AAPL')


### 4) Return on Equity (ROE)

def plot_roe(ticker):
    stock = yf.Ticker(ticker)
    roe = stock.info['returnOnEquity']
    plt.plot([roe] * len(stock.history(period="2y")), label='ROE')
    plt.title(f'{ticker} ROE Over Time')
    plt.xlabel('Date')
    plt.ylabel('ROE')
    plt.show()

# Example usage
plot_roe('AAPL')


### 5) Price-to-Book Ratio (P/B Ratio)

def plot_pb_ratio(ticker):
    stock = yf.Ticker(ticker)
    pb_ratio = stock.history(period="2y")['Close'] / stock.info['bookValue']
    pb_ratio.plot(title=f'{ticker} P/B Ratio Over Time')
    plt.xlabel('Date')
    plt.ylabel('P/B Ratio')
    plt.show()

# Example usage
plot_pb_ratio('AAPL')

### 6) Debt-to-Equity Ratio

def plot_de_ratio(ticker):
    stock = yf.Ticker(ticker)
    de_ratio = stock.info['debtToEquity']
    plt.plot([de_ratio] * len(stock.history(period="2y")), label='D/E Ratio')
    plt.title(f'{ticker} Debt-to-Equity Ratio Over Time')
    plt.xlabel('Date')
    plt.ylabel('D/E Ratio')
    plt.show()

# Example usage
plot_de_ratio('AAPL')

### 7) Current Ratio

def plot_current_ratio(ticker):
    stock = yf.Ticker(ticker)
    current_ratio = stock.info['currentRatio']
    plt.plot([current_ratio] * len(stock.history(period="2y")), label='Current Ratio')
    plt.title(f'{ticker} Current Ratio Over Time')
    plt.xlabel('Date')
    plt.ylabel('Current Ratio')
    plt.show()

# Example usage
plot_current_ratio('AAPL')

### 8) Free Cash Flow (FCF)

def plot_fcf(ticker):
    stock = yf.Ticker(ticker)
    fcf = stock.info['freeCashflow']
    plt.plot([fcf] * len(stock.history(period="2y")), label='Free Cash Flow')
    plt.title(f'{ticker} Free Cash Flow Over Time')
    plt.xlabel('Date')
    plt.ylabel('Free Cash Flow')
    plt.show()

# Example usage
plot_fcf('AAPL')

### 9) Beta

def plot_beta(ticker):
    stock = yf.Ticker(ticker)
    beta = stock.info['beta']
    plt.plot([beta] * len(stock.history(period="2y")), label='Beta')
    plt.title(f'{ticker} Beta Over Time')
    plt.xlabel('Date')
    plt.ylabel('Beta')
    plt.show()

# Example usage
plot_beta('AAPL')

### 10) Market Capitalization

def plot_market_cap(ticker):
    stock = yf.Ticker(ticker)
    market_cap = stock.history(period="2y")['Close'] * stock.info['sharesOutstanding']
    market_cap.plot(title=f'{ticker} Market Capitalization Over Time')
    plt.xlabel('Date')
    plt.ylabel('Market Cap')
    plt.show()

# Example usage
plot_market_cap('AAPL')