# Predictive Analytics using Linear Regression

## Project Overview

This project demonstrates the use of **Predictive Analytics** to estimate the **Return on Investment (ROI)** of marketing campaigns using **Linear Regression**. The model is trained on a marketing dataset containing campaign details such as company, campaign type, advertising channel, acquisition cost, clicks, impressions, engagement score, and customer segment.

---

## Objective

To build a machine learning model that predicts the ROI of future marketing campaigns based on historical campaign data.

---

## Dataset

**Dataset Name:** Marketing Dataset

### Features

* Campaign_ID
* Company
* Campaign_Type
* Target_Audience
* Duration
* Channel_Used
* Conversion_Rate
* Acquisition_Cost
* Clicks
* Impressions
* Engagement_Score
* Location
* Language
* Customer_Segment
* Date

### Target Variable

* ROI (Return on Investment)

---

## Tools & Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Jupyter Notebook

---

## Data Preprocessing

The following preprocessing steps were performed:

* Removed "$" and "," from Acquisition_Cost.
* Converted Acquisition_Cost to float.
* Converted Duration from text to integer.
* Extracted Year, Month, and Day from the Date column.
* Encoded categorical variables using One-Hot Encoding.
* Split the dataset into training and testing sets.

---

## Machine Learning Model

**Algorithm Used:** Linear Regression

The model was trained using 80% of the dataset and evaluated on the remaining 20%.

---

## Evaluation Metrics

The model performance was evaluated using:

* RMSE (Root Mean Squared Error)
* MAE (Mean Absolute Error)
* R² Score

---

## Output Files

* predictive_analytics.ipynb
* marketing.csv
* linear_regression_model.pkl
* prediction_report.pdf
* README.md

---

## How to Run

1. Install required libraries

```
pip install pandas numpy scikit-learn joblib
```

2. Open the notebook

```
predictive_analytics.ipynb
```

3. Run all cells.

4. The trained model will be saved as:

```
linear_regression_model.pkl
```

---

## Conclusion

The Linear Regression model successfully predicts the expected ROI of marketing campaigns. Such predictive models help organizations estimate campaign performance, optimize marketing budgets, and make informed business decisions.
