import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

# Load Dataset
df = pd.read_csv("./DA_Day_6/Dataset/Housing.csv")

print("Original Dataset Shape:")
print(df.shape)

# -------------------------
# One-Hot Encoding
# -------------------------

categorical_columns = df.select_dtypes(include=["object"]).columns

df_encoded = pd.get_dummies(
    df,
    columns=categorical_columns,
    drop_first=True
)

print("\nAfter One-Hot Encoding:")
print(df_encoded.shape)

# -------------------------
# Feature Scaling
# -------------------------

numerical_columns = df_encoded.select_dtypes(include=["int64", "float64"]).columns

scaler = StandardScaler()

df_encoded[numerical_columns] = scaler.fit_transform(
    df_encoded[numerical_columns]
)

# -------------------------
# Interaction Feature
# -------------------------

if "area" in df.columns and "bedrooms" in df.columns:

    df_encoded["area_bedrooms_interaction"] = (
        df["area"] * df["bedrooms"]
    )
# folder = "Encoded"
# os.makedirs(folder,exist_ok=True)
# # Save Engineered Dataset

df_encoded.to_csv("Engineered_Housing_Dataset.csv",
    index=False)

print("\nFeature Engineering Complete!")
print("File Saved: Engineered_Housing_Dataset.csv")