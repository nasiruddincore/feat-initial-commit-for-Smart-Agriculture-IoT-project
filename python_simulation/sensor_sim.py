# python_simulation/sensor_sim.py
import csv
import time
import random

def get_sensor_data():
    return {
        "temperature": round(random.uniform(20.0, 35.0), 2),
        "humidity": round(random.uniform(30.0, 70.0), 2),
        "soil_moisture": random.randint(100, 1000),
        "light_intensity": random.randint(0, 100)
    }

def log_data():
    with open('data/sensor_logs.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        while True:
            data = get_sensor_data()
            writer.writerow([time.time(), data['temperature'], data['soil_moisture']])
            print(f"Logged: {data}")
            time.sleep(2)

if __name__ == "__main__":
    log_data()