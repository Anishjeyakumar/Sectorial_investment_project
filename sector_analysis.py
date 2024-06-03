#this code gives the performance of all sectors 
#also gives total of 12 stocks (3 high performing stocks from four least performing sector-3*4=12)
import pandas as pd

sector_data = {}
companies = {
    'Commodity': ['ACC', 'DEEPAKNTR', 'AMBUJACEM', 'GRASIM', 'HINDALCO', 'RELIANCE', 'VEDL', 'SHREECEM', 'SRF', 'TATACHEM', 'TATAPOWER', 'TATASTEEL', 'BPCL', 'SAIL', 'HINDPETRO', 'UPL', 'PIIND', 'PIDILITIND', 'JSWSTEEL', 'ONGC', 'NTPC', 'IOC', 'COALINDIA', 'APLAPOLLO', 'ADANIPOWER', 'JINDALSTEL', 'NAVINFLUOR', 'ULTRACEMCO', 'DALBHARAT'],
    'BANK': ['SBIN', 'KOTAKBANK', 'FEDERALBNK', 'HDFCBANK', 'ICICIBANK', 'BANKBARODA', 'INDUSINDBK', 'AXISBANK', 'PNB', 'AUBANK', 'IDFCFIRSTB', 'BANDHANBNK'],
    'Realty': ['SWANENERGY', 'PHOENIXLTD', 'DLF', 'PRESTIGE', 'GODREJPROP', 'MAHLIFE', 'SOBHA', 'BRIGADE', 'OBEROIRLTY'],
    'Metal': ['HINDALCO', 'VEDL', 'TATASTEEL', 'SAIL', 'NATIONALUM', 'HINDZINC', 'RATNAMANI', 'HINDCOPPER', 'ADANIENT', 'JSWSTEEL', 'WELCORP', 'NMDC', 'APLAPOLLO', 'JINDALSTEL', 'JSL'],
    'PSE': ['BPCL', 'BEL', 'SAIL', 'HINDPETRO', 'BHEL', 'OIL', 'POWERGRID', 'ONGC', 'NTPC', 'IOC', 'COALINDIA', 'LICHSGFIN', 'HAL', 'PFC', 'GAIL', 'NHPC', 'CONCOR', 'RECLTD', 'IRCTC'],
    'Energy': ['RELIANCE', 'TATAPOWER', 'BPCL', 'POWERGRID', 'ONGC', 'NTPC', 'IOC', 'COALINDIA', 'ADANIPOWER', 'ADANIGREEN'],
    'Auto': ['ASHOKLEY', 'BALKRISIND', 'BHARATFORG', 'EICHERMOT', 'HEROMOTOCO', 'M&M', 'BOSCHLTD', 'MRF', 'TATAMOTORS', 'MOTHERSON', 'MARUTI', 'TVSMOTOR', 'BAJAJ-AUTO', 'TIINDIA'],
    'FMCG': ['BRITANNIA', 'COLPAL', 'NESTLEIND', 'HINDUNILVR', 'ITC', 'PGHH', 'TATACONSUM', 'RADICO', 'DABUR', 'EMAMILTD', 'MCDOWELL-N', 'MARICO', 'GODREJCP', 'UBL', 'VBL'],
    'Pharma': ['ABBOTINDIA', 'CIPLA', 'GLAXO', 'SANOFI', 'PFIZER', 'DRREDDY', 'LUPIN', 'TORNTPHARM', 'IPCALAB', 'SUNPHARMA', 'AUROPHARMA', 'NATCOPHARM', 'GRANULES', 'BIOCON', 'ALKEM', 'GLENMARK', 'ZYDUSLIFE', 'DIVISLAB', 'LAURUSLABS'],
    'IT': ['WIPRO', 'INFY', 'MPHASIS', 'TCS', 'HCLTECH', 'TECHM', 'LTIM', 'PERSISTENT', 'COFORGE', 'LTTS']
}

#date range to determine the stocks to be taken for investing next year
#to invest in 2017 ,backtest here from jan 2016 to dec 2016
start_date = '2020-01-01'
end_date = '2020-12-31'

for sector, tickers in companies.items():
    sector_data[sector] = fetch_data(tickers, start_date, end_date)

#Daily returns 
sector_daily_returns = {}
for sector, data in sector_data.items():
    sector_daily_returns[sector] = calculate_daily_returns(data)

# cumulative returns
sector_cumulative_returns = {}
for sector, daily_returns in sector_daily_returns.items():
    sector_cumulative_returns[sector] = calculate_cumulative_returns(daily_returns)

# sector wise cumulative return 
mean_cumulative_returns = {}
sector_final_returns = {}
for sector, cumulative_returns in sector_cumulative_returns.items():
    valid_returns = [cr for cr in cumulative_returns.values() if not cr.empty]
    mean_cumulative_returns[sector] = np.mean([cr.iloc[-1] for cr in valid_returns]) if valid_returns else np.nan
    sector_final_returns[sector] = sum([cr.iloc[-1] for cr in valid_returns if not cr.empty]) if valid_returns else np.nan

# Identify top three stocks in each sector
top_performing_stocks = {}
for sector, cumulative_returns in sector_cumulative_returns.items():
    valid_returns = {ticker: cr for ticker, cr in cumulative_returns.items() if not cr.empty}
    sorted_returns = sorted(valid_returns.items(), key=lambda x: x[1].iloc[-1], reverse=True)
    top_performing_stocks[sector] = sorted_returns[:3]


#To get sectorwise cum returns of all sectors    
print("Mean cumulative returns by sector:")
sorted_sectors = sorted(mean_cumulative_returns.items(), key=lambda x: x[1], reverse=False)
for sector, mean_return in sorted_sectors:
    color = '\033[91m' if mean_return in dict(sorted_sectors[:4]).values() else '\033[0m'
    print(f"{color}{sector}: {mean_return:.2f}\033[0m")


#To store top three performing stocks from least performing sectors   
bottom_four_sectors = sorted(mean_cumulative_returns.items(), key=lambda x: x[1])[:4]
top_stocks_bottom_sectors = pd.DataFrame(columns=['Sector', 'Stock', 'Return'])

for sector, _ in bottom_four_sectors:
    for ticker, returns in top_performing_stocks[sector]:
        top_stocks_bottom_sectors = pd.concat([top_stocks_bottom_sectors, pd.DataFrame({
            'Sector': [sector],
            'Stock': [ticker],
            'Return': [returns.iloc[-1]]
        })])
        
print("\nTop three performing stocks in bottom four sectors:")
print(top_stocks_bottom_sectors)
