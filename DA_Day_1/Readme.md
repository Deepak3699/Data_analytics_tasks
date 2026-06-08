# Task 1: Data Collection & Data Source Identification

## Intern Details
Name: Deepak
Internship: Data Analytics Internship

## Objective
The objective of this task is to identify a reliable data source, collect data, and understand different types of data sources used in analytics projects.

---

## Dataset Information

Dataset Name: Wine Quality Dataset

Source:
UCI Machine Learning Repository

Dataset ID:
186

Description:
The Wine Quality Dataset contains physicochemical properties of red and white Portuguese wines and their quality ratings.

---

## Data Source Type

Secondary Data

Reason:
The dataset was previously collected and published by researchers and is publicly available through the UCI Machine Learning Repository.

---

## Tools Used

- Python
- Pandas
- UCI ML Repository API
- VS Code

---

## Data Collection Method

The dataset was collected using the Python package:

```python
from ucimlrepo import fetch_ucirepo
wine_quality = fetch_ucirepo(id=186)
```

## paper link 

https://www.semanticscholar.org/paper/Modeling-wine-preferences-by-data-mining-from-Cortez-Cerdeira/bf15a0ccc14ac1deb5cea570c870389c16be019c

## Files Included
task1_wine_dataset.py
Data_Source_Report.pdf
wine_quality_dataset.py
Dataset CSV Files
Screenshots

## Learning Outcome

Understanding Primary and Secondary Data
Identifying reliable data sources
Downloading datasets from UCI Repository
Loading datasets using Python
Exploring dataset structure

