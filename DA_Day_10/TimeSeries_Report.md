# Time Series Analysis Report

## Project Overview

This project focuses on analyzing historical stock market data of Reliance Industries using Time Series Analysis techniques.

---

## Dataset Information

Dataset Name: Stock Market Data

Stock Symbol: RELIANCE.NS

Data Source: Yahoo Finance

Features:

- Date
- Open
- High
- Low
- Close
- Volume

---

## Exploratory Analysis

The closing stock prices were analyzed over time to understand long-term market behavior.

Observations:

- Stock prices showed an overall upward trend.
- Short-term fluctuations were observed due to market volatility.
- Volume varied significantly across different periods.

---

## Moving Average Analysis

A 30-Day Moving Average was calculated.

Purpose:

- Smooth short-term fluctuations.
- Identify long-term trends.
- Reduce noise in daily stock prices.

Observation:

The moving average curve followed the general trend of stock prices and provided a clearer picture of market direction.

---

## Stationarity Test

Method Used:

Augmented Dickey-Fuller (ADF) Test

Hypothesis:

- Null Hypothesis (H0): Data is non-stationary.
- Alternative Hypothesis (H1): Data is stationary.

Interpretation:

- p-value < 0.05 → Stationary
- p-value > 0.05 → Non-Stationary

Result:

The stationarity conclusion was determined using the ADF test output.

---

## Seasonal Decomposition

The time series was decomposed into:

### Trend

Represents long-term movement in stock prices.

### Seasonal Component

Represents repeating patterns over time.

### Residual Component

Represents random noise and unexplained variations.

Observation:

Seasonal decomposition helped identify recurring behavior and underlying trends.

---

## Forecasting

Model Used:

ARIMA (AutoRegressive Integrated Moving Average)

Purpose:

To predict future stock prices based on historical observations.

Observation:

The forecasting model generated future price estimates for the selected time horizon.

---

## Key Findings

1. Reliance stock prices exhibited long-term trends.
2. Moving averages successfully reduced noise.
3. Stationarity testing provided insights into data behavior.
4. Seasonal decomposition revealed trend and seasonal effects.
5. ARIMA forecasting produced future stock price estimates.

---

## Conclusion

Time Series Analysis is an effective technique for analyzing stock market behavior. By applying moving averages, stationarity testing, seasonal decomposition, and forecasting models, valuable insights can be extracted from historical stock data and used for future decision-making.
