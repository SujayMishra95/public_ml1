# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

exercise_model = pickle.load(open('C:/Users/Sujay/Desktop/Exercise Calories/exercise_cals_sk.sav', 'rb'))

    # page title
st.title('Calories Burnt Prediction using Machine Learning')
    
Gender = st.text_input('Gender (Male:0, Female:1)')
Age = st.text_input('Age (years)')
Height = st.text_input('Height (cm)')
Weight = st.text_input('Weight (kg)')
Duration = st.text_input('Exercise Duration (mins)')
Heart_Rate = st.text_input('Heart Rate (bps)')
Body_Temp = st.text_input('Body Temperature (Degrees Celcius)')
 
     
     
    # code for Prediction
cals_burnt_pred = ''
    
    # creating a button for Prediction
    
if st.button('Number of Calories burnt result'):
      cals_burnt = exercise_model.predict([[Gender, Age, Height, Weight, Duration, Heart_Rate, Body_Temp]])                          
     
      cals_burnt_pred = cals_burnt
st.success(cals_burnt_pred)

    
