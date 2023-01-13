import mlflow
import os
import pandas as pd
from fastapi import FastAPI
from schemas import PredictIn, PredictOut
from typing import Optional

os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5001"
os.environ["AWS_ACCESS_KEY_ID"] = "minio"
os.environ["AWS_SECRET_ACCESS_KEY"] = "miniostorage"


def get_model(
    model_name="sk_model",
    model_version: int = 1,
    model_stage: Optional[str] = None,
):
    try:
        if model_stage:
            model_uri = f"models:/{model_name}/{model_version}"
        else:
            model_uri = f"models:/{model_name}/{model_version}"
        model = mlflow.sklearn.load_model(model_uri)
        return model

    except Exception as e:
        print("Error ! : \n", e)
        return None


model = get_model()

app = FastAPI()


@app.post("/predict", response_model=PredictOut)
def predict(data: PredictIn) -> PredictOut:
    global model
    df = pd.DataFrame([data.dict()])
    pred = model.predict(df).item()
    return PredictOut(iris_class=pred)
