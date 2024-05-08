import pandas as pd

data = pd.read_csv("../data/raw_data/stock_data.csv")
print(data.head())
# Handle Missing Values:
miss_val = input("Please choose a type among = (Forward Filling : ffill, Backward Filling : bfill, Interpolate : Linear) ---> ")
print(miss_val)
if miss_val in ["ffill",'bfill']:
    data.fillna(method=miss_val, inplace = True)
    
else:
    data.interpolate(method= miss_val, inplace = True)
    



# Data Time format for Attribute:Date
if data['date'].dtype == 'datetime64[ns]':
    print("The 'date' attribute is already in datetime format.")
else:
    print("The 'date' attribute is not in datetime format.")
    data['date'] = pd.to_datetime(data['date'])
    print("Converted to datetime format")


# Adding Daily Returns as a new attributes
data['daily_returns'] = data['close'].pct_change()
data["daily_returns"].fillna(0, inplace =True)
print(data.head())

# data.to_csv("Preprocessed_stock_data.csv", index= False)

# Calculating Moving Averages:
# df = pd.DataFrame()
data['10_day_MA'] = data['close'].rolling(window=10).mean()
data['50_day_MA'] = data['close'].rolling(window=50).mean()

data.to_csv("Preprocessed_stock_data.csv", index= False)

print(data.head())

#df.reset_index(inplace=True)

# df.to_csv("Moving_Averages_Stock_Price.csv", index = False)

