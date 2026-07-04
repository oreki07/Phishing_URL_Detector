from flask import Flask, render_template, request
import joblib
from feature_extraction import extract_features
from domain_checker import check_domain

app = Flask(__name__)

model = joblib.load("model/phishing_model.pkl")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    url = request.form['url']

    # Check if domain exists
    domain_info = check_domain(url)

    # Domain definitely not registered
    if domain_info["exists"] is False:
        return render_template(
            "index.html",
            prediction="❌ Domain is NOT Registered",
            confidence=0,
            url=url,
            domain_info=domain_info,
            recommendation="This domain is not registered. Avoid visiting it.",
            status="warning"
        )

    # WHOIS lookup failed
    if domain_info["exists"] is None:
        return render_template(
            "index.html",
            prediction="⚠️ Unable to Verify Domain",
            confidence=0,
            url=url,
            domain_info=domain_info,
            recommendation="The WHOIS lookup failed. This does NOT necessarily mean the domain is fake.",
            status="warning"
        )

    # Extract features
    features = extract_features(url)

    # ML Prediction
    prediction = model.predict([features])
    probability = model.predict_proba([features])

    confidence = round(max(probability[0]) * 100, 2)

    if prediction[0] == 1:
        result = "⚠️ Phishing Website Detected"
        recommendation = "Avoid visiting this website."
        status = "danger"
    else:
        result = "✅ Legitimate Website"
        recommendation = "This domain appears safe according to the machine learning model."
        status = "safe"

    return render_template(
        "index.html",
        prediction=result,
        confidence=confidence,
        url=url,
        domain_info=domain_info,
        recommendation=recommendation,
        status=status
    )
    


if __name__ == "__main__":
    app.run(debug=True)