import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
st.set_page_config(
    page_title="HealthVision AI",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
components.html(
    """
    <style>
        p{
            margin:0px;
            padding:0px;
            color: white;
            font-family: "Source Sans Pro", sans-serif;
            font-size: 55px;
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
        }
    </style>
    <p id="effect">HealthVision AI</p>
    """,
    height=60,
)
st.title("Glaucoma Predictor")

st.write("Glaucoma is a group of eye diseases that damage the optic nerve, which connects the eye to the brain. This damage can cause irreversible vision loss and blindness if left untreated. The most common type of glaucoma, open-angle glaucoma, occurs when fluid builds up in the eye and increases pressure on the optic nerve.")
st.write("The problems caused by glaucoma include a gradual loss of peripheral (side) vision, which can go unnoticed until it becomes severe. In advanced stages, central vision can also be affected. While there is no cure for glaucoma, early detection and treatment can help slow or prevent vision loss. Treatment may include eye drops, medication, laser surgery, or traditional surgery to lower the pressure in the eye.")
st.write("hence, we have developed A Convolutional Neural Network (CNN) to predict whether the Eye scan has Glaucoma or not. It has been trained on more than 300 images divided into two classes, to upto 50 epochs.")

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/GlaucomaModel2.h5","Models/GlaucomaV2Labels.txt")
    st.write(f"It is {y} with confidence {int(conf*100)}")
