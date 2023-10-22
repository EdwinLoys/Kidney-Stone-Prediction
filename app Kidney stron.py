import pickle
import streamlit as st
import pandas as pd

# Load the trained model
model = pickle.load(open("C:/Users/Edwin Loys/Desktop/Final Modul CI/final_model.pkl", "rb"))

# Define a function to make a prediction
def predict(gravity, ph, osmo, cond, urea, calc):
    features = pd.DataFrame({
        "gravity": gravity,
        "ph": ph,
        "osmo": osmo,
        "cond": cond,
        "urea": urea,
        "calc": calc
    }, index=[0])
    prediction = model.predict(features)
    return prediction

# Add a title
st.title("kidney_stone_prediction")

# Add input fields for the features
gravity = st.number_input("Gravity: ")
ph = st.number_input("PH: ")
osmo = st.number_input("Osmolarity: ")
cond = st.number_input("Conductivity: ")
urea = st.number_input("Urea: ")
calc = st.number_input("Calcium: ")

result = ""
if st.button("Predict"):
    result = predict(gravity, ph, osmo, cond, urea, calc)
    st.success('The output is {}'.format(result))
