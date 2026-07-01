import pandas as pd

data = pd.read_csv("dataset/phishing_url_dataset.csv")

print(data["target"].value_counts())