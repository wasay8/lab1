# import pandas as pd
# import numpy as np

# # Load your stock price data into a DataFrame (assuming you have it in a CSV file)
# data = pd.read_csv("/home/abdulwas/Desktop/abdul_2152268318/scripts/_stock_data_2000_to_2023.csv")
# data['Date'] = pd.to_datetime(data['Date'])
# data.set_index('Date', inplace=True)

# # Define the period for RSI calculation
# rsi_period = 14

# # Calculate daily price changes
# data['Price Change'] = data['Close'].diff()

# # Calculate average gains and losses over the period
# data['Gain'] = np.where(data['Price Change'] > 0, data['Price Change'], 0)
# data['Loss'] = np.where(data['Price Change'] < 0, -data['Price Change'], 0)
# data['Avg Gain'] = data['Gain'].rolling(window=rsi_period).mean()
# data['Avg Loss'] = data['Loss'].rolling(window=rsi_period).mean()

# # Calculate RSI
# data['RSI'] = 100 - (100 / (1 + (data['Avg Gain'] / data['Avg Loss'])))

# # Define RSI thresholds for buy and sell signals
# buy_threshold = 30
# sell_threshold = 70

# # Generate buy and sell signals
# data['Signal'] = 0  # 0 for no signal, 1 for buy, -1 for sell
# data.loc[data['RSI'] < buy_threshold, 'Signal'] = 1
# data.loc[data['RSI'] > sell_threshold, 'Signal'] = -1

# # Visualize the buy and sell signals
# import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 6))
# plt.plot(data.index, data['Close'], label='Closing Price', alpha=0.7)
# plt.axhline(y=buy_threshold, color='g', linestyle='--', label=f'Buy Threshold ({buy_threshold})')
# plt.axhline(y=sell_threshold, color='r', linestyle='--', label=f'Sell Threshold ({sell_threshold})')
# plt.plot(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['Close'], '^', markersize=10, color='g', label='Buy Signal')
# plt.plot(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['Close'], 'v', markersize=10, color='r', label='Sell Signal')
# plt.title('RSI Momentum Strategy')
# plt.legend()
# plt.show()
# print(data.head())


import pandas as pd
import numpy as np


# data.set_index('date', inplace=True)
def buy_sell_RSI(data):
	# Define the period for RSI calculation
	rsi_period = 14

	# Calculate daily price changes
	data['Price Change'] = data['close'].diff()

	# Calculate average gains and losses over the period
	data['Gain'] = np.where(data['Price Change'] > 0, data['Price Change'], 0)
	data['Loss'] = np.where(data['Price Change'] < 0, -data['Price Change'], 0)
	data['Avg Gain'] = data['Gain'].rolling(window=rsi_period).mean()
	data['Avg Loss'] = data['Loss'].rolling(window=rsi_period).mean()

	# Calculate RSI
	data['RSI'] = 100 - (100 / (1 + (data['Avg Gain'] / data['Avg Loss'])))

	# Define RSI thresholds for buy and sell signals
	buy_threshold = 30
	sell_threshold = 70

	# Generate buy and sell signals
	data['Signal'] = 0  # 0 for no signal, 1 for buy, -1 for sell
	data.loc[data['RSI'] < buy_threshold, 'Signal'] = 1
	data.loc[data['RSI'] > sell_threshold, 'Signal'] = -1

	# Calculate MSE and RMSE for buy/sell signals
	actual_prices = data['close']
	predicted_prices = data['Signal'] * actual_prices.shift(1)  # Assuming signals are executed the day after
	predicted_prices.fillna(0, inplace=True)  # Fill NaN values with 0 for the first day

	mse = np.mean((actual_prices - predicted_prices) ** 2)
	rmse = np.sqrt(mse)

	print(f'Mean Squared Error (MSE): {mse:.2f}')
	print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
	
	return data

# Load your stock price data into a DataFrame (assuming you have it in a CSV file)
if __name__ =="__main__":
	csv_data = pd.read_csv("Preprocessed_stock_data.csv")
	csv_data = csv_data[csv_data['name']=='FRBK']
	csv_data['date'] = pd.to_datetime(csv_data['date'])
	data, buy_threshold, sell_threshold= buy_sell_RSI(csv_data)
	# Visualize the buy and sell signals
	import matplotlib.pyplot as plt
	buy_threshold = 30
	sell_threshold = 70
	plt.figure(figsize=(12, 6))
	plt.plot(data.index, data['close'], label='Closing Price', alpha=0.7)
	plt.axhline(y=buy_threshold, color='g', linestyle='--', label=f'Buy Threshold ({buy_threshold})')
	plt.axhline(y=sell_threshold, color='r', linestyle='--', label=f'Sell Threshold ({sell_threshold})')
	plt.plot(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['close'], '^', markersize=10, color='g', label='Buy Signal')
	plt.plot(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['close'], 'v', markersize=10, color='r', label='Sell Signal')
	plt.title('RSI Momentum Strategy')
	plt.legend()
	plt.show()
