import json
import pickle
import os

model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")
model = pickle.load(open(model_path, "rb"))

def handler(request):
    if request.method == "GET":
        return {
            "statusCode": 200,
            "body": json.dumps({"message": "API working"})
        }

    if request.method == "POST":
        data = json.loads(request.body)
        prediction = model.predict([data["input"]])

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": prediction.tolist()})
        }