# dashboard/app.py
import streamlit as st
import pandas as pd
import os

st.title("Live IoT Monitoring Dashboard")

# Path relative to root
file_path = 'data/sensor_logs.csv'

if os.path.exists(file_path):
    df = pd.read_csv(file_path, names=['timestamp', 'temp', 'moisture'])
    if not df.empty:
        st.line_chart(df[['temp', 'moisture']])
    else:
        st.warning("CSV file is empty. Waiting for data...")
else:
    st.error(f"File not found at {file_path}. Ensure your simulation is running.")