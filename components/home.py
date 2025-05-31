import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def Hero(c: DeltaGenerator):
    c.title("Discover the Soul of India")
    c.markdown(
        """
        From _ancient traditions_ to _modern expressions_, experience the **heartbeat of India** like never before.

        Let your journey unfold through rich **colors**, **sounds**, **flavors**, and **stories** that have shaped a civilization for millennia.
        """
    )

    if c.button("Start Exploring →", type="primary"):
        st.switch_page("pages/culture.py")

    c.divider()


def About(c: DeltaGenerator):
    c.subheader("Why Indian Culture?")
    c.markdown(
        """
        India is more than a country — it’s a **living mosaic** of languages, festivals, philosophies, and artistic traditions.

        With over **4,000 years of recorded history**, India's contributions to global thought, science, and culture are profound. This platform is a tribute to its **timeless heritage**, **diverse people**, and **modern vibrancy**.
        """
    )

    if c.button("Learn More About Us →", type="tertiary"):
        st.switch_page("pages/about.py")


def Personalize(c: DeltaGenerator):
    c.subheader("Not sure where to begin?")
    c.markdown(
        "Make It Yours, Let us help you **craft a personalized journey** based on your interests and preferences."
    )

    c.markdown(
        """
        Want to explore culture based on what excites you most? Whether it's **music**, **food**, **spirituality**, or **festivals**, we’ll create a journey tailored to your interests.

        - Choose your focus: art, history, cuisine, traditions
        - Receive curated suggestions across states and seasons
        - Get inspired by real stories and meaningful insights
        """
    )

    if c.button("Customize My Journey →", type="tertiary"):
        st.switch_page("pages/personalize.py")

    c.divider()


def Culture(c: DeltaGenerator):
    c.subheader("A Tapestry of Traditions")
    c.markdown(
        """
        Discover how ancient rituals coexist with contemporary innovation. From **yoga and temple architecture** to **Bollywood cinema** and **modern design**, Indian culture is layered, dynamic, and ever-evolving.

        - Explore regional crafts, dance forms, and musical traditions
        - Learn about cultural festivals and seasonal rituals
        - Dive into food culture, from street snacks to royal cuisine
        """
    )

    if c.button("Explore Indian Culture →", type="tertiary"):
        st.switch_page("pages/culture.py")

    c.divider()


def Explore(c: DeltaGenerator):
    c.subheader("Experience India, One Story at a Time")
    c.markdown(
        """
        Go beyond landmarks — explore the **people, history, and everyday life** that give meaning to each place.

        - Discover iconic sites and hidden gems across the country
        - Read authentic stories from locals, artists, and travelers
        - Understand the deeper significance behind cultural practices
        """
    )

    if c.button("Start Exploring →", type="tertiary"):
        st.switch_page("pages/explore.py")

    c.divider()


def Sidebar(c: DeltaGenerator):
    c.subheader("Quick Navigation")
    c.markdown("Use the links below to jump directly to each section:")

    c.link_button("Home Page ↗", "/", use_container_width=True)
    c.link_button("About Us ↗", "/about", use_container_width=True)
    c.link_button("Personalize ↗", "/personalize", use_container_width=True)
    c.link_button("Culture Hub ↗", "/culture", use_container_width=True)
    c.link_button("Explore ↗", "/explore", use_container_width=True)

    c.markdown("---")
    c.markdown(
        "**Tip:** Bookmark the pages you're most interested in for easy reference during your journey."
    )
