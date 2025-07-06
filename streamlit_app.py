import streamlit as st
import pickle 
import numpy as np

model = pickle.load(open('insurance_trained_model.pkl', 'rb'))

st.title("Insurance Prediction Model")

age = st.number_input('Enter the age:', min_value=0, max_value=120)
bmi = st.number_input('Enter the BMI:', step=0.1)
No_children = st.number_input('Enter the number of children:', min_value=0, max_value=5)
smoker = st.selectbox('Enter the smoker status:', ['no', 'yes'])
region = st.selectbox('Enter the region:', ['northeast', 'northwest', 'southeast', 'southwest'])

# Manual One-Hot Encoding
smoker_yes = 1 if smoker == 'yes' else 0

region_northeast = 1 if region == 'northeast' else 0
region_northwest = 1 if region == 'northwest' else 0
region_southeast = 1 if region == 'southeast' else 0
region_southwest = 1 if region == 'southwest' else 0

input_data = [age, bmi, No_children, smoker_yes, region_northeast, region_northwest, region_southeast, region_southwest]
input_data = np.array(input_data).reshape(1, -1)

if st.button('Predict'):
    prediction = model.predict(input_data)
    st.success(f"Predicted Insurance Cost: ${prediction[0]:.2f}")
