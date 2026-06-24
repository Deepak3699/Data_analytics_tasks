


import yfinance as yf
import pandas as pd

# Define the stock ticker and the time window you want to analyze
ticker = "RELIANCE.NS" 
start_date = "2021-01-01"
end_date = "2026-01-01" # Fetches data up to this point

# Fetch the historical data
print(f"Fetching data for {ticker}...")
df = yf.download(ticker, start=start_date, end=end_date)

# Preview the data
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Save it to a CSV file so you have a physical copy for your task deliverables
df.to_csv("stock_market_data.csv")
print("\nDataset successfully downloaded and saved as 'stock_market_data.csv'!")