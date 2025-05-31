import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def Hero(c: DeltaGenerator):
    c.title("YourStory - Hackathon | by snowflake")
    c.write("By Hephaestus team")
    c.divider()
    c.header("Discover the Soul of India!")
    c.write(
        "From ancient traditions to modern expressions, experience the heartbeat of India like never before."
    )
    if c.button("Start Your Journey &#8594;"):
        st.switch_page("pages/personalize.py")
    c.divider()


def About(c: DeltaGenerator):
    c.header("Why Indian Culture?")
    c.write(
        "India is more than a country — it’s a living mosaic of languages, festivals, philosophies, and stories that have shaped the world for thousands of years. This platform is a tribute to its timeless traditions, colorful diversity, and modern vibrance. Whether you’re here to learn, explore, or reconnect, welcome to the journey."
    )
    if c.button("Learn More About Us &#8594;"):
        st.switch_page("pages/about.py")
    c.divider()


def Personalize(c: DeltaGenerator):
    c.header("Make It Yours")
    c.write(
        "Want to explore culture based on your interests? Whether it's music, food, spirituality, or festivals, we'll craft your cultural journey just for you."
    )
    if c.button("Personalize My Journey &#8594;"):
        st.switch_page("pages/personalize.py")
    c.divider()


def Culture(c: DeltaGenerator):
    c.header("A Tapestry of Traditions")
    c.write(
        "Dive into India’s rich culture — from ancient temples to Bollywood beats, from yoga to vibrant crafts. Explore art, cuisine, history, and daily life across every state and region."
    )
    if c.button("Explore Indian Culture &#8594;"):
        st.switch_page("pages/culture.py")
    c.divider()


def Explore(c: DeltaGenerator):
    c.header("Experience India, One Story at a Time")
    c.write(
        "Explore iconic places, discover lesser-known gems, and uncover real stories from people who live the culture every day. Your window into India’s living heritage awaits."
    )
    if c.button("Start Exploring &#8594;"):
        st.switch_page("pages/explore.py")


def Sidebar(c: DeltaGenerator):
    c.write("## Open link in new tab")
    c.link_button("Go to Home page &#8599;", "/", use_container_width=True)
    c.link_button("Go to About page &#8599;", "/about", use_container_width=True)
    c.link_button(
        "Go to Personalize page &#8599;", "/personalize", use_container_width=True
    )
    c.link_button("Go to Culture page &#8599;", "/culture", use_container_width=True)
    c.link_button("Go to Explore page &#8599;", "/explore", use_container_width=True)
