from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from typing import List
import numpy as np

# Initialize the FastAPI app
app = FastAPI()

# Load the serialized model
model = joblib.load('rf_model_2024-09-22-15-00-00.pkl')  # Use the correct timestamped filename

# Define the input data schema using Pydantic for validation
class SalesInput(BaseModel):
    Store: int
    DayOfWeek: int
    Customers: int
    Open: int
    Promo: int
    StateHoliday: str
    SchoolHoliday: int
    StoreType: int
    Assortment: int
    CompetitionDistance: float
    CompetitionOpenSinceMonth: int
    CompetitionOpenSinceYear: int
    Promo2: int
    Promo2SinceWeek: int
    Promo2SinceYear: int

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Rossmann Sales Prediction API"}

# Define the prediction endpoint
@app.post("/predict/")
def predict_sales(data: List[SalesInput]):
    try:
        # Convert input data into a DataFrame
        input_data = pd.DataFrame([item.dict() for item in data])

        # Preprocess the data (if necessary based on your model's needs)
        # E.g., scaling, label encoding, etc.

        # Make predictions
        predictions = model.predict(input_data)

        # Return the predictions as a list
        return {"predictions": predictions.tolist()}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Run the app (for local testing)
# Use: `uvicorn <this_file>:app --reload` to run this app locally.
