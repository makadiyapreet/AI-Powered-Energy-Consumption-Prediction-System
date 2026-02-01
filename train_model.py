import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import joblib

def train_model():
    print("Loading dataset...")
    df = pd.read_csv('energy_dataset.csv')
    
    features = ['temperature', 'humidity', 'occupancy_rate', 'hour', 'day_of_week', 'is_weekend', 'square_footage']
    target = 'energy_consumption_commercial' 
    
    X = df[features]
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Training Random Forest Model... (No extra installation needed)")
    # Using 200 trees for higher accuracy than before
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    
    print(f"Model Training Complete!")
    print(f"Mean Absolute Error: {mae:.2f} kWh")
    
    joblib.dump(model, 'energy_model.pkl')
    print("Model saved as 'energy_model.pkl'")

if __name__ == "__main__":
    train_model()