from statsmodels.tsa.stattools import adfuller

# 1. Run the Augmented Dickey-Fuller (ADF) test on the Close prices
print("--- Running ADF Test on Original Close Price ---")
result = adfuller(df_close['Close'])

print(f'ADF Statistic: {result[0]:.4f}')
print(f'p-value: {result[1]:.4f}')
print('Critical Values:')
for key, value in result[4].items():
    print(f'\t{key}: {value:.4f}')

# Interpret the p-value
if result[1] <= 0.05:
    print("\nResult: Reject the Null Hypothesis. The data IS stationary.")
else:
    print("\nResult: Fail to reject the Null Hypothesis. The data IS NOT stationary.")