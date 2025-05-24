import streamlit as st
from streamlit.delta_generator import DeltaGenerator

def Quiz(main:DeltaGenerator) -> None:
    with main.expander("Test-1", True):
        if main.button("test-2"):
            test_2()

@st.dialog("Test-2", width="large")
def test_2() -> None:
    st.write("This is test-2")
    if st.button("Is working?"):
        with st.expander("It is working..."):
            st.write("Test worked!")
