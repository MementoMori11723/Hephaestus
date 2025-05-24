import streamlit as st
from streamlit.delta_generator import DeltaGenerator

def navbar() -> None:
    pass

def footer() -> None:
    st.divider()
    st.write("This is footer!")

def side_footer() -> None:
    st.sidebar.divider()
    st.sidebar.write("This is sidebar footer!") 

def Layout() -> tuple[DeltaGenerator, DeltaGenerator]:
    # Navbar Sections
    navbar()
    # Main Sections
    main = st.columns(1)[0]
    # Footer Sections
    footer()
    # Sidebar's Main Sections
    side_main = st.sidebar.columns(1)[0]
    # Sidebar Footer
    side_footer()
    # Returning Main Layout's
    return main, side_main
