import os
import pickle
import json

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def handler(request):
    try:
        # Dummy input
        data = [[0, 1, 2, 3, 4]]

        prediction = model.predict(data)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "prediction": prediction.tolist()
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }