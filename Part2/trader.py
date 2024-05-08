import pandas as pd
import numpy as np
import duckdb
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from buy_sell_RSI import buy_sell_RSI
from buy_sell_SMA import buy_sell_SMA
import argparse
class Trader:
	def __init__(self,fund,method):
		self.fund = fund
		self.method = method
		self.stock_names = []
		self.invest_data = pd.DataFrame()
		self.num_stock = defaultdict(int)
		self.stock_price = defaultdict(int)
		self.history = pd.DataFrame(columns=["date","total_pos"])
		self.buy_th = None
		self.sell_th = None
	def loading_stock_information(self,init_data):
		# init_data = pd.read_csv(address)
		self.stock_names = init_data['name'].unique()
		for name in self.stock_names:
			p_init_data = init_data[init_data['name']==name].copy()
			# Choosing the analysis strategy
			if self.method == "RSI":
				strategy = buy_sell_RSI
			elif self.method == "SMA":
				strategy = buy_sell_SMA
			tres = strategy(p_init_data)
			self.invest_data = pd.concat([self.invest_data,tres],ignore_index=True)
		print("Trading information import successfully!")
		print(self.invest_data.head(20))
		print(self.invest_data.info())
	
	def _buy_and_sell(self,trading_record):
		# Update the price of stock
		for iter,record in trading_record.iterrows():
			self.stock_price[record['name']] = record['close']
		useful_record = trading_record[trading_record["Signal"]!=0]
		
		for iter,record in useful_record.iterrows():
			if record["Signal"] == -1:
				rate = 4
				stock_num = self.fund*rate/100//record['close'] # buying rate = 4
				self.num_stock[record['name']]+=stock_num
				self.fund-=stock_num*record['close']
			else:
				rate = 90
				stock_num = self.num_stock[record['name']]*rate//100 # selling rate = 90
				self.fund+=stock_num*record['close']
				self.num_stock[record['name']]-=stock_num 
			
		return
	
	def auto_trading(self):
		start_fund = self.fund
		str_start_date = self.invest_data['date'].min()
		str_end_date = self.invest_data['date'].max()
		start_date = datetime.strptime(str_start_date,"%Y-%m-%d")
		end_date = datetime.strptime(str_end_date,"%Y-%m-%d")
		for i in range((end_date-start_date).days+1):
			current_date = start_date+timedelta(days=i)
			str_current_date = current_date.strftime("%Y-%m-%d")
			self._buy_and_sell(self.invest_data[self.invest_data['date']==str_current_date])
			
			# Calculate the total Pos
			value = self.fund
			for key in self.num_stock:
				t_total_value =  self.num_stock[key]*self.stock_price[key]
				value+=t_total_value
			t_history = pd.DataFrame([[str_current_date,value]],columns=["date","total_pos"])
			self.history = pd.concat([self.history, t_history],ignore_index=True)
		
		print("Cash:",self.fund)
		print("Current Stocks:")
		value = self.fund
		for key in self.num_stock:
			t_total_value =  self.num_stock[key]*self.stock_price[key]
			value+=t_total_value
			print(f"name: {key}, num: {self.num_stock[key]}, total_value: {t_total_value}")
		
		# Caluate the metrics
		print(f"portfolio_value: {value}")
		annualized_returns_rate = pow((1+(value-start_fund)/start_fund),365/(end_date-start_date).days)-1
		print(f"annualized returns: {annualized_returns_rate}")
		self.history['daily return'] = self.history['total_pos'].pct_change()
		SR = (annualized_returns_rate-0.04)/self.history['daily return'].std()
		print(f"Sharpe Ratio: {SR}")
		
if __name__ =="__main__":
	# input_add = "Preprocessed_stock_data.csv"
	con = duckdb.connect('stock.db')
	init_data = con.sql("SELECT * FROM stocks").df()
	
	# arguments initailization
	parser = argparse.ArgumentParser()
	parser.add_argument('--fund',type=float,default=50000)
	parser.add_argument('--method',type=str, default='RSI',choices=['SMA','RSI'])
	
	# Create a trader
	args = parser.parse_args()
	trader = Trader(args.fund,args.method)
	#trader.loading_stock_information(input_add)
	trader.loading_stock_information(init_data)
	trader.auto_trading()
