import os
import pickle
from flask import Flask, jsonify

app = Flask(__name__)

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


@app.route("/api")
def predict():
    try:
        # Dummy input
        data = [[0, 1, 2, 3, 4]]

        prediction = model.predict(data)

        return jsonify({
            "prediction": prediction.tolist()
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500