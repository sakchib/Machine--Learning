import streamlit as st
from streamlit_option_menu import option_menu

# Create an option menu
with st.sidebar:  # You can also place it in the main app
    selected = option_menu(
        menu_title="Main Menu",  # Title of the menu
        options=["Home", "About", "Contact"],  # Menu options
        icons=["house", "info-circle", "envelope"],  # Icons from https://icons.getbootstrap.com/
        menu_icon="cast",  # Icon for the menu
        default_index=0,  # Default selected option
    )

# Display content based on selected menu
if selected == "Home":
    st.title("Welcome to Home Page")
elif selected == "About":
    st.title("About Us")
    st.write("This is the About page.")
elif selected == "Contact":
    st.title("Contact Us")
    st.write("Here is how you can contact us!")
