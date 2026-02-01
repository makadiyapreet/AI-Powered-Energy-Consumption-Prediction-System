import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_synthetic_data(num_days=365):
    print("Generating synthetic energy data... Please wait.")
    
    # 1. Setup Time Range (Hourly data for 1 year)
    start_date = datetime(2024, 1, 1)
    # 24 hours * num_days
    hours = num_days * 24
    date_rng = [start_date + timedelta(hours=x) for x in range(hours)]
    
    df = pd.DataFrame(date_rng, columns=['timestamp'])
    
    # 2. Generate Features (The "Fields" you requested)
    np.random.seed(42)  # For reproducible results
    
    # Extract useful time features
    df['hour'] = df['timestamp'].dt.hour
    df['day_of_week'] = df['timestamp'].dt.dayofweek # 0=Monday, 6=Sunday
    df['month'] = df['timestamp'].dt.month
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x >= 5 else 0)
    
    # Simulate Weather (Temperature in Celsius)
    # Cooler in mornings/winter, hotter in afternoons/summer
    # Base temp + daily variation + seasonal variation
    df['temperature'] = (
        20 + 
        5 * np.sin((df['hour'] - 6) / 24 * 2 * np.pi) + # Daily cycle
        10 * np.cos((df['month'] - 7) / 12 * 2 * np.pi) + # Seasonal cycle (peak in July)
        np.random.normal(0, 2, hours) # Random noise
    )
    
    # Simulate Humidity (%)
    df['humidity'] = 50 + 10 * np.cos((df['hour']) / 24 * 2 * np.pi) + np.random.normal(0, 5, hours)
    df['humidity'] = df['humidity'].clip(20, 100) # Keep between 20% and 100%

    # Simulate Square Footage (Random fluctuation representing active areas)
    df['square_footage'] = np.random.randint(1000, 5000, hours)

    # 3. Simulate Occupancy Rate (0 to 1 scale)
    # Low occupancy at night, high during day
    df['occupancy_rate'] = 0.1 + 0.8 * np.sin((df['hour'] - 6) / 24 * np.pi)
    df['occupancy_rate'] = df['occupancy_rate'].clip(0, 1)
    # Lower occupancy on weekends
    df.loc[df['is_weekend'] == 1, 'occupancy_rate'] *= 0.6
    
    # 4. Generate Target Variables (Energy Consumption in kWh) for different sectors
    
    # Formula: Base Load + (Temp Factor) + (Occupancy Factor) + Random Noise
    
    # Sector A: Residential (Peaks morning/evening)
    df['energy_consumption_residential'] = (
        5 + 
        (0.5 * df['temperature']) + 
        (10 * df['occupancy_rate']) + 
        np.random.normal(0, 0.5, hours)
    )

    # Sector B: Commercial (Peaks 9-5 business hours)
    # Strong correlation with occupancy and square footage
    df['energy_consumption_commercial'] = (
        20 + 
        (1.2 * df['temperature']) + 
        (50 * df['occupancy_rate']) + 
        (0.005 * df['square_footage']) +
        np.random.normal(0, 2, hours)
    )

    # Sector C: Industrial (High constant load + spikes)
    df['energy_consumption_industrial'] = (
        100 + 
        (20 * df['occupancy_rate']) + 
        np.random.normal(0, 5, hours)
    )

    # Cleanup: Ensure no negative energy values
    features = ['energy_consumption_residential', 'energy_consumption_commercial', 'energy_consumption_industrial']
    for f in features:
        df[f] = df[f].clip(lower=0)

    # Save to CSV
    df.to_csv('energy_dataset.csv', index=False)
    print(f"Success! 'energy_dataset.csv' created with {len(df)} rows.")
    print(df.head())

if __name__ == "__main__":
    generate_synthetic_data()