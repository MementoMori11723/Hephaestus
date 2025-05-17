import streamlit as st

st.set_page_config(
    page_title="Hephaestus",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

routes, pages = {
    "Home": "pages/home.py",
    "About": "pages/about.py",
}, []

for route, path in routes.items():
    isHome = True if route == "Home" else False
    pages.append(
        st.Page(
            path, title=route,
            default=isHome
        )
    )

navigation = st.navigation(pages=pages)
navigation.run()
