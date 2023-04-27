import streamlit as st

# Set page title
st.set_page_config(
    page_title="HealthVision AI",
    page_icon="🧬",
    initial_sidebar_state="expanded",
)

# Define page layout
def page_layout():
    # Set page title
    st.title("Welcome to HealthVision")
    
    # Add app description
    st.write("HealthVision is an app that combines various ML models into one in order to determine if you have a disease, using CNN and X-rays of the patients. The app was made by Neev Datta and Siddharth Rajpal for a project. The app uses advanced algorithms to diagnose various diseases, including lung cancer, tuberculosis, and pneumonia.")
    
    # Add benefits section
    st.markdown("## Benefits:")
    st.write("- Fast and accurate diagnosis of diseases")
    st.write("- Non-invasive and painless diagnosis using X-rays")
    st.write("- Accessible from anywhere, anytime")
    
    # Add novelty section
    st.markdown("## Novelty:")
    st.write("- HealthVision combines multiple ML models into one app")
    st.write("- The app uses CNN and X-rays to diagnose diseases")
    st.write("- HealthVision uses advanced algorithms to provide fast and accurate diagnosis")
    
    # Add relevance section
    st.markdown("## Relevance:")
    st.write("- HealthVision can diagnose various diseases, including lung cancer, tuberculosis, and pneumonia")
    st.write("- The app can be used by doctors, hospitals, and patients")
    st.write("- HealthVision can improve the accuracy and speed of disease diagnosis")
    
    # Add uses section
    st.markdown("## Uses:")
    st.write("- Hospitals and clinics can use HealthVision to diagnose diseases more accurately and quickly")
    st.write("- Patients can use HealthVision to get a quick and accurate diagnosis without the need for invasive procedures")
    st.write("- HealthVision can be used to screen large populations for diseases, such as tuberculosis and lung cancer")
    
# Render page layout
page_layout()
