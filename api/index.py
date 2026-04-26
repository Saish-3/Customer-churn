import os
import pickle
import json

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")
model = pickle.load(open(model_path, "rb"))

def handler(request):
    try:
        # Example dummy input
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