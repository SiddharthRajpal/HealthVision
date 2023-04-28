import streamlit as st
from skin_cancer import detectskin
import pandas as pd
import random
import imagerec
import streamlit.components.v1 as components
st.set_page_config(
    page_title="HealthVision AI",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)
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


st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.title("Skin Cancer Predictor")

st.write('<style>div.row-widget.stMarkdown { font-size: 1.2rem; }</style>', unsafe_allow_html=True)


st.write("Skin cancer is a type of cancer that develops in the cells of the skin. It is the most common type of cancer worldwide, and its incidence is increasing every year. There are three main types of skin cancer: basal cell carcinoma, squamous cell carcinoma, and melanoma. Basal cell and squamous cell carcinomas are the most common types and are usually caused by prolonged exposure to the sun. Melanoma, while less common, is the most dangerous type and can spread to other parts of the body if left untreated. Symptoms of skin cancer may include changes in the appearance of moles or other skin lesions, such as growth, bleeding, or itching. Early detection and treatment are crucial for successful treatment and can greatly improve the prognosis. Prevention measures include avoiding prolonged exposure to the sun, using sunscreen, and wearing protective clothing.")
st.divider()
st.write("Machine learning (ML) is playing an increasingly important role in the detection of skin cancer. ML algorithms can be trained on large datasets of images of skin lesions to identify patterns and features that are associated with different types of skin cancer. This allows ML algorithms to classify skin lesions accurately and quickly, often outperforming human experts in terms of accuracy.")
st.write("We have developed A Convolutional Neural Network (CNN) to predict whether the skin is benign or malignant. It has been trained on more than 1,000 images divided into two classes, to upto 20 epochs.")
st.divider()
uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])


if uploaded_file!=None:
    st.image(uploaded_file)
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y,conf = imagerec.imagerecognise(uploaded_file,"Models/SkinCancerModel.h5","Models/SkinCancerLabel.txt")
        
    if y.strip() == "Benign":
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
            <h1>It is Benign</h1>
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
            <h1>Cancer Detected</h1>
            """
        )
