import streamlit as st
from joblib import load

#st.title('Hello word')

model = load('titanic_model.joblib')

st.title('Titanic Survival Prediction')

st.sidebar.title('Menu')

Menu = ['Home', 'Predition']

st.sidebar.selectbox('', menu)

age = st.sidebar('Age', 0.42, 80.0, 30.0)
sibsp = st.slider('SibSp', 0, 8, 0)
parch = st.slider('Parch', 0, 9, 0)
fare = st.slider('Fare', 0.0, 512.30, 32.20)

predict_button = st.button('Predict')

if predict_button :

 input_data = [[age, sibsp, parch, fare]]

prediction = model.predict(input_data)

st.subheader('Prediction')
if prediction[0] == 1:
    st.write('Survived')
else:
    st.write('Not Survived')

#st.subheader('Prediction Probability')
#st.write(f'Survived: {predict_proba[0][1]:2f}')   
#st.write(f'Not Survived: {predict_proba[0][0]:2f}')  