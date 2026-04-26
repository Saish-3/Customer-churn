import os
import pickle
from flask import Flask, jsonify

app = Flask(__name__)

try:
    model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")

    with open(model_path, "rb") as f:
        model = pickle.load(f)

except Exception as e:
    model = None
    load_error = str(e)


@app.route("/api")
def predict():
    try:
        if model is None:
            return jsonify({
                "model_load_error": load_error
            }), 500

        # Correct sklearn input shape
        data = [[0, 1, 2, 3, 4]]

        prediction = model.predict(data)

        return jsonify({
            "prediction": prediction.tolist()
        })

    except Exception as e:
        return jsonify({
            "runtime_error": str(e)
        }), 500