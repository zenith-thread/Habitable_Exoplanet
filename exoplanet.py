import streamlit as st
import pandas as pd
from io import BytesIO

def exoplanet_data_page():
    st.header("📊 Exoplanet Data")
    dataset = pd.read_csv('mixed_columns_plname.csv')

    # Show Dataset
    st.dataframe(dataset)

    # Download Dataset as Excel
    output = BytesIO()
    dataset.to_excel(output, index=False, engine='openpyxl')
    st.download_button(
        label="📥 Download Dataset as Excel",
        data=output.getvalue(),
        file_name="exoplanet_dataset.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
