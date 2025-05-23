import streamlit as st
from components.common import Footer

@st.dialog("Test-2", width="large")
def test_2():
    st.write("This is test-2")
    if st.button("Is working?"):
        with st.expander("It is working..."):
            Footer()

with st.expander("Test-1", True):
    if st.button("test-2"):
        test_2()

Footer()
