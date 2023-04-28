import streamlit as st
import imagerec
import pandas as pd
import random
import streamlit.components.v1 as components


st.set_page_config(
    page_title="HealthVision AI",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)
components.html(
    """
    <style>
        #effect{
            margin:0px;
            padding:0px;
            font-family: "Source Sans Pro", sans-serif;
            font-size: max(8vw, 20px);
            font-weight: 700;
            top: 0px;
            right: 25%;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#FF4C4B, #FFFB80);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">HealthVision AI</p>
    """,
    height=69,
)

st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.title("Pneumonia X-Ray Predictor")

st.write("Pneumonia is an infection that inflames the air sacs in one or both lungs, causing them to fill with fluid or pus. The infection can be caused by a variety of microorganisms, including bacteria, viruses, and fungi. Pneumonia can be acquired in the community or in a hospital setting, and it can range in severity from mild to life-threatening.")
st.divider()
st.write("Machine learning (ML) can play an important role in pneumonia prediction by analyzing medical images and identifying patterns that may be indicative of the disease. For example, ML models can be trained on large datasets of chest X-rays and CT scans to learn features that distinguish between normal lungs and those affected by pneumonia.")
st.divider()
st.write("We have developed A Convolutional Neural Network (CNN) to predict whether the lung scan has Pneumonia or not. It has been trained on more than 10,000 images divided into two classes, to upto 50 epochs.")
st.divider()

uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/Pnemonia.h5","Models/labelsPnemonia.txt")
    if y.strip() == "Negative":
        components.html(
            """
            <style>
            h1{
                
                background: -webkit-linear-gradient(0.25turn,#01CCF7, #8BF5F5);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>It is not Pneumomnia</h1>
            """
        )
    else:
        components.html(
            """
            <style>
            h1{
                background: -webkit-linear-gradient(0.25turn,#FF4C4B, #F70000);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                font-family: "Source Sans Pro", sans-serif;
            }
            </style>
            <h1>It is Pneumomnia</h1>
            """
        )
