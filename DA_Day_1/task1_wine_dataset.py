from ucimlrepo import fetch_ucirepo

wine_quality = fetch_ucirepo(id=186)

X = wine_quality.data.features
y = wine_quality.data.targets

print("Dataset Shape:")
print(X.shape)

print("\nFirst 5 Rows:")
print(X.head())

print("\nTarget Values:")
print(y.head())

print("\nColumn Names:")
print(X.columns)