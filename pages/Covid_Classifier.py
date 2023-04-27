import streamlit as st
import imagerec
import pandas as pd
import random


st.title("Covid X-Ray Predictor")

st.write("COVID-19 is a highly infectious respiratory illness caused by the SARS-CoV-2 virus. It first emerged in Wuhan, China in late 2019 and quickly spread to become a global pandemic. Symptoms of COVID-19 can range from mild (fever, cough, fatigue, body aches) to severe (difficulty breathing, pneumonia, acute respiratory distress syndrome) and it can lead to death in some cases, especially in elderly people and those with underlying health conditions. The virus is primarily spread through respiratory droplets when an infected person coughs, sneezes, talks or breathes, and can also be spread by touching a surface contaminated with the virus and then touching one's mouth, nose, or eyes. Prevention measures include frequent hand washing, wearing masks, social distancing, and vaccination.")
st.write("Now, Covid cases are on the rise again... to prevent another pandemic like 2020, there is a need to classify Covid cases ASAP")
st.write("hence, we have developed A Convolutional Neural Network (CNN) to predict where the lung scan has Covid or not. It has been trained on more than 500 images divided into two classes, to upto 50 epochs.")

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/CovidModel.h5","Models/CovidLabels.txt")
    st.write(f"It is {y} ")