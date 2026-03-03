import streamlit as st
import joblib
import numpy as np
model=joblib.load("model.pkl")
st.title("Loan Approval Prediction App")

income = st.number_input("Enter Income")
loan = st.number_input("Enter Loan Amount")

if st.button("Predict"):
    input_data=np.array([[income,loan]])
    prediction=model.predict(input_data)
    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")