import streamlit as st
import pandas as pd
from io import BytesIO

def habitable_planets_page():
    st.header("📊 Habitable Planets Predicted by Model")
    habitable_dataset = pd.read_csv('planets_predicted_as_habitable_with_classes.csv')

    # Show Dataset
    st.dataframe(habitable_dataset)

    # Download Result as Excel
    output = BytesIO()
    habitable_dataset.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Download Result as Excel",
        data=output.getvalue(),
        file_name="habitable_exoplanet_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
