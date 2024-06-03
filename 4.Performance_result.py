#This code gives the performance results of the 12 stocks if invested the next year of the testing period
#If investment is in  in 2021 ,backtest should be from jan 2020 to dec 2020
import pandas as pd

# enter the backtest year it will provide next year results
start_date = '2020-01-01'
end_date = '2020-12-31'
result_year = '2021' #enter result year

next_year_stock_returns = {}
for stock in top_stocks_bottom_sectors['Stock']:
    next_year_data = fetch_next_year_data([stock], start_date, end_date)
    adj_close_prices = next_year_data[stock]['Adj Close']
    start_price = adj_close_prices.iloc[0]
    end_price = adj_close_prices.iloc[-1]
    returns = ((end_price - start_price) / start_price)*100
    next_year_stock_returns[stock] = returns

#gives returns of the invested stocks 
next_year_returns_df = pd.DataFrame(next_year_stock_returns.items(), columns=['Stock', 'Next Year Returns'])
print(next_year_returns_df)

#T get Total returns obtained in the year 
total_returns = next_year_returns_df['Next Year Returns'].sum()
cum_returns = (total_returns ) / 12

print(f"Return for the year {result_year} is {cum_returns:.2f}%")
