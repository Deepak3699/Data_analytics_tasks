# Data Transformation and Feature Engineering Report

## Project Title

Feature Engineering on Housing Dataset

## Objective

The objective of this project is to transform raw housing data into a format suitable for machine learning models through feature engineering techniques.

## Tools Used

* Python
* Pandas
* Scikit-learn

## Dataset

Housing Prices Dataset

The dataset contains numerical and categorical attributes related to house prices.

## Feature Engineering Techniques

### One-Hot Encoding

Categorical variables were converted into numerical format using one-hot encoding.

Purpose:

* Machine learning models require numerical inputs.
* Prevents incorrect ordinal relationships.

### Feature Scaling

Numerical variables were standardized using StandardScaler.

Purpose:

* Places features on a similar scale.
* Improves model performance.

### Interaction Features

A new feature was created by multiplying area and bedrooms.

Feature Name:

area_bedrooms_interaction

Purpose:

* Capture relationships between existing variables.

## Output

An engineered dataset was generated containing:

* Encoded categorical features
* Scaled numerical features
* New interaction features

## Conclusion

Feature engineering improved dataset quality and prepared the data for machine learning algorithms by making features more informative and model-friendly.
