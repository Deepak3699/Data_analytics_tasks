# Task 10: Time Series Data Analysis

## Objective

The objective of this task is to analyze stock market data using Time Series Analysis (TSA) techniques. The analysis includes trend identification, stationarity testing, moving averages, seasonal decomposition, and forecasting.

---

## Tools Used

- Python
- Pandas
- NumPy
- Matplotlib
- Statsmodels

---

## Dataset

Dataset Name: Stock Market Data

File: stock_market_data.csv

Source: Yahoo Finance (RELIANCE.NS Historical Data)

---

## Analysis Performed

### 1. Data Loading
Loaded stock market data using Pandas.

### 2. Data Preprocessing
- Converted Date column to datetime format.
- Set Date as index.
- Checked for missing values.

### 3. Exploratory Analysis
- Summary statistics.
- Closing price trend visualization.

### 4. Moving Average Analysis
Calculated 30-day Moving Average to smooth short-term fluctuations.

### 5. Stationarity Test
Performed Augmented Dickey-Fuller (ADF) Test to determine whether the time series is stationary.

### 6. Seasonal Decomposition
Separated the stock price series into:
- Trend
- Seasonality
- Residual Components

### 7. Forecasting
Implemented ARIMA model to forecast future stock prices.

---

## Deliverables

- TSA_Notebook.ipynb
- stock_market_data.csv
- Forecasting Plot
- Seasonal Decomposition Plot
- Moving Average Plot
- TimeSeries_Report.md

---

## Learning Outcomes

After completing this task:

- Understood Time Series Data.
- Learned Moving Average techniques.
- Performed Stationarity Testing.
- Identified Seasonal Components.
- Applied Forecasting Models.
- Interpreted stock market trends.

---

## Interview Questions

### What is Stationarity?

A stationary time series has constant statistical properties such as mean, variance, and autocorrelation over time.

### What is Seasonal Decomposition?

Seasonal decomposition separates a time series into trend, seasonality, and residual components to better understand underlying patterns.
