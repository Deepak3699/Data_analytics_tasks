# Data Cleaning and Preprocessing - Titanic Dataset

## Internship
Data Analytics Internship - Edutech Solution

## Task Objective
The objective of this task is to clean and preprocess the Titanic dataset to make it suitable for further analysis and machine learning applications.

## Dataset Information
- Dataset Name: Titanic Dataset
- Source: Kaggle
- Format: CSV
- Type: Secondary Data

## Tools Used
- Python
- Pandas
- NumPy
- Scikit-learn

## Steps Performed

### 1. Data Loading
The Titanic dataset was loaded into a Pandas DataFrame using the `read_csv()` function.

### 2. Data Inspection
- Viewed first few rows of the dataset.
- Checked dataset structure and data types.
- Generated summary statistics.

### 3. Missing Value Handling
Missing values were identified using:

```python
df.isnull().sum()
```

Actions taken:
- Age column: Missing values replaced with median value.
- Embarked column: Missing values replaced with mode value.
- Cabin column: Ignored or removed due to a large number of missing values.

### 4. Duplicate Check
Duplicate records were checked using:

```python
df.duplicated().sum()
```

No duplicate records were found in the dataset.

### 5. Feature Scaling
Min-Max Scaling was applied to numerical features such as Age and Fare.

Formula:

x' = (x - min) / (max - min)

This transformed values into the range of 0 to 1.

### 6. Outlier Detection
Outliers were detected using the Interquartile Range (IQR) method.

Steps:
- Calculate Q1 and Q3
- Compute IQR = Q3 - Q1
- Determine lower and upper bounds
- Identify values outside the bounds as outliers

### 7. Saving Clean Data
The cleaned dataset was saved as:

```python
clean_titanic.csv
```

## Key Learnings
- Understanding data quality issues.
- Handling missing values effectively.
- Identifying and removing duplicates.
- Applying feature scaling techniques.
- Detecting and handling outliers.
- Preparing data for machine learning models.

## Outcome
Successfully cleaned and preprocessed the Titanic dataset, making it ready for further analysis and machine learning tasks.

## Author
[Deepak]
Data Analytics Intern