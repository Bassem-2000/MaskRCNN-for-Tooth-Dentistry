import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")


me = Image.open('me.jpg')
col4, col5 = st.columns([0.7, 0.3], gap="large")
with col5:
    st.image(me)
with col4:
    st.title("About me")
    st.write("## My name is Bassem Ahmed")

    paragraph = """
    ***Greetings! I'm a 23-year-old graduate with a passion for Electronics and Computer Engineering (ECE),
    specializing in the exciting realms of Artificial Intelligence (AI).
    My journey has been marked by a 3.7 GPA, which reflects my dedication to learning and pushing
    the boundaries of innovation.***

    !***What truly fascinates me about the AI and Computer Vision field is
    its potential to revolutionize industries and solve complex problems in creative ways. I've had
    the privilege to explore cutting-edge technologies, from developing predictive models to harnessing
    the power of machine learning algorithms.***

    ***As someone who thrives on challenges and loves to explore
    the uncharted territories of technology, I'm always on the lookout for new opportunities to collaborate
    and contribute to this ever-evolving landscape. So, let's embark on this exciting journey together and
    unlock the potential of AI and Computer Vision!***
    """

    st.write(paragraph,unsafe_allow_html=True)
    
st.markdown(""" <style>
.css-ffhzg2{background-image: url("https://images.squarespace-cdn.com/content/v1/607df72a80f9a2508797f76d/1620747525834-TEXH964J2WSMZMZAUQ5R/Home-Ai.jpg");
background-repeat: no-repeat;
background-size: cover;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True
)
