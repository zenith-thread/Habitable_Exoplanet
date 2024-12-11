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

    # Mappings for categorical variables
    zone_class_mapping = {'Cold': 0, 'Hot': 1, 'Warm': 2}
    mass_class_mapping = {'Jovian': 0, 'Mercurian': 1, 'Neptunian': 2, 'Subterran': 3, 'Superterran': 4, 'Terran': 5}
    composition_class_mapping = {'gas': 0, 'iron': 1, 'rocky-iron': 2, 'rocky-water': 3, 'water-gas': 4}
    atmosphere_class_mapping = {'hydrogen-rich': 0, 'metals-rich': 1, 'no-atmosphere': 2}
    habitable_class_mapping = {'non-habitable': 0, 'mesoplanet': 1, 'thermoplanet': 2}

    # Dropdowns for categorical inputs
    zone_class = st.selectbox("P. Zone Class", options=list(zone_class_mapping.keys()))
    mass_class = st.selectbox("P. Mass Class", options=list(mass_class_mapping.keys()))
    composition_class = st.selectbox("P. Composition Class", options=list(composition_class_mapping.keys()))
    atmosphere_class = st.selectbox("P. Atmosphere Class", options=list(atmosphere_class_mapping.keys()))
    habitable_class = st.selectbox("P. Habitable Class", options=list(habitable_class_mapping.keys()))

    # Numeric inputs for the remaining features
    labels = [
        "P. Min Mass (EU)", "P. Mass (EU)", "P. Radius (EU)", 
        "P. Density (EU)", "P. Gravity (EU)", "P. Esc Vel (EU)", "PSFluxMin", 
        "PSFluxMean", "PSFluxMax", "P. Teq Min (K)", "P. Teq Mean (K)", "P. Teq Max (K)", 
        "P. Surf Press (EU)", "P. Mag", "P. Appar Size (deg)", "P. Period (days)", 
        "P. Sem Major Axis (AU)", "P. Eccentricity", "P. Mean Distance (AU)", "P. Omega (deg)", 
        "S. Mass (SU)", "S. Radius (SU)", "S. Teff (K)", "S. Luminosity (SU)", "S. [Fe/H]", 
        "S. Age (Gyrs)", "S. Appar Mag", "S. Mag from Planet", "S. Size from Planet (deg)", 
        "S. Hab Zone Min (AU)", "S. Hab Zone Max (AU)", "P. HZD", "P. HZC", "P. HZA", 
        "P. HZI", "P. ESI"
    ]

    # Collect all inputs in one go
    features = [
        zone_class_mapping[zone_class],
        mass_class_mapping[mass_class],
        composition_class_mapping[composition_class],
        atmosphere_class_mapping[atmosphere_class],
        habitable_class_mapping[habitable_class]
    ]
    for i, label in enumerate(labels):
        value = st.number_input(f"{label}", value=0.0, key=f"input_{i}")
        features.append(value)

    # Predict Button
    if st.button("Predict"):
        prediction = make_prediction(features)
        st.success(f"The predicted habitability class is: **{prediction}**")
