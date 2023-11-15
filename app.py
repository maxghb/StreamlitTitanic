# import library

import streamlit as st
from joblib import load

st.title('Hello World')

model = load('titanic_model.joblib')

st.title('Titanic Survival Prediction')

st.sidebar.title('Menu')

menu = ['Home', 'Prediction']

st.sidebar.selectbox('', menu)

age = st.slider('Age', 0.42, 80.0, 30.0)
sibsp = st.slider('SibSp', 0, 8, 0)
parch = st.slider('Parch', 0, 6, 0)
fare = st.slider('Fare', 0.0, 512.3292, 32.20)

predict_button = st.button('Predict')

# prediction logic

if predict_button:
    # รับค่าจาก input มาใส่ตัวแปรแบบ list
    input_data = [[age, sibsp, parch, fare]]

    prediction = model.predict(input_data)
    # หาค่าความน่าจะเป็นที่จะรอด
    predict_proba = model.predict_proba(input_data)
    st.write(prediction[0])

    st.subheader('Prediction')
    if prediction[0] == 1:
        st.write('Survived')
    else:
        st.write('Not Survived')

    st.subheader('Prediction Probability')
    st.write(f'Survived :{predict_proba[0][1]:.2f}')
    st.write(f'Not Survived :{predict_proba[0][0]:.2f}')