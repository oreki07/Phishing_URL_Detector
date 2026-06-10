# Phishing URL Detection Using Machine Learning

A Machine Learning-based web application that analyzes URLs and predicts whether they are **Legitimate** or **Phishing**. The project uses a Random Forest Classifier trained on URL-based features and provides predictions through a Flask web interface.

---

## Project Overview

Phishing attacks are one of the most common cyber threats used to steal user credentials, banking information, and personal data through fake websites.

This project aims to identify potentially malicious URLs using Machine Learning. The application extracts URL features, passes them to a trained model, and displays the prediction along with a confidence score.

---

##  Objectives

- Detect phishing websites based on URL characteristics.
- Train a Machine Learning model on phishing URL data.
- Build a user-friendly web interface using Flask.
- Display prediction confidence to users.
- Demonstrate the application of Machine Learning in Cyber Security.

---

## 🛠 Technologies Used

### Programming Language
- Python 3

### Machine Learning
- Scikit-Learn
- Random Forest Classifier

### Data Processing
- Pandas
- NumPy

### Model Persistence
- Joblib

### Web Development
- Flask
- HTML

---

##  Project Structure

```text
Phishing_URL_Detector/
│
├── dataset/
│   └── phishing_url_dataset.csv
│
├── model/
│   └── phishing_model.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── train.py
├── feature_extraction.py
├── check_dataset.py
├── check_target.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

##  Working Principle

### Step 1: Dataset Loading

The phishing URL dataset is loaded using Pandas.

### Step 2: Data Preparation

The dataset is divided into:

- Features (X)
- Target Labels (y)

Where:

- `0` = Legitimate URL
- `1` = Phishing URL

### Step 3: Model Training

A Random Forest Classifier is trained using:

- 80% Training Data
- 20% Testing Data

### Step 4: Model Evaluation

The trained model is evaluated on unseen test data.

**Achieved Accuracy:**

```text
91.57%
```

### Step 5: Model Saving

The trained model is saved as:

```text
model/phishing_model.pkl
```

using Joblib.

### Step 6: URL Analysis

When a user enters a URL:

- Features are extracted
- The ML model predicts whether the URL is phishing or legitimate
- Confidence score is displayed

---

##  Features Used for Detection

The model uses the following URL features:

| Feature | Description |
|----------|-------------|
| url_length | Total URL length |
| valid_url | Checks URL format |
| at_symbol | Number of @ symbols |
| sensitive_words_count | Sensitive keywords count |
| path_length | Length of URL path |
| isHttps | HTTPS usage |
| nb_dots | Number of dots |
| nb_hyphens | Number of hyphens |
| nb_and | Number of & symbols |
| nb_or | Number of "or" occurrences |
| nb_www | Number of www occurrences |
| nb_com | Number of .com occurrences |
| nb_underscore | Number of underscores |

---

##  Machine Learning Algorithm

### Random Forest Classifier

Random Forest was selected because:

- High accuracy
- Handles multiple features efficiently
- Resistant to overfitting
- Suitable for classification problems

---

##  Running the Project

### 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Phishing-URL-Detection-ML.git
```

### 2. Move into Project Directory

```bash
cd Phishing-URL-Detection-ML
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Model

```bash
python train.py
```

### 5. Run the Flask Application

```bash
python app.py
```

### 6. Open Browser

```text
http://127.0.0.1:5000
```

---

##  Application Workflow

```text
User Input URL
       │
       ▼
Feature Extraction
       │
       ▼
Random Forest Model
       │
       ▼
Prediction
       │
       ▼
Confidence Score
       │
       ▼
Display Result
```

---

##  Dataset Information

- Total Records: 2488
- Features: 13
- Target Classes:
  - Legitimate URLs: 1313
  - Phishing URLs: 1175

The dataset is relatively balanced, making it suitable for binary classification.

---

##  Limitations

Current version does not:

- Verify domain ownership
- Check SSL certificate validity
- Query WHOIS information
- Use blacklist databases
- Detect all typo-squatting domains

Example:

```text
google.com      → Legitimate
googel.com      → May still be classified as Legitimate
```

because the model relies on URL features rather than domain reputation.

---

##  Future Enhancements

- Domain reputation analysis
- WHOIS lookup integration
- SSL certificate validation
- Real-time phishing detection
- Advanced NLP-based URL classification
- Modern Bootstrap UI
- Deployment on cloud platforms

---

## Academic Relevance

This project demonstrates concepts from:

- Cyber Security
- Machine Learning
- Data Analytics
- Web Application Development
- Network Security

---

##  Author

**Uttkarsh Tiwari**

Cyber Security Student

---

##  License

This project is developed for educational and academic purposes.