import streamlit as st
import pickle
import pandas as pd


st.set_page_config(layout="wide")

st.title('Diabetes Prediction Application')

st.divider()

cols1, cols2, cols3, cols4 = st.columns(4)


with cols1:
  pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0, step=1)

  bmi = st.number_input("BMI", min_value=0.0, max_value=100.0, value=30.0, step=0.1)

with cols2:

  glucose = st.number_input("Glucose", min_value=0, max_value=200, value=100, step=1)

  blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=100, step=1)
  
with cols3:
  
  skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=25, step=1)
  
  insulin = st.number_input("Insulin", min_value=0, max_value=1000, value=100, step=1)
  
with cols4:
  
  age = st.number_input("Age", min_value=0, max_value=100, value=25, step=1)
  
  
with cols1:
  model_type = st.selectbox(
        "Which classification model would you like to use?",
        ("Random Forest", "Gradient Boost"),
    )  
  

if model_type == "Random Forest":
  model = pickle.load(open('rf.sav', 'rb'))
else:
  model = pickle.load(open('gb.sav', 'rb'))

ex = pd.DataFrame([[
  pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, age
]])

ex.columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'Age']

st.write("")
if st.button('Predict Diabetes'):
  
    predictions = model.predict(ex)
    if predictions[0] == 1:
        st.write('Diabetes Prediction: Positive')
    else:
        st.write('Diabetes Prediction: Negative')

