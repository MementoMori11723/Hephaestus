import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data.api import Top_videos


def Sidebar(c: DeltaGenerator) -> None:
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
        "There is a saying that goes, They say a way to a man's heart is through his stomach, and what better way to understand india than cooking their food!"
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
