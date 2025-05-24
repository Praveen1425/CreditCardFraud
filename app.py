import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load('amount_only_model (1).pkl')

st.set_page_config(page_title="Fraud Detection", layout="centered")
st.title("💳 Credit Card Fraud Detector")

# Input form
amount = st.number_input("Enter Transaction Amount ($):", min_value=0.01, format="%.2f")

if st.button("Check Transaction"):
    input_data = np.array([[amount]])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.error(f"⚠️ Potential Fraud Detected! Probability: {proba:.2f}")
    else:
        st.success(f"✅ Legitimate Transaction. Probability of Fraud: {proba:.2f}")
        