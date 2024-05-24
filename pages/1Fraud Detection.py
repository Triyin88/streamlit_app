import streamlit as st

# dashboard title
st.markdown(
    """
    <style>
    @font-face {
        font-family: 'Amasis MT Pro Black';
        src: url('https://path-to-your-font/AmasisMTPro-Black.ttf');  /* Ensure you provide the correct URL to the font file */
    }
    .custom-text {
        font-family: 'Amasis MT Pro Black', sans-serif;
        font-size: 60px;
        font-weight: bold;
        color: black;
    }
    </style>
    <div class="custom-text">
      E-Commerce Fraud Detection
    </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.success("Fraud Detection")

import numpy as np
import pandas as pd
import time
import warnings
warnings.filterwarnings('ignore')
import plotly.express as px
from joblib import load
import streamlit as st

# load model
@st.cache_resource
def run_model():
   BBC=load("BBC.model")
   return BBC

model = run_model()

# Define function for enter data manually
def manual_data():
   # Define optimal threshold
   optimal_threshold = 0.496

   # Sample data for the graph
   sample_data = pd.DataFrame({
     'Account Age Days': [150, 365, 730, 30, 45, 60, 450],
     'Transaction Hour': [14, 9, 20, 3, 2, 23, 16],
     'Transaction Amount': [25.50, 100.75, 50.00, 500.00, 450.00, 600.00, 120.50]
   })

   def predict_proba(df):
      features = df[['Account Age Days', 'Transaction Hour', 'Transaction Amount']].values
      return model.predict_proba(features)[:, 1]

   # Predict probabilities for sample data
   sample_data['Probability of Fraud'] = predict_proba(sample_data)

   # Create input fields
   account_age_days = st.number_input("Account Age Days", min_value=0, max_value=10000, value=0)
   transaction_hour = st.number_input("Transaction Hour", min_value=0, max_value=23, value=0)
   transaction_amount = st.number_input("Transaction Amount", min_value=0.0, value=0.0)

   # Create a button for prediction
   if st.button("Predict"):
      # Create a feature array
      features = np.array([[account_age_days, transaction_hour, transaction_amount]])

      # Make prediction
      prediction_proba = model.predict_proba(features)[:, 1]
      prediction = (prediction_proba >= optimal_threshold).astype(int)

      # Display the result
      st.write(f"Prediction: {'Fraudulent' if prediction[0] == 1 else 'Not Fraudulent'}")
      st.write(f"Probability: {prediction_proba[0]:.2f}")
   
   # Plot the graph
   fig = px.scatter(
    sample_data,
    x='Transaction Amount',
    y='Probability of Fraud',
    title='Probability of Fraud vs Transaction Amount',
    labels={'Transaction Amount': 'Transaction Amount', 'Probability of Fraud': 'Probability of Fraud'},
    color='Probability of Fraud',
    color_continuous_scale='Viridis'
   )

   st.plotly_chart(fig)


# Define function for upload csv file:
def csv_file():
   uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

   if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        st.write("Uploaded data:")
        st.write(df)
        X_test=df[['Account Age Days', 'Transaction Hour', 'Transaction Amount']]

        if st.button("Predict"):
            # Make prediction
            prediction_proba = model.predict_proba(X_test, )[:, 1]
            prediction = model.predict(X_test, )
            df['Prediction']=prediction
            df['Probability']=prediction_proba
            df['Prediction'] = df['Prediction'].map({0: 'non-fraud', 1: 'fraud'})
            
            
            st.write("Predictions:")
            st.write(df)

            if df not in st.session_state:
               # Save the data to session state
               st.session_state.df = df
     
            
       

# Insert selectbox for data input
option = st.selectbox(
   "Choose data input method for fraud detection",
   ("None","Enter data manually", "Upload csv file"),
   placeholder="Choose data input method...",
)

st.write("You selected:", option)

if option == "Enter data manually":
   manual_data()

if option == "Upload csv file":
   csv_file()

