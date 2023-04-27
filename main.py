import streamlit as st
import imagerec
st.title("HealthVision")
st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. The infection can be caused by a variety of microorganisms, including bacteria, viruses, and fungi. Pneumonia can be acquired in the community or in a hospital setting, and it can range in severity from mild to life-threatening.")
st.write("Machine learning (ML) can play an important role in pneumonia prediction by analyzing medical images and identifying patterns that may be indicative of the disease. For example, ML models can be trained on large datasets of chest X-rays and CT scans to learn features that distinguish between normal lungs and those affected by pneumonia.")
st.write("We have developed A Convolutional Neural Network (CNN) to predict wether the lung scan has Pneumonia or not. It has been trained on more than 10,000 images divided into two classes, to upto 50 epochs.")

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/FinalModel.h5","Models/labels.txt")
    st.write(f"It is {y} with {round(conf*100)}% confidence")
