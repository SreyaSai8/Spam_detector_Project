

```markdown
# 🧠 Spam Detector API

A **production-grade**, containerized **REST API** to classify text as **spam** or **not_spam**, powered by **scikit-learn**, **Flask**, and **TF-IDF + Naive Bayes**. Trained on **India-specific** spam data and built to work fully **offline**.

---

## 🚀 Features

- ✅ Lightweight, fast API using **Flask**
- 🧠 Spam classification using **TF-IDF + Naive Bayes**
- 📦 Fully **Dockerized** for cross-platform deployment
- 🔌 Accepts **JSON** input, returns **label + confidence**
- ⚙️ Configurable via `config.json`
- 🩺 `/health` and `/version` endpoints
- 🔐 Compliant with `schema.json`
- 📊 Optionally logs predictions

---

## 📁 Project Structure

```

spam-detector/
├── app/
│   ├── main.py               # Flask API entry point
│   └── model/
│       ├── spam\_Navie.joblib         # Trained classifier
│       └── tfidf\_vectorizer.joblib   # TF-IDF vectorizer
├── config.json               # Runtime settings
├── schema.json               # Input validation schema
├── data/
│   └── dataset.json          # India-specific spam dataset
├── Dockerfile                # Docker image definition
├── requirements.txt          # Python dependencies
├── README.md                 # Project documentation
└── tests/
└── test\_predict.py       # Unit tests

````

---

## ⚙️ `config.json` (Required)

Example runtime configuration:

```json
{
  "model_name": "spam_Navie",
  "version": "1.0.0",
  "confidence_threshold": 0.6,
  "labels": ["spam", "not_spam"],
  "log_predictions": true
}
````

---

## 🐳 Docker Deployment Guide

### Step 1: Build the Docker image

```bash
docker build -t spam-detector .
```

### Step 2: Run the container on port 8000

```bash
docker run -p 8000:8000 spam-detector
```

> 🟢 The API will be accessible at: `http://localhost:8000`

---

## 🔮 How to Predict

### ✅ Endpoint

`POST /predict`
Send a JSON body with a `"post"` field containing the text to classify.

### 📦 Request Format

```json
{
  "post": "Win a free trip to Goa! Click here to claim your prize!"
}
```

### 🔁 Response Format

```json
{
  "label": "spam",
  "confidence": 0.93
}
```

---

## 🧪 Test with Postman

1. Open Postman → `New Request`
2. Method: `POST`
3. URL: `http://localhost:8000/predict`
4. Headers: `Content-Type: application/json`
5. Body → `raw` → JSON:

```json
{
  "post": "This is a limited time offer just for you!"
}
```

6. Click **Send**.

---

## 💻 Test with `curl`

```bash
curl -X POST http://localhost:8000/predict \
     -H "Content-Type: application/json" \
     -d '{"post": "This is a limited time offer just for you!"}'
```

---

## 🔍 Other API Endpoints

| Endpoint   | Method | Description               |
| ---------- | ------ | ------------------------- |
| `/predict` | POST   | Predict spam or not\_spam |
| `/health`  | GET    | Check API health          |
| `/version` | GET    | Returns model info        |

---

## 🧪 Running Tests

```bash
python -m unittest tests/test_predict.py
```

---


## 🙋‍♀️ Author

**S. Sreya Sai** — Computer Science & AI/ML Enthusiast

