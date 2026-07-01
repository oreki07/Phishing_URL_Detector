import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("dataset/phishing_url_dataset.csv")

# Features
X = data.drop("target", axis=1)

# Labels
y = data["target"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)

print(f"Accuracy: {accuracy*100:.2f}%")

# Save model
joblib.dump(model, "model/phishing_model.pkl")

print("Model saved successfully!")