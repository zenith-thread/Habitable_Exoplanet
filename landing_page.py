import streamlit as st

def show_landing_page():
    st.markdown(
        """
        <style>
        .title {
            color: #004466;
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            color: #333333;
            font-size: 24px;
            text-align: center;
        }
        .content {
            text-align: justify;
            font-size: 18px;
            margin: 20px auto;
            max-width: 800px;
            color: #555555;
        }
        .footer {
            color: #777777;
            text-align: center;
            margin-top: 50px;
        }
        </style>
        <div class="title">Exoplanet Habitability Predictor</div>
        <div class="subtitle">A Deep Learning Based Web App</div>
        <div class="content">
            Welcome to the <strong>Exoplanet Habitability Predictor</strong>! This project is designed to analyze 
            exoplanet datasets and predict whether planets are habitable based on various parameters. 
            Powered by a trained Deep learning model, this tool allows you to:
            <ul>
                <li>Explore exoplanet datasets 📊</li>
                <li>View planets predicted as habitable 🌍</li>
                <li>Manually predict habitability for single planets 🔮</li>
                <li>Upload a CSV file for batch predictions 📂</li>
            </ul>
            Start exploring now by navigating to the different sections using the top menu bar.
        </div>
        <div class="footer">
            Created with ❤️ by Ahmed Raza | Powered by Streamlit & TensorFlow
        </div>
        """,
        unsafe_allow_html=True,
    )
