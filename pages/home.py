import streamlit as st
from components.common import Navbar, Footer
from components.home import Culture, Explore, Hero, About, Personalize

try:
    Navbar()
    Hero(
        st.container(
            height=500
        )
    )
    About(
        st.container(
            height=500
        )
    )
    Personalize(
        st.container(
            height=500
        )
    )
    Culture(
        st.container(
            height=500
        )
    )
    Explore(
        st.container(
            height=500
        )
    )
    Footer()
except Exception as e:
    raise e
