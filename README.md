# IoT-Enabled Smart Agriculture Monitoring System

## 🚀 Overview
An end-to-end IoT solution designed to monitor environmental parameters (Soil Moisture, Temperature, Humidity, Light) and automate irrigation systems. This project minimizes water wastage by up to 30% through real-time data analysis.

## 🛠️ Tech Stack
- **Hardware Simulation:** ESP32, Wokwi, DHT22 Sensor, Relay Module.
- **Backend/Automation:** Python (Data Logging), Arduino/C++.
- **Dashboard:** Streamlit (Real-time data visualization).
- **Architecture:** Field-to-Cloud data pipeline via MQTT and CSV logging.

## ⚙️ Features
- **Real-time Monitoring:** Tracks soil, ambient temp, and light levels.
- **Automated Irrigation:** Logic-based pump control to optimize water usage.
- **Data Analytics:** Logs sensor history to CSV for trend analysis.
- **Dashboard:** Interactive UI to view live field status.

## 📂 Folder Structure
- `/arduino_code`: Firmware for sensor acquisition and relay control.
- `/python_simulation`: Script for virtual sensor data generation.
- `/dashboard`: Streamlit application for real-time monitoring.
- `/data`: CSV storage for historical logging.

## 🚀 How to Run
1. Clone the repository: `git clone <your-repo-url>`
2. Create a virtual environment: `python -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run simulation: `python python_simulation/sensor_sim.py`
5. Launch dashboard: `streamlit run dashboard/app.py`
