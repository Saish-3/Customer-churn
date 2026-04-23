from fastapi import FastAPI
import pickle
import os

app = FastAPI()

# Load model
model_path = os.path.join(os.path.dirname(__file__), "../churn_model.pkl")
model = pickle.load(open(model_path, "rb"))

@app.get("/")
def home():
    return {"message": "Customer Churn API is running"}

@app.get("/predict")
def predict():
    data = [[0, 1, 2, 3, 4]]  # dummy input
    result = model.predict(data)
    return {"prediction": result.tolist()}