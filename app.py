# app.py

import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Streamlit app UI
st.title('Seed Health Status')
st.subheader('Predict potato seed health based on sensor readings')

st.sidebar.header("Enter Sensor Data")
temperature = st.sidebar.number_input('Temperature (°C)', min_value=1.0, max_value=15.0, value=10.0)
humidity = st.sidebar.number_input('Humidity (%)', min_value=80, max_value=95, value=90)
co2 = st.sidebar.number_input('CO2 Concentration (ppm)', min_value=300, max_value=1000, value=500)

# Prediction
if st.sidebar.button('Predict'):
    input_data = np.array([[temperature, humidity, co2]])
    prediction = model.predict(input_data)[0]  # Get string label like 'Good', 'Fair', 'Poor'

    st.markdown(f"### Predicted Potato Health: `{prediction}`")

    # Show image based on prediction
    if prediction == 'Good':
        st.image('good_health.png', caption='🥔 Healthy Storage Conditions', use_container_width=True)
    elif prediction == 'Fair':
        st.image('fair_health.png', caption='⚠️ Moderate Health – Check Parameters', use_container_width=True)
    elif prediction == 'Poor':
        st.image('poor_health.png', caption='❌ Poor Conditions – Immediate Action Needed', use_container_width=True)
    else:
        st.warning("Unknown prediction. Please check input or model.")

    st.success(f"Prediction completed: {prediction}")
