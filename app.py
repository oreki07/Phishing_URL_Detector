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
    if not url:
        return render_template(
            "index.html",
            prediction="Please enter a URL", confidence=0, url="",status="warning")
        

    features = [extract_features(url)]

    prediction = model.predict(features)
    probability = model.predict_proba(features)
    confidence = round(max(probability[0]) * 100,2)

    if prediction[0] == 1:
        result = "⚠️ Phishing Website Detected"
        status="danger"
    else:
        result = "✅ Legitimate Website"
        status="safe"

    return render_template(
        "index.html",
        prediction=result,
        confidence=round(confidence, 2),
        url=url,
        status=status
    )

if __name__ == "__main__":
    app.run(debug=True)