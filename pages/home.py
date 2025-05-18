import streamlit as st
from components.common import navbar, footer
from utils.analysis import analyse

navbar()
st.write("Home Page!")
st.json(analyse())
footer()
