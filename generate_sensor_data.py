import pandas as pd
import numpy as np

# Simulate sensor data (Temperature, Humidity, CO2)
np.random.seed(42)

def generate_data(n=1000):
    data = {
        'Temperature': np.random.uniform(1, 15, n),  # Temperature between 1°C and 15°C
        'Humidity': np.random.uniform(80, 95, n),    # Humidity between 80% and 95%
        'CO2': np.random.uniform(300, 1000, n),      # CO2 between 300ppm and 1000ppm
    }
    df = pd.DataFrame(data)
    # Create Health status based on the sensor readings
    conditions = [
        (df['Temperature'] >= 5) & (df['Temperature'] <= 10) &  # Ideal temperature range
        (df['Humidity'] >= 85) & (df['Humidity'] <= 92) &       # Ideal humidity range
        (df['CO2'] >= 350) & (df['CO2'] <= 800),                # Ideal CO2 range
    ]
    choices = ['Good']
    df['Health'] = np.select(conditions, choices, default='Fair')  # Default to 'Fair'
    
    # Add some 'Poor' readings with random violations
    df.loc[df['Temperature'] < 3, 'Health'] = 'Poor'
    df.loc[df['Humidity'] > 93, 'Health'] = 'Poor'
    df.loc[df['CO2'] > 900, 'Health'] = 'Poor'
    
    return df

# Generate data and save it to a CSV file
df = generate_data(1000)
df.to_csv('sensor_data.csv', index=False)
print("Sensor data generated and saved to sensor_data.csv")
