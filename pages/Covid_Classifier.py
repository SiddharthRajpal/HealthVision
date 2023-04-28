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


st.title("Covid X-Ray Predictor")
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

st.write("COVID-19 is a highly infectious respiratory illness caused by the SARS-CoV-2 virus. It first emerged in Wuhan, China in late 2019 and quickly spread to become a global pandemic. Symptoms of COVID-19 can range from mild (fever, cough, fatigue, body aches) to severe (difficulty breathing, pneumonia, acute respiratory distress syndrome) and it can lead to death in some cases, especially in elderly people and those with underlying health conditions. The virus is primarily spread through respiratory droplets when an infected person coughs, sneezes, talks or breathes, and can also be spread by touching a surface contaminated with the virus and then touching one's mouth, nose, or eyes. Prevention measures include frequent hand washing, wearing masks, social distancing, and vaccination.")
st.write("Now, Covid cases are on the rise again... to prevent another pandemic like 2020, there is a need to classify Covid cases as soon as possible")
st.divider()
st.write("Hence, we have developed A Convolutional Neural Network (CNN) to predict whether the lung scan has Covid or not. It has been trained on more than 500 images divided into two classes, to upto 50 epochs.")
st.divider()
uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/CovidModel.h5","Models/CovidLabels.txt")
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
            <h1>It is Negative for Covid 19</h1>
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
            <h1>It is Positive for Covid 19</h1>
            """
        )
