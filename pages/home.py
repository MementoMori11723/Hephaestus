import streamlit as st
from components.common import Footer
from components.home import Culture, Explore, Hero, About, Personalize

try:
    Hero(
        st.container(
            height=500
        )
    )
    About(
        st.container(
            height=600
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
            height=550
        )
    )
    Footer()
except Exception as e:
    raise e
