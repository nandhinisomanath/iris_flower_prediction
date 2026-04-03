from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import pandas as pd
import joblib

model = joblib.load('../notebooks/iris_classifier.pkl')
scaler = joblib.load('../notebooks/iris_scaler.pkl')
class_names = joblib.load('../notebooks/class_names.pkl')

print(class_names)

app = FastAPI(title='Iris Classifier')


class irisInput(BaseModel):
    sepal_length: float = Field(..., alias="sepal length (cm)", gt=0)
    sepal_width: float = Field(..., alias="sepal width (cm)", gt=0)
    petal_length: float = Field(..., alias="petal length (cm)", gt=0)
    petal_width: float = Field(..., alias="petal width (cm)", gt=0)

    class Config:
        populate_by_name = True


species_map = {
    0: 'Iris-setosa',
    1: 'Iris-versicolor',
    2: 'Iris-virginica'
}


@app.post("/predict")
def predict(data: irisInput):
    try:
        # Convert input data to DataFrame
        df = pd.DataFrame([data.model_dump(by_alias=True)])

        # 🔥 Fix: Rename columns to match training

        df = df.rename(columns={
            'sepal length (cm)': 'SepalLengthCm',
            'sepal width (cm)': 'SepalWidthCm',
            'petal length (cm)': 'PetalLengthCm',
            'petal width (cm)': 'PetalWidthCm'
        })

        # Scale the features
        scaled_features = scaler.transform(df)

        print("Initial check")
        print(scaled_features)

        # Make prediction
        prediction = model.predict(scaled_features)
        predicted_class = species_map[prediction[0]]

        print("Initial check 2")
        print(prediction)

        print(f'Predicted class: {predicted_class}')

        # if predicted_class == 2:
        #     predicted_class = 'Iris-versicolor'

        return {
            "prediction": predicted_class,
            "class_index": int(prediction[0])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/")
def read_root():
    return {"message": "Welcome to the Iris Classifier API"}
