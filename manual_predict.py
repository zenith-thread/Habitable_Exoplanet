import streamlit as st
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.initializers import HeUniform

# Load Model and Scaler
custom_objects = {'LeakyReLU': LeakyReLU, 'HeUniform': HeUniform}
model = load_model('SELU_Habitable.h5', custom_objects=custom_objects)
scaler = joblib.load('habitability_scaler.pkl')

# Prediction Function
def make_prediction(input_data):
    scaled_data = scaler.transform([input_data])
    prediction = model.predict(scaled_data)
    predicted_class = prediction.argmax(axis=1)[0]
    return predicted_class

def manual_predict_page():
    st.header("🔮 Predict Habitability for a Single Planet")
    st.write("Enter the details of a planet to predict its habitability class.")

    # Input Form for User
    features = []
    labels = [
        "P. Zone Class", "P. Mass Class", "P. Composition Class", "P. Atmosphere Class", 
        "P. Habitable Class", "P. Min Mass (EU)", "P. Mass (EU)", "P. Radius (EU)", 
        "P. Density (EU)", "P. Gravity (EU)", "P. Esc Vel (EU)", "PSFluxMin", 
        "PSFluxMean", "PSFluxMax", "P. Teq Min (K)", "P. Teq Mean (K)", "P. Teq Max (K)", 
        "P. Surf Press (EU)", "P. Mag", "P. Appar Size (deg)", "P. Period (days)", 
        "P. Sem Major Axis (AU)", "P. Eccentricity", "P. Mean Distance (AU)", "P. Omega (deg)", 
        "S. Mass (SU)", "S. Radius (SU)", "S. Teff (K)", "S. Luminosity (SU)", "S. [Fe/H]", 
        "S. Age (Gyrs)", "S. Appar Mag", "S. Mag from Planet", "S. Size from Planet (deg)", 
        "S. Hab Zone Min (AU)", "S. Hab Zone Max (AU)", "P. HZD", "P. HZC", "P. HZA", 
        "P. HZI", "P. ESI"
    ]

    # Dynamically create input boxes
    for label in labels:
        value = st.number_input(f"{label}", value=0.0)
        features.append(value)

    # Predict Button
    if st.button("Predict"):
        prediction = make_prediction(features)
        st.success(f"The predicted habitability class is: **{prediction}**")
