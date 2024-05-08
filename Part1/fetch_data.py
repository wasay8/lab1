import yfinance as yf
import pandas as pd
from datetime import datetime
STOCKS = ["DOC.V", "IONQ", "FRBK","YPF","ADBE","BLRX","VLO","VS"]
START_DATE="2023-08-08"
END_DATE="2023-09-08"
def is_valid_date(date_str):
        try:
                datatime.strptime(date_str,"%Y-%mm-%dd")
                return True
        except:
                return False
def is_valid_stock(stock_str):
	ticker = yf.Ticker(stock_str)
	info = None
	try:
		info = ticker.info
		print(f"Stock {stock_str} is valid!")
		return True
	except:
		print(f"Cannot get info of {stock_str}!")
		return False
		
class TicketsDownloader:
  # Download from Yahoo
   def __init__(self,start_date:str,end_date:str,ticker_list:list):
     self.start_date=start_date
     self.end_date=end_date
     self.ticker_list=ticker_list

   def fetch_data(self,proxy=None):
     #fetching data, and reutrn pd.DataFrame 7 columns:A date,open,high,low,close,volume and tick symbol
     res=pd.DataFrame()
     for tic in self.ticker_list:
       tres=yf.download(tic,start=self.start_date,end=self.end_date,proxy=proxy)
       tres['name']=tic
       tres = tres.reset_index()
       res = pd.concat([res,tres],ignore_index=True)
     print("just downloaded：")
     print(res.head(5))

     try:
     #fixing the column name
       res.columns=["date","open","high","low","close","adjcp","volumn","name"]
     except NotImplementedError:
       print("the features are not supported currently")

     res=res.reset_index(drop=True)

     print("after simple processed:")
     print(res.head(5))
     print("Shape of DataFrame: ", res.shape)
     print(res.info())
     return res

if __name__ =="__main__":
	print("Here is your stocks list:",STOCKS)
	print(f"Date range: from {START_DATE} to {END_DATE}\n")
	while True:
		print("There are some options for you, if you are done with your stock selection, press d or D to start the download.")
		print("a) Add a stock to the list")
		print("r) Remove a stock from the list")
		print("c) Change the time range")
		print("i) Information about stocks")
		print("d) Download the stock data")
		print("q) Quit")

		ans = input("Your option?: ")
		if ans == 'A' or ans == 'a':
			stock_name = input("Enter the stock symbol! Please noticed that invalid symbol cannot work in the downloading process: ")
			if is_valid_stock(stock_name):	
				STOCKS.append(stock_name)
			else:
				print("Failed to add a stock!")
		elif ans == 'r' or ans == 'R':
			stock_name = input("Enter the stock symbol that you want to remove: ")
			try:
				STOCK.remove(stock_name)
				print("Successed!")
			except:
				print("Failed!")
		elif ans == 'd' or ans == 'D':
                     	stock_data = TicketsDownloader(START_DATE,END_DATE,STOCKS).fetch_data()
                     	stock_data.to_csv("stock_data.csv",index=False)
                     	break
		elif ans == 'i' or ans == 'I':
		        print("Here is your stocks list:",STOCKS)
		        print(f"Data range: from {START_DATE} to {END_DATE}\n")
		        print("")
		elif ans == 'q' or ans == 'Q':
			print("Thank you very much!")
			break
		elif ans == 'c' or ans == 'C':
		        t_START_DATE = input(f"Enter the New Start Date ({START_DATE}): ")
		        t_END_DATE = input(f"Enter the New End Date ({END_DATE}): ")
		        if is_valid_date(t_START_DATE) and is_valid_date(t_END_DATE):
		                START_DATE = t_START_DATE
		                END_DATE = t_END_DATE
		                print("Successed!")
		        else:
		                print("Invalid answer! Please try another options!")
		else:
			print("Invalid answer! Please enter your option again!")




