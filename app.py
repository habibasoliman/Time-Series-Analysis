import streamlit as st
import pandas as pd
import numpy as np
import joblib
from xgboost import XGBRegressor
from datetime import datetime, timedelta

# Load model and scalers (if used)
model = joblib.load('xgboost_model.pkl')

# Title
st.title("Dept 3 Weekly Sales Forecast")

# Input features
st.write("### Input Features (for a week):")

lag_1 = st.number_input("Lag 1 (previous week)", value=20000.0)
lag_2 = st.number_input("Lag 2", value=19500.0)
lag_3 = st.number_input("Lag 3", value=19000.0)
temp = st.number_input("Temperature", value=55.0)
holiday = st.selectbox("Is Holiday?", [0, 1])
week = st.slider("Week Number", 1, 52, 26)
month = st.slider("Month", 1, 12, 6)
year = st.slider("Year", 2010, 2025, 2012)

# Predict
if st.button("Forecast Weekly Sales"):
    features = np.array([[lag_1, lag_2, lag_3, temp, holiday, week, month, year]])
    prediction = model.predict(features)[0]
    st.success(f"Predicted Weekly Sales: ${prediction:,.2f}")
