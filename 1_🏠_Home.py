import streamlit as st
import numpy as np
from PIL import Image
from streamlit_option_menu import option_menu
import requests
from io import BytesIO

def space():
    for i in range(4):
        st.write("") 
st.set_page_config(page_title='Instance Segmentation app', 
                   page_icon="🦷", 
                   layout="wide",
                   initial_sidebar_state = 'collapsed'
                   )


# st.image(img, use_column_width=True)

# selected = option_menu(
#     menu_title=None,
#     options=['Home', 'About', 'Contact'], 
#     icons=['house', 'book', 'envelope'],
#     orientation='horizontal'
# )


col1, col2, col3 = st.columns([1.5, 3.5, 1])

with col2:
    st.header('**Computer Vision in Tooth Dentistry**:tooth:')

space()

col4, col5 = st.columns([0.7, 0.3], gap="large")
with col4:
    st.write('''
            ### The Power of Visual Understanding:
            **Experience cutting-edge instance segmentation 
            technology powered by the Mask R-CNN algorithm and implemented using the state-of-the-art Detectron2 framework.
            Our platform brings together the latest in deep learning and computer vision to provide accurate and efficient 
            object instance segmentation in images**
            ''')

    space()

    st.write('''
            ### Key Features:
            **Precise Instance Segmentation: Our model accurately identifies and delineates individual objects within images, providing pixel-level segmentation masks for each instance.
            Fast and Efficient: Powered by Detectron2, our solution leverages efficient backbone architectures for real-time or near-real-time instance segmentation without compromising accuracy.
            Easy to-Use Interface: Our user-friendly web interface allows you to upload your images and instantly see the results of instance segmentation, making it accessible to both experts and newcomers in the field.
            Interactive Visualization: Explore and interact with the segmented images using our intuitive visualization tools. Toggle between original and segmented views to understand the model's performance better.
            Customizable: Tailor the instance segmentation model to your specific use case by fine-tuning it on your dataset. Our platform provides guides and resources to help you adapt the model effectively.
            Scalable Deployment: Whether you're working on a personal project or an enterprise-level application, our model can be seamlessly integrated into your workflow with our deployment guides.**
            ''')
with col5:
    st.image('https://i.gifer.com/45RS.gif')

#https://media4.giphy.com/media/IhCzn4tK8JNxq82xtv/giphy.gif
#https://i.gifer.com/45RS.gif
#https://thumbs.gfycat.com/SandyHighlevelJaguar-max-1mb.gif
#https://media.giphy.com/media/Zap26z0mAZirZ7uDP1/giphy.gif

space()

# col_button = st.columns([0.9, 0.3, 0.9])[1]

with st.expander(":red[**Start the Journey**] :rocket:", expanded = False):
    uploaded_image = st.file_uploader("Drop X-ray", type=["jpg", "jpeg", "png"])
    c1, c2, c3 = st.columns([0.3, 0.4, 0.3])
    with c2:
        if uploaded_image:
            st.image(uploaded_image, caption= 'Uploaded Image', use_column_width=True)
            if st.button('Process Image', use_container_width=True):
                with st.spinner("Processing..."):
                    response = requests.post('http://localhost:8000/Predict', files={'file':uploaded_image})
                if response.status_code == 200:
                    st.success('Image Processed Successfully!')
                    out = Image.open(BytesIO(response.content))
                    st.image(out, caption= 'Processed Image', use_column_width=True)
                else:
                    st.error('Error Processing the image.')
st.markdown("""
            ## You can access to the code and every thing on this github repo feel free to give me your feedback &nbsp;&nbsp; \
            [<img alt="alt_text" width="60px" src="https://seeklogo.com/images/G/github-logo-5F384D0265-seeklogo.com.png" />](https://github.com/Bassem-2000/MaskRCNN-for-Tooth-Dentistry)
            """, unsafe_allow_html=True)

st.markdown(""" <style>
.css-ffhzg2{background-image: url("https://images.pond5.com/transparent-scull-and-teeth-xray-footage-070329948_prevstill.jpeg");
background-repeat: no-repeat;
background-size: cover;
}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style> """, unsafe_allow_html=True
)
