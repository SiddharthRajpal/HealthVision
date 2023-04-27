import streamlit as st
import pandas as pd
from io import StringIO
import imagerec
st.title("X-Ray Characterization")
uploaded_file = st.file_uploader("Choose a File", type=['jpg','png','jpeg'])
x = st.button("Predict")
if x:
    with st.spinner("Predicting..."):
        y= imagerec.imagerecognise(uploaded_file,"Models/FinalModel.h5","Models/labels.txt")
    st.write(y)
