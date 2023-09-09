import streamlit as st

st.title("Contact Me")
st.write("### Feel free to reach out to me for any inquiries or feedback!")

name = st.text_input("**Your Name**", "")
email = st.text_input("**Your Email**", "")
message = st.text_area("**Message**", "")

if st.button("Submit"):
    if name and email and message:
        # For example, sending an email or storing the form data in a database
        st.success("Message sent successfully!")
    else:
        st.warning("Please fill out all fields.")
st.write("""

# Social Contacts
         
         """)
logos = """
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Whatsapp2_colored_svg-512.png" />](https://wa.me/+201006491306)
&nbsp;
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Linkedin_unofficial_colored_svg-512.png" />](https://www.linkedin.com/in/bassem-ahmed-ahmed/)
&nbsp;
[<img alt="alt_text" width="30px" height="40px" src="https://cdn4.iconfinder.com/data/icons/social-media-logos-6/512/112-gmail_email_mail-256.png" />](mailto:bassemahmed.am@gmail.com)
[<img alt="alt_text" width="30px" src="https://cdn2.iconfinder.com/data/icons/social-media-2285/512/1_Facebook2_colored_svg-512.png" />](https://www.facebook.com/bassem.ahmed.7712/)
[<img alt="alt_text" width="35px" height="35px" src="https://seeklogo.com/images/G/github-logo-9BBCA663A4-seeklogo.com.png" />](https://github.com/Bassem-2000)
"""
       
st.markdown(logos, unsafe_allow_html=True)
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