import pandas as pd

data = pd.read_csv("dataset/phishing_url_dataset.csv")

print(data.head())
print("\nColumns:")
print(data.columns)
print("\nShape:")
print(data.shape)