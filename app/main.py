from flask import Flask, request, jsonify
import joblib
import json
import sys

# Load and validate config.json
try:
    with open("config.json", "r") as f:
        config = json.load(f)

    REQUIRED_KEYS = {"model_name", "version", "confidence_threshold", "labels", "log_predictions"}
    if not REQUIRED_KEYS.issubset(config):
        raise ValueError("Missing keys in config.json")
except Exception as e:
    print(f"Failed to load config.json: {e}")
    sys.exit(1)

# Load model and vectorizer
try:
    model = joblib.load(f"app/model/{config['model_name']}.joblib")
    vectorizer = joblib.load("app/model/tfidf_vectorizer.joblib")
except Exception as e:
    print(f"Failed to load model/vectorizer: {e}")
    sys.exit(1)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if not request.is_json:
        return jsonify({"error": "Invalid input, JSON expected"}), 400

    data = request.get_json()
    if "post" not in data:
        return jsonify({"error": "'post' field is required"}), 400

    text = data["post"]
    vec = vectorizer.transform([text])
    confidence = model.predict_proba(vec)[0][1]
    label = config["labels"][0] if confidence >= config["confidence_threshold"] else config["labels"][1]

    if config["log_predictions"]:
        print(f"Post: {text}")
        print(f"Prediction: {label} (Confidence: {confidence:.2f})")

    return jsonify({
        "label": label,
        "confidence": round(float(confidence), 2)
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        "model_name": config["model_name"],
        "version": config["version"],
        "threshold": config["confidence_threshold"]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
  # <-- Required for Docker to expose it
