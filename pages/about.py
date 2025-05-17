import streamlit as st
from pages.components.navbar import run as navbar
from pages.components.footer import run as footer

navbar()
st.write("About Page!")
footer()
