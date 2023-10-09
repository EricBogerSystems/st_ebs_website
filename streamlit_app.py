import streamlit as st
from streamlit_option_menu import option_menu

# Streamlit page config
st.set_page_config(page_title="EricBogerSystems", page_icon="🖥️", layout="wide")

# Use local CSS file style.css
with open("style/style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# Sidebar Menu
st.sidebar.image("data/ebs_logo.png",caption="Developed and Maintaned by Eric Boger")
with st.sidebar:
    menu_selected = option_menu(
        menu_title="MENU", 
        menu_icon="cast",
        options=[ "Home", "Projects", "Contact" ],
        icons=[ "house" , "book" , "envelope" ],
        default_index=0,
        orientation="vertical",  # horizontal
    )

#
# Home Page
#
if menu_selected == "Home":
    st.title("Home")
    st.subheader("... under construction ...")

#
# Projects Page
#
if menu_selected == "Projects":
    st.title("Projects")
    st.subheader("... I'm ready for your project ...")

#
# Contact Page
#
if menu_selected == "Contact":
    st.title("Contact")
    st.subheader("EricBogerSystems")

    st.text("info@ericbogersystems.com")
    
    link_linkedin="[LinkedIn](https://de.linkedin.com/in/eric-boger-69022bba)"
    st.markdown(link_linkedin,unsafe_allow_html=True)

    link_xing="[XING](https://www.xing.com/profile/Eric_Boger2)"
    st.markdown(link_xing,unsafe_allow_html=True)

