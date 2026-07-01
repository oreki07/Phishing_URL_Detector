from flask import Flask, render_template, request
import joblib
from feature_extraction import extract_features

app = Flask(__name__)

model = joblib.load("model/phishing_model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    features = [extract_features(url)]

    prediction = model.predict(features)
    probability = model.predict_proba(features)
    confidence = max(probability[0]) * 100

    if prediction[0] == 1:
        result = "⚠️ Phishing Website Detected"
    else:
        result = "✅ Legitimate Website"

    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence, 2),
        url=url
    )

if __name__ == "__main__":
    app.run(debug=True)