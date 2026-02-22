import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state == "home":
    st.title("home")
    st.write("Welcome to the Empire Game")
    if st.button("Start"):
        st.session_state = "settings"
        st.rerun()
elif st.session_state == "settings":
    st.title("settings")
    st.write("Please enter settings of your game")