import streamlit as st
from landing_page import show_landing_page
from exoplanet import exoplanet_data_page
from habitable_planets import habitable_planets_page
from manual_predict import manual_predict_page
from predict_csv import predict_csv_page

st.title("Exoplanet Habitability Predictor 🌌")
st.sidebar.title("Navigation")

# Navigation Sidebar
page = st.sidebar.radio("", ["Home", "Exoplanets Data", "Habitable Planets", "Manual Predict Habitability", "Predict Uploaded CSV"])

# Page Routing
if page == "Home":
    show_landing_page()

elif page == "Exoplanets Data":
    exoplanet_data_page()

elif page == "Habitable Planets":
    habitable_planets_page()

elif page == "Manual Predict Habitability":
    manual_predict_page()

elif page == "Predict Uploaded CSV":
    predict_csv_page()
