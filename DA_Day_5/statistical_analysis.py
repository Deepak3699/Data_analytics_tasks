import pandas as pd
import numpy as np
from scipy import stats

# Load Dataset
df = pd.read_csv("./DA_Day_5/experiment_dataset.csv")

# Separate Groups
group_a = df[df["Group"] == "A"]["Score"]
group_b = df[df["Group"] == "B"]["Score"]

# Mean
mean_a = np.mean(group_a)
mean_b = np.mean(group_b)

# Median
median_a = np.median(group_a)
median_b = np.median(group_b)

# Mode
mode_a = stats.mode(group_a, keepdims=True)
mode_b = stats.mode(group_b, keepdims=True)

# Standard Deviation
std_a = np.std(group_a)
std_b = np.std(group_b)

# Independent T-Test
t_statistic, p_value = stats.ttest_ind(group_a, group_b)

# Print Results
print("=" * 50)
print("STATISTICAL ANALYSIS REPORT")
print("=" * 50)

print("\nGROUP A")
print("Mean:", round(mean_a, 2))
print("Median:", median_a)
print("Mode:", mode_a.mode[0])
print("Standard Deviation:", round(std_a, 2))

print("\nGROUP B")
print("Mean:", round(mean_b, 2))
print("Median:", median_b)
print("Mode:", mode_b.mode[0])
print("Standard Deviation:", round(std_b, 2))

print("\nT-TEST RESULTS")
print("T-Statistic:", round(t_statistic, 4))
print("P-Value:", round(p_value, 6))

if p_value < 0.05:
    print("\nConclusion:")
    print("Statistically Significant Difference Found")
    print("Reject Null Hypothesis")
else:
    print("\nConclusion:")
    print("No Statistically Significant Difference Found")
    print("Fail to Reject Null Hypothesis")

print("=" * 50)