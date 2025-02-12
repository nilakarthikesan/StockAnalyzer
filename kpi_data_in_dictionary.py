import yfinance as yf
def get_kpis(ticker):
    stock = yf.Ticker(ticker)
    kpis = {}

    # 1) Price-to-Earnings Ratio (P/E Ratio)
    pe_ratio = stock.history(period="2y")['Close'] / stock.info['trailingEps']
    kpis['PE Ratio'] = pe_ratio.tolist()

    # 2) Earnings Per Share (EPS)
    eps = stock.history(period="2y")['Close'] / stock.info['sharesOutstanding']
    kpis['EPS'] = eps.tolist()

    # 3) Dividend Yield
    dividends = stock.dividends
    dividend_yield = dividends / stock.history(period="2y")['Close']
    kpis['Dividend Yield'] = dividend_yield.tolist()

    # 4) Return on Equity (ROE)
    roe = stock.info['returnOnEquity']
    kpis['ROE'] = [roe] * len(stock.history(period="2y"))

    # 5) Price-to-Book Ratio (P/B Ratio)
    pb_ratio = stock.history(period="2y")['Close'] / stock.info['bookValue']
    kpis['PB Ratio'] = pb_ratio.tolist()

    # 6) Debt-to-Equity Ratio
    de_ratio = stock.info['debtToEquity']
    kpis['Debt-to-Equity Ratio'] = [de_ratio] * len(stock.history(period="2y"))

    # 7) Current Ratio
    current_ratio = stock.info['currentRatio']
    kpis['Current Ratio'] = [current_ratio] * len(stock.history(period="2y"))

    # 8) Free Cash Flow (FCF)
    fcf = stock.info['freeCashflow']
    kpis['Free Cash Flow'] = [fcf] * len(stock.history(period="2y"))

    # 9) Beta
    beta = stock.info['beta']
    kpis['Beta'] = [beta] * len(stock.history(period="2y"))

    # 10) Market Capitalization
    market_cap = stock.history(period="2y")['Close'] * stock.info['sharesOutstanding']
    kpis['Market Capitalization'] = market_cap.tolist()

    return kpis

# Example usage
kpis = get_kpis('AAPL')
print(kpis)
