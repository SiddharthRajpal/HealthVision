import streamlit as st

# Set page title
st.set_page_config(page_title='About Us | HealthVision')

# Define Neev Datta and Siddharth Rajpal
neev = {
    'name': 'Neev Datta',
    'title': 'Co-Founder',
    'bio': 'Neev is a passionate developer and entrepreneur with a background in computer science. He loves building products that solve real-world problems and has a particular interest in healthcare technology. In his free time, he enjoys playing basketball and reading science fiction.',

}

siddharth = {
    'name': 'Siddharth Rajpal',
    'title': 'Co-Founder',
    'bio': 'Siddharth is a creative thinker and problem solver with a strong foundation in mathematics and engineering. He is driven by a desire to use technology to make the world a better place and has a keen interest in AI and machine learning. In his free time, he enjoys hiking and playing guitar.',
}

# Define page layout
st.write(f"# About Us | HealthVision")
st.write(f"## {neev['name']} and {siddharth['name']}")
st.write(f"### {neev['title']} and {siddharth['title']}")

# Add photos
col1, col2 = st.columns(2)
with col1:
    st.image("Images/NeevImage.jpg", width=200)
    st.write(neev['name'])

with col2:
    st.image("Images/me.png", width=200)
    st.write(siddharth['name'])

# Add bios
st.markdown(f"### {neev['name']}")
st.write(neev['bio'])

st.markdown(f"### {siddharth['name']}")
st.write(siddharth['bio'])

# Add HealthVision description
st.markdown("## HealthVision")
st.write("HealthVision is an app that uses AI and machine learning to detect diseases from images uploaded by users. Our goal is to make healthcare more accessible and affordable by providing a fast, accurate, and reliable diagnosis tool. We believe that technology can revolutionize the way we approach healthcare, and we're excited to be at the forefront of this innovation.")

# Add contact information
st.markdown("## Contact Us")
st.write("If you have any questions, feedback, or just want to say hi, feel free to reach out to us at hello@healthvision.com. We'd love to hear from you!")
