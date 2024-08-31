from streamlit_option_menu import option_menu
import streamlit as st

class Navbar:
    
    def __init__(self, default_index=0, orientation="horizontal"):
        self.options = ["Home", "About", "Contact", "Installation"]
        self.icons = ["house", "info-circle", "envelope"]
        self.menu_icon = "cast"
        self.default_index = default_index
        self.orientation = orientation

    def display(self):
        return option_menu(
            menu_title=None,  
            options=self.options, 
            icons=self.icons,  
            menu_icon=self.menu_icon,  
            default_index=self.default_index,  
            orientation=self.orientation,  
        )

    def navigate(self, selected_option, page):

        if page == 'Home':
            if selected_option == "About":
                st.switch_page('pages/1-about.py')
            elif selected_option == "Contact":
                st.switch_page('pages/2-contact.py')

        elif page == 'About': 
            if selected_option == "Home":
                st.switch_page('index.py')
            elif selected_option == "Contact":
                st.switch_page('pages/2-contact.py')

        elif page == 'Contact': 
            if selected_option == "Home":
                st.switch_page('index.py')
            if selected_option == "About":
                st.switch_page('pages/1-about.py')
