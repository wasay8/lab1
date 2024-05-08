# import pandas as pd

# data = pd.read_csv("/home/abdulwas/Desktop/abdul_2152268318/scripts/_stock_data_2000_to_2023.csv")

# print(data.shape)

# import pandas as pd

# # Load your stock price data into a DataFrame (assuming you have it in a CSV file)
# data['Date'] = pd.to_datetime(data['Date'])
# data.set_index('Date', inplace=True)
# print(data.head())

# # Define short-term and long-term moving averages
# short_window = 50
# long_window = 200

# # Calculate moving averages
# data['SMA_Short'] = data['Close'].rolling(window=short_window).mean()
# data['SMA_Long'] = data['Close'].rolling(window=long_window).mean()

# # Generate buy and sell signals
# data['Signal'] = 0  # 0 for no signal, 1 for buy, -1 for sell
# data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = 1
# data.loc[data['SMA_Short'] < data['SMA_Long'], 'Signal'] = -1

# # Visualize the buy and sell signals
# import matplotlib.pyplot as plt

# plt.figure(figsize=(12, 6))
# plt.plot(data.index, data['Close'], label='Closing Price', alpha=0.7)
# plt.plot(data.index, data['SMA_Short'], label=f'{short_window}-day SMA', alpha=0.7)
# plt.plot(data.index, data['SMA_Long'], label=f'{long_window}-day SMA', alpha=0.7)
# plt.plot(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['Close'], '^', markersize=10, color='g', label='Buy Signal')
# plt.plot(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['Close'], 'v', markersize=10, color='r', label='Sell Signal')
# plt.title('SMA Crossover Strategy')
# plt.legend()
# plt.show()

# print(data.head())

import pandas as pd
import numpy as np


# data.set_index('date', inplace=True)
def buy_sell_SMA(data):
# Define short-term and long-term moving averages
	short_window = 50
	long_window = 200

	# Calculate moving averages
	data['SMA_Short'] = data['close'].rolling(window=short_window).mean()
	data['SMA_Long'] = data['close'].rolling(window=long_window).mean()

	# Generate buy and sell signals
	data['Signal'] = 0  # 0 for no signal, 1 for buy, -1 for sell
	data.loc[data['SMA_Short'] < data['SMA_Long'], 'Signal'] = 1
	data.loc[data['SMA_Short'] > data['SMA_Long'], 'Signal'] = -1

	# Calculate MSE and RMSE for buy/sell signals
	actual_prices = data['close']
	predicted_prices = data['Signal'] * actual_prices.shift(1)  # Assuming signals are executed the day after
	predicted_prices.fillna(0, inplace=True)  # Fill NaN values with 0 for the first day

	mse = np.mean((actual_prices - predicted_prices) ** 2)
	rmse = np.sqrt(mse)

	print(f'Mean Squared Error (MSE): {mse:.2f}')
	print(f'Root Mean Squared Error (RMSE): {rmse:.2f}')
	return data
# Visualize the buy and sell signals
if __name__ =="__main__":
	import matplotlib.pyplot as plt
	# Load your stock price data into a DataFrame (assuming you have it in a CSV file)
	data = pd.read_csv("Preprocessed_stock_data.csv")
	data['date'] = pd.to_datetime(data['date'])
	data = buy_sell_SMA(data)
	short_window,long_window = 50,200
	plt.figure(figsize=(12, 6))
	plt.plot(data.index, data['close'], label='Closing Price', alpha=0.7)
	plt.plot(data.index, data['SMA_Short'], label=f'{short_window}-day SMA', alpha=0.7)
	plt.plot(data.index, data['SMA_Long'], label=f'{long_window}-day SMA', alpha=0.7)
	plt.plot(data[data['Signal'] == 1].index, data[data['Signal'] == 1]['close'], '^', markersize=10, color='g', label='Buy Signal')
	plt.plot(data[data['Signal'] == -1].index, data[data['Signal'] == -1]['close'], 'v', markersize=10, color='r', label='Sell Signal')
	plt.title('SMA Crossover Strategy')
	plt.legend()
	plt.show()


