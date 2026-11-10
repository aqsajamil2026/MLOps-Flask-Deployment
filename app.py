from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return jsonify({"status": "ok", "message": "Flask ML app is running"})

@app.get("/predict")
def predict():
    # Demo prediction endpoint; replace with the trained model in the real project.
    return jsonify({"prediction": 0, "model_version": "demo-1"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
