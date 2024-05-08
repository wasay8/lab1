import duckdb
import pandas as pd

con = duckdb.connect('stock.db')

preproc_data = pd.read_csv("Preprocessed_stock_data.csv")

con.sql("CREATE TABLE stocks AS SELECT * FROM preproc_data")

# insert into the table "my_table" from the DataFrame "my_df"
con.sql("INSERT INTO stocks SELECT * FROM preproc_data")

con.sql("SELECT * FROM stocks").show()
