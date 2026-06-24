import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset cleanly
# skiprows=[1] removes the 'Ticker / RELIANCE.NS' row completely
df = pd.read_csv("./stock_market_data.csv", skiprows=[1], index_col=0, parse_dates=True)

# Clean up column names just in case there are hidden spaces
df.columns = df.columns.str.strip()

# 2. Extract and convert the 'Close' price to numbers
df_close = pd.DataFrame(index=df.index)
df_close['Close'] = pd.to_numeric(df['Close'], errors='coerce')
df_close = df_close.dropna()

# 3. Calculate Moving Averages (MA)
df_close['MA20'] = df_close['Close'].rolling(window=20).mean()
df_close['MA50'] = df_close['Close'].rolling(window=50).mean()

# 4. Plot the Moving Averages
plt.figure(figsize=(12, 6))
plt.plot(df_close['Close'], label='Reliance Close Price', color='blue', alpha=0.5)
plt.plot(df_close['MA20'], label='20-Day Moving Average', color='red', linestyle='--')
plt.plot(df_close['MA50'], label='50-Day Moving Average', color='green', linestyle='-')

plt.title('Reliance Industries (RELIANCE.NS) - Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price (INR)')
plt.legend()
plt.grid(True)
plt.show()