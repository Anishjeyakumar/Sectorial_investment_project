import yfinance as yf

def fetch_data(tickers, start, end):
    data = {}
    for ticker in tickers:
        data[ticker] = yf.download(ticker + '.NS', start=start, end=end)
    return data

def fetch_next_year_data(tickers, start_date, end_date):
    next_year_start_date = pd.to_datetime(start_date) + pd.DateOffset(years=1)
    next_year_end_date = pd.to_datetime(end_date) + pd.DateOffset(years=1)
    next_year_data = fetch_data(tickers, next_year_start_date.strftime('%Y-%m-%d'), next_year_end_date.strftime('%Y-%m-%d'))
    return next_year_data
