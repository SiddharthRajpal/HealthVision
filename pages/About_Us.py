import streamlit as st
import streamlit.components.v1 as components


# Set page title
st.set_page_config(
    page_title="HealthVision AI | About Us",
    page_icon=":dna:",
    initial_sidebar_state="expanded",
)
st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
img{border-radius: 10px;}
</style> """, unsafe_allow_html=True)
st.write('<style>div.row-widget.stMarkdown { font-size: 24px; }</style>', unsafe_allow_html=True)

# Define Neev Datta and Siddharth Rajpal
neev = {
    'name': 'Neev Datta',
    'title': '',
    'bio': 'I am a computer geek who loves coding, creating 3D art, and developing games. Over the last 2 years, I have mastered Python, C#, C++, HTML, CSS, Java, JavaScript, Dart, Rust and C. One of my specialities is creating entirely computer-generated scenes in Blender, I am so passionate about it that I even have an Instagram page dedicated solely to showcasing my creations. I also have invested many hours into mastering Unreal Engine and Unity. Ignoring computers I am also an aspiring professional racer in the Indian F4 Championship.',

}

siddharth = {
    'name': 'Siddharth Rajpal',
    'title': 'Founders',
    'bio': 'In my leisure time, I enjoy coding and possess proficiency in eight programming languages. Additionally, I indulge in reading books and have a firm grasp of mathematics and physics. Other than that I have a keen interest in AI. In addition to my coding expertise, I am also keenly interested in 3D art and have honed my skills with the Blender software. I am so passionate about it that I even have an Instagram page dedicated solely to showcasing my creations. Furthermore, I love 3D printing technology and enjoy experimenting with it whenever possible.',
}

# Define page layout
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
            left: 0px;
            position: fixed;
            background: -webkit-linear-gradient(0.25turn,#20D2FE, #5292FE);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        p{
            font-size: 2rem;
        }
    </style>
    <p id="effect">About Us</p>
    """,
    height=69,
)
st.write(f"## Founders")

# Add photos
col1, col2 = st.columns(2)
with col1:
    st.image("Images/NeevImage.jpeg", width=200)
    st.write(neev['name'])

with col2:
    st.image("Images/me.png", width=200)
    st.write(siddharth['name'])
st.divider()
# Add bios
st.markdown(f"### {neev['name']}")
st.write(neev['bio'])
st.divider()
st.markdown(f"### {siddharth['name']}")
st.write(siddharth['bio'])

# Add HealthVision description
st.markdown("## HealthVision")
st.write("HealthVision is an app that uses AI and machine learning to detect diseases from images uploaded by users. Our goal is to make healthcare more accessible and affordable by providing a fast, accurate, and reliable diagnosis tool. We believe that technology can revolutionize the way we approach healthcare, and we're excited to be at the forefront of this innovation.")


