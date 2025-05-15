from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load the saved model at startup
model = joblib.load('models/student_performance_model.pkl')


app = FastAPI(title="Student Performance Prediction API")

# Define input data model (request body)
class StudentData(BaseModel):
    Hours_Studied: float
    Previous_Scores: float
    Extracurricular_Activities: str  # 'Yes' or 'No'
    Sleep_Hours: float
    Sample_Question_Papers_Practiced: int

@app.get("/")
def read_root():
    return { "Student Performance Prediction API"}

@app.get("/features")
def get_features():
    return {
        "features": [
            "Hours_Studied (float)",
            "Previous_Scores (float)",
            "Extracurricular_Activities ('Yes' or 'No')",
            "Sleep_Hours (float)",
            "Sample_Question_Papers_Practiced (int)"
        ]
    }


@app.post("/predict/")
def predict_performance(data: StudentData):
    # Convert input data to DataFrame for model prediction
    input_df = pd.DataFrame([{
        'Hours Studied': data.Hours_Studied,
        'Previous Scores': data.Previous_Scores,
        'Extracurricular Activities': data.Extracurricular_Activities,
        'Sleep Hours': data.Sleep_Hours,
        'Sample Question Papers Practiced': data.Sample_Question_Papers_Practiced
    }])
    
    # Predict using the loaded model
    prediction = model.predict(input_df)
    
    return {"Predicted_Performance_Index": round(prediction[0], 2)}
