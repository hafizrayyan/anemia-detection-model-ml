import streamlit as st
import pickle 
import numpy as np

with open("anemia_pr_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Anemia Detection")
Gender	 = st.selectbox("Enter Gender (0 = male , 1 = female): ",[0,1])
Hemoglobin= st.number_input("Enter Hemoglobin :")
MCH = st.number_input("Entetr MCH :")
MCHC = st.number_input("Enter MCHC :")
MCV = st.number_input("Enter MCV :")

if st.button("Predict"):
    input_data = np.array([[Gender, Hemoglobin, MCH, MCHC , MCV]])

    prediction = model.predict(input_data)

    if prediction == 0 :
        st.success(f"Result: {prediction[0]} Negative")
    
    elif prediction == 1 :
        st.success(f"Result: {prediction[0]} Positive")    
    
