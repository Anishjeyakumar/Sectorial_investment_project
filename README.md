# Portfolio Management:Dynamic sector allocation based on performance-Using Python 

## Overview:


This project is designed to provide a comprehensive analysis of historical stock data to support informed investment decisions. By leveraging historical market data, the project aims to identify trends, assess sector performance, and select top-performing stocks for potential investment opportunities. The project encompasses data collection, return calculation, sector analysis, top-performing stock selection, and future return projections.

## Features:

## Data Collection:

The project utilizes the Yahoo Finance API (yfinance) to fetch historical stock data for a predefined list of stock tickers. This data includes information such as opening price, closing price, high price, low price, and volume traded, among others. Data is collected for a specified time range, allowing for historical analysis.

## Return Calculation:

Daily returns and cumulative returns are calculated for each stock based on the fetched historical data. Daily returns represent the percentage change in a stock's price from one day to the next, while cumulative returns provide insights into the overall performance of a stock over the specified time period.

## Sector Analysis:

Stocks are organized into predefined sectors based on industry classifications or user-defined categories. Mean cumulative returns are calculated for each sector, providing an overview of the historical performance of stocks within that sector. This analysis helps investors identify sectors with higher historical returns and potential growth opportunities.

## Top-Performing Stocks Selection:

Within each sector, top-performing stocks are identified based on their cumulative returns. The project focuses on stocks within sectors that have historically underperformed, aiming to uncover potential growth opportunities within overlooked sectors. This approach allows investors to capitalize on trends and identify promising investment opportunities.

## Future Performance Projection:

Future returns are projected for the next year based on historical data and performance trends. By analyzing historical performance and identifying patterns, the project aims to forecast potential returns for individual stocks and sectors. This projection aids investors in making informed decisions about future investments and portfolio allocations.

## Libraries required

Pandas 
```bash
pip install pandas
```
Numpy
```bash
pip install Numpy
```
Yfinance - To fetch historial data of stocks
```bash
pip install Yfinance
```


