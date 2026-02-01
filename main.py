from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS so the frontend can talk to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the trained model
try:
    model = joblib.load('energy_model.pkl')
except:
    print("ERROR: energy_model.pkl not found. Please run train_model.py first.")

# Input structure for single prediction
class EnergyInput(BaseModel):
    temperature: float
    humidity: float
    occupancy_rate: float
    hour: int
    day_of_week: int
    is_weekend: int
    square_footage: int

# Input structure for daily forecast
class DayInput(BaseModel):
    temperature_max: float
    temperature_min: float
    humidity: float
    occupancy_rate: float
    day_of_week: int
    is_weekend: int
    square_footage: int

# Endpoint 1: Predict Single Point
@app.post("/predict")
def predict_energy(data: EnergyInput):
    input_data = pd.DataFrame([data.dict()])
    prediction = model.predict(input_data)
    return {"predicted_energy_consumption": float(prediction[0])}

# Endpoint 2: Predict Full 24 Hours
@app.post("/predict_day")
def predict_day(data: DayInput):
    hours = list(range(24))
    temps = []
    
    # Generate a realistic temperature curve (peak at 2 PM)
    for h in hours:
        norm_time = (h - 14) / 12 * np.pi
        temp_at_h = (data.temperature_max + data.temperature_min) / 2 - \
                    (data.temperature_max - data.temperature_min) / 2 * np.cos(norm_time)
        temps.append(temp_at_h)

    # Create batch data for 24 hours
    batch_data = pd.DataFrame({
        'temperature': temps,
        'humidity': [data.humidity] * 24,
        'occupancy_rate': [data.occupancy_rate if 8 <= h <= 18 else data.occupancy_rate * 0.2 for h in hours],
        'hour': hours,
        'day_of_week': [data.day_of_week] * 24,
        'is_weekend': [data.is_weekend] * 24,
        'square_footage': [data.square_footage] * 24
    })
    
    predictions = model.predict(batch_data)
    
    return {
        "hourly_predictions": predictions.tolist(),
        "hourly_temps": temps
    }

# Endpoint 3: AI Insights (Explainability)
@app.get("/model_insights")
def get_model_insights():
    # Feature names must match training order
    feature_names = ['Temperature', 'Humidity', 'Occupancy', 'Hour', 'Day', 'Weekend', 'Sq Ft']
    importances = model.feature_importances_
    return {"features": feature_names, "importance": importances.tolist()}