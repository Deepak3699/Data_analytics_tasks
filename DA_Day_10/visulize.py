import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
# Note: index_col=0 sets the Date as the index, and parse_dates=True converts it to datetime format
df = pd.read_csv("./stock_market_data.csv", index_col=0, parse_dates=True)

# Clean column multi-index if yfinance created one
if isinstance(df.columns, pd.MultiIndex):
    df.columns = df.columns.get_level_values(0)

# We will use 'Close' price for our analysis
df_close = df[['Close']].dropna()

# 2. Calculate Moving Averages (MA)
# 20-day Short Term Moving Average
df_close['MA20'] = df_close['Close'].rolling(window=20).mean()
# 50-day Long Term Moving Average
df_close['MA50'] = df_close['Close'].rolling(window=50).mean()

# 3. Plot the Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(df_close['Close'], label='Original Close Price', color='blue', alpha=0.5)
plt.plot(df_close['MA20'], label='20-Day Moving Average', color='red', linestyle='--')
plt.plot(df_close['MA50'], label='50-Day Moving Average', color='green', linestyle='-')

plt.title('Stock Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()