import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def footer() -> None:
    st.divider()
    st.write(
        "<div style='text-align: center;'>"
        "© 2025 <b>YourStory</b> | Made with ❤️ by <b>Hephaestus</b><br><br>"
        "<span style='font-size: 1.2em;'>Powered by </span><br>"
        "<img src='https://ometis.co.uk/hubfs/Snowflake%202.png' alt='Snowflake' height='100' width='175'></img>"
        "</div>",
        unsafe_allow_html=True
    )


def side_footer() -> None:
    st.sidebar.divider()
    st.sidebar.markdown("## 🇮🇳 YourStory")
    st.sidebar.caption("✨ Discover. Experience. Share.")
    st.sidebar.divider()
    st.sidebar.subheader("Contact me")
    col1, col2, col3 = st.sidebar.columns(3, border=True)
    col1.write("[![Github](https://img.icons8.com/m_outlined/512/github.png)](https://github.com/MementoMori11723)")
    col1.write("###### Github")
    col2.write("[![Portfolio](https://yasasvi.site/assets/img/favicon.webp)](https://yasasvi.site/)")
    col2.write("###### Portfolio")
    col3.write("[![Email](https://w7.pngwing.com/pngs/122/880/png-transparent-letter-mail-mailing-email-mailbox-inbox.png)](mailto:contact@yasasvi.site)")
    col3.write("###### Email")
    st.sidebar.divider()
    st.sidebar.markdown("🌐 Made with ❤️ by **Hephaestus**")
    st.sidebar.caption("🧊 Powered by Snowflake")


def Layout() -> tuple[DeltaGenerator, DeltaGenerator]:
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
