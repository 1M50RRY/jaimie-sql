from flask import Flask, request, jsonify
import inference

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    return jsonify(inference.predict(request))

@app.route("/health", methods=["GET"])
def health():
    return jsonify(inference.health(request))
