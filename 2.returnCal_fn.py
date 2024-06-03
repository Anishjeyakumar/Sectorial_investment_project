import numpy as np
#contains functions to calculate returns and identify high performing stocks
def calculate_daily_returns(data):
    returns = {}
    for ticker, df in data.items():
        df['Daily Return'] = df['Adj Close'].pct_change()
        returns[ticker] = df['Daily Return']
    return returns

def calculate_cumulative_returns(daily_returns):
    cumulative_returns = {}
    for ticker, returns in daily_returns.items():
        cumulative_returns[ticker] = (1 + returns).cumprod() - 1
    return cumulative_returns

def calculate_mean_cumulative_returns(cumulative_returns):
    mean_cumulative_returns = {}
    for sector, returns in cumulative_returns.items():
        valid_returns = [cr for cr in returns.values() if not cr.empty]
        mean_cumulative_returns[sector] = np.mean([cr.iloc[-1] for cr in valid_returns]) if valid_returns else np.nan
    return mean_cumulative_returns

def identify_top_performing_stocks(cumulative_returns):
    top_performing_stocks = {}
    for sector, returns in cumulative_returns.items():
        valid_returns = {ticker: cr for ticker, cr in returns.items() if not cr.empty}
        sorted_returns = sorted(valid_returns.items(), key=lambda x: x[1].iloc[-1], reverse=True)
        top_performing_stocks[sector] = sorted_returns[:3]
    return top_performing_stocks
