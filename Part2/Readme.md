# Algorithm Development
Python: 3.11.4  
Pandas: 2.0.3 
Numpy: 1.24.3
Matplotlib: 0.1.9

### Algorithm Used :

#### SMA: Simple Moving Average
Execute : buy_sell_SMA.py

1. Moving averages provide a simplified view of data trends by calculating the mean of a specified number of recent data points, helping to reduce noise and highlight underlying patterns.

2. They are commonly used in finance to analyze stock prices (e.g., 50-day or 200-day moving averages) and in various fields to track trends in data over time, such as weather, sales, or website traffic.

3. Different types of moving averages, like simple moving averages (SMA) and exponential moving averages (EMA), offer varying levels of responsiveness to recent data, making them versatile tools for trend analysis and forecasting.

![Screenshot 2023-09-16 at 12 58 40 PM](https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/b153a53a-2727-47a2-8e3d-201c35550eb9)


![Screenshot 2023-09-16 at 12 58 56 PM](https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/daa8b373-6d9e-41e7-b022-714509c35640)



#### RSI : Relative Strength Index
Execute : buy_sell_RSI.py

RSI measures the speed and magnitude of recent price changes, indicating whether an asset is overbought (above 70) or oversold (below 30). Traders use it to identify potential trend reversals or confirm existing trends.

When RSI is high, it suggests that the asset may be overextended, and a price correction or reversal may be imminent. Conversely, a low RSI value may indicate that the asset is oversold, potentially signaling a buying opportunity.

RSI is a valuable tool for traders and investors to make informed decisions about entry and exit points in the market based on the current strength of an asset's price movements.


![Screenshot 2023-09-16 at 12 59 25 PM](https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/8d7140fb-3507-4ae5-9c27-a58f1edb15ce)


![Screenshot 2023-09-16 at 12 59 45 PM](https://github.com/thoughtfuldata/DSCI560-project/assets/48021329/82c7ee4b-7f08-4b4a-b57d-3fb6ed41fa76)



## Trading Environment

There are two method to predict the trend of stock in the procject -- Relative Strength Index (RSI) and Simple Moving Average (SMA)

First run to_db.py to create a database
>python3 to_db.py

To run the trading environment, please run the commend:
> python3 trader.py

To fix the initial fund and prediction method, please run like:
> python3 trader.py --fund 50000 --method SMA

The result should look like:

![image](https://github.com/thoughtfuldata/DSCI560-project/assets/55038803/7706218b-be68-4ad2-972e-c8566420c855)
