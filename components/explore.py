import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data.api import Top_videos


def Sidebar(c: DeltaGenerator) -> None:
    @st.dialog("sidebar-popup", width="large")
    def sidebar_popup(link: str) -> None:
        st.video(link)

    data = {
        "Manipuri": {
            "img": "https://i0.wp.com/darshanajhaveri.com/wp-content/uploads/2018/11/image_33-e1543396552578.jpg?resize=303%2C447",
            "url": "https://youtu.be/HzqQjdCSmuY",
            "info": "Manipuri dance, also known as Jagoi or Manipuri Raas Leela, is one of India's classical dance forms, originating from the state of Manipur.",
        },
        "Bharatanatyam": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/Bharata_Natyam_Performance_DS.jpg/330px-Bharata_Natyam_Performance_DS.jpg",
            "url": "https://youtu.be/YuxLEc2JqnE",
            "info": "Bharatanatyam is a classical Indian dance form from Tamil Nadu, known for its storytelling through intricate hand gestures, facial expressions, and rhythmic footwork.",
        },
        "Odissi": {
            "img": "https://lipsasatapathy.com/wp-content/uploads/2023/12/27973802_10155274930011475_6775249791606593842_n.jpg",
            "url": "https://youtu.be/LUHrTwrC3wU",
            "info": "Odissi dance is a classical Indian dance form originating from the state of Odisha.",
        },
        "Kathakali": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Kathakali_BNC.jpg/250px-Kathakali_BNC.jpg",
            "url": "https://youtu.be/GBbcYtkqVKQ",
            "info": "Kathakali is a classical Indian dance-drama form from Kerala, known for its stylized acting, intricate costumes, and vibrant makeup.",
        },
        "Kathak": {
            "img": "https://www.drishtiias.com/images/uploads/1579336257_image4.jpg",
            "url": "https://youtu.be/UBYqv21c0Yk",
            "info": "Kathak is one of the eight major forms of Indian classical dance. Its origin is attributed to the traveling bards in ancient northern India known as Kathakar",
        },
        "Sattriya": {
            "img": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkCHh7Ta2bWBau8reOoepbbgu9-eeldC-apw&s",
            "url": "https://youtu.be/-123CQlpqBY",
            "info": "Sattriya is a classical Indian dance form from Assam, India, with strong roots in neo-Vaishnavism.",
        },
        "Kuchipudi": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Indian_Dancer_%28Malabika_Sen%29.jpg/250px-Indian_Dancer_%28Malabika_Sen%29.jpg",
            "url": "https://youtu.be/tyTOe1wabgM",
            "info": "Kuchipudi is a classical Indian dance-drama form originating from the village of Kuchipudi in Andhra Pradesh, India.",
        },
        "Mohiniyattam": {
            "img": "https://upload.wikimedia.org/wikipedia/commons/8/8d/Mohiniyattom_performance.jpg",
            "url": "https://youtu.be/Fl3g-RUYE3w",
            "info": "Mohiniyattam is a classical Indian dance form originating from Kerala, known for its graceful and feminine movements.",
        },
    }
    option = c.selectbox("Different types of dance", data.keys())
    c.image(data[option]["img"], use_container_width=True)
    c.write(data[option]["info"])
    if c.button("Click for preview", use_container_width=True):
        sidebar_popup(data[option]["url"])


def Others(c: DeltaGenerator) -> None:
    c.header("Find More")
    c.write(
        "- [Buy Indian Dresses & Indian Clothes Online - Panash India](https://www.panashindia.com/sale-promotions)"
    )
    c.write(
        "- [Places to visit in India](https://www.makemytrip.com/tripideas/places-to-visit-in-india)"
    )
    c.write("- [Best recipes of India](https://bestrecipesofindia.com/)")
    c.write("- [Incredible India](https://www.incredibleindia.gov.in/en)")
    c.write("- [History of India](https://en.wikipedia.org/wiki/History_of_India)")


def Flavors(c: DeltaGenerator) -> None:
    @st.dialog("flavors-popup", width="large")
    def flavors_popup(data: str) -> None:
        st.write(data)

    c.header("Explore")
    c.write(
        "They say the way to a man's heart is through his stomach — and what better way to understand India than by cooking and savoring its rich, flavorful dishes? 🇮🇳"
    )
    c.divider()

    c.subheader("Top Flavors in india")
    columns = c.columns(5, gap="medium")

    for i, column in enumerate(columns):
        column.image(
            "https://www.shutterstock.com/shutterstock/photos/2286554497/display_1500/stock-photo-random-pictures-cute-and-funny-2286554497.jpg"
        )
        column.write("This is a column")
        if column.button("Pop-up", key=f"f{i}-button", use_container_width=True):
            flavors_popup(f"This is some random data by {i+1}!")

    expander = c.expander("Find more recipes here", expanded=False)
    for x in range(10):
        sub_columns = expander.columns(5, gap="medium")
        for i, column in enumerate(sub_columns):
            column.image(
                "https://www.shutterstock.com/shutterstock/photos/2286554497/display_1500/stock-photo-random-pictures-cute-and-funny-2286554497.jpg"
            )
            column.write("This is a sub column")
            if column.button("Pop-up", key=f"f{x} - {i}", use_container_width=True):
                flavors_popup(
                    f"This is some random data from sub_columns by {x} - {i}!"
                )

    c.divider()


def Places(c: DeltaGenerator) -> None:
    @st.dialog("places-popup", width="large")
    def places_popup(data: str) -> None:
        st.write(data)

    c.subheader("Top Places in india")
    columns = c.columns(5, gap="medium")

    for i, column in enumerate(columns):
        column.image(
            "https://www.shutterstock.com/shutterstock/photos/2286554497/display_1500/stock-photo-random-pictures-cute-and-funny-2286554497.jpg"
        )
        column.write("This is a column")
        if column.button("Pop-up", key=f"p{i}-button", use_container_width=True):
            places_popup(f"This is some random data by {i+1}!")

    expander = c.expander("Find more recipes here", expanded=True)
    for x in range(5):
        sub_columns = expander.columns(5, gap="medium")
        for i, column in enumerate(sub_columns):
            column.image(
                "https://www.shutterstock.com/shutterstock/photos/2286554497/display_1500/stock-photo-random-pictures-cute-and-funny-2286554497.jpg"
            )
            column.write("This is a sub column")
            if column.button("Pop-up", key=f"p{x} - {i}", use_container_width=True):
                places_popup(f"This is some random data from sub_columns by {x} - {i}!")
