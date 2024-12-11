import streamlit as st
import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from tensorflow.keras.layers import LeakyReLU
from tensorflow.keras.initializers import HeUniform
from io import BytesIO

# Load Model and Scaler
custom_objects = {'LeakyReLU': LeakyReLU, 'HeUniform': HeUniform}
model = load_model('SELU_Habitable.h5', custom_objects=custom_objects)
scaler = joblib.load('habitability_scaler.pkl')

def predict_csv_page():
    st.header("📂 Predict Habitability for Multiple Planets")
    uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])
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

    if uploaded_file:
            # Read Uploaded CSV without assuming headers
            input_df = pd.read_csv(uploaded_file, header=None)  # Ignore file's headers
            input_df.columns = labels  # Assign custom headers
            st.write("### Uploaded Data")
            st.dataframe(input_df)

            # Make Predictions
            try:
                # Scale the data
                scaled_data = scaler.transform(input_df.values)
                
                # Get predictions (probabilities)
                predictions = model.predict(scaled_data)  # Returns probabilities
                
                # Ensure probabilities are normalized
                predictions = predictions / predictions.sum(axis=1, keepdims=True)

                # Extract predicted classes and confidence for the predicted class
                predicted_classes = predictions.argmax(axis=1)
                confidence_scores = predictions[np.arange(predictions.shape[0]), predicted_classes]

                # Add Predictions and Confidence Scores to DataFrame
                input_df['Predicted_Class'] = predicted_classes
                input_df['Predicted_Confidence'] = confidence_scores

                # Display Results
                st.write("### Predictions")
                st.dataframe(input_df)

                # Download Results as Excel
                output = BytesIO()
                input_df.to_excel(output, index=False, engine='openpyxl')
                st.download_button(
                    label="📥 Download Predictions as Excel",
                    data=output.getvalue(),
                    file_name="predicted_habitability_with_confidence.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")