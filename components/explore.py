import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data import api
from data.analysis import Location


def Sidebar(c: DeltaGenerator) -> None:
    @st.dialog("sidebar-popup", width="large")
    def sidebar_popup(link: str) -> None:
        st.video(link)

    data = api.Dance()
    option = c.selectbox("Different types of dance", data.keys())
    c.image(data[option]["img"], use_container_width=True)
    c.write(data[option]["info"])
    if c.button("Click for preview", use_container_width=True):
        sidebar_popup(data[option]["url"])


def Others(c: DeltaGenerator) -> None:
    c.header("Find More Information Here")
    e = c.expander("More Resoures", expanded=True)
    e.write(
        "- [Buy Indian Dresses & Indian Clothes Online - Panash India](https://www.panashindia.com/sale-promotions)"
    )
    e.write(
        "- [Places to visit in India](https://www.makemytrip.com/tripideas/places-to-visit-in-india)"
    )
    e.write("- [Best recipes of India](https://bestrecipesofindia.com/)")
    e.write("- [Incredible India](https://www.incredibleindia.gov.in/en)")
    e.write("- [History of India](https://en.wikipedia.org/wiki/History_of_India)")


def Artwork(c: DeltaGenerator) -> None:
    def section(data: dict):
        c.subheader(data["Name"])
        c.write(data["Desc"])
        columns = c.columns(5, gap="small", vertical_alignment="center")
        for i, column in enumerate(columns):
            column.image(
                f"./static/{data['Field']}/{i+1}.jpg", use_container_width=True
            )

    paintings = api.Painting()
    c.header("Different Artworks in india")
    section(paintings[0])
    section(paintings[1])
    section(paintings[2])
    section(paintings[3])
    section(paintings[4])
    section(paintings[5])
    section(paintings[6])
    section(paintings[7])
    c.divider()


def Flavors(c: DeltaGenerator) -> None:
    @st.dialog("Recipe", width="large")
    def flavors_popup(data: dict) -> None:
        st.image(data["Image"], caption=data["Name"])

        st.header(data["Name"])
        st.write(f"- **Cusine**: {data["cuisine"]}")
        st.write("#### Ingredients: ")
        st.write(data["items"])

        st.write("#### Instructions")
        st.write(data["instructions"])
        st.link_button(
            "Click here to view the full recipes",
            url=data["url"],
            type="primary",
            use_container_width=True,
        )

    c.header("Different Recipes in india")
    c.subheader("Over 4000+ recipes over here!")
    c.write(
        "They say the way to a man's heart is through his stomach — and what better way to understand India than by cooking and savoring its rich, flavorful dishes? 🇮🇳"
    )

    flavor = api.Flavors()
    flavor_sorted = flavor.sort_values(by="TranslatedRecipeName")
    search = c.selectbox("Search", flavor_sorted["TranslatedRecipeName"].unique())

    filter_data = flavor_sorted[flavor_sorted["TranslatedRecipeName"] == search]

    col1, col2 = c.columns(2, gap="medium", border=True)
    col1.image(
        f"{filter_data.iloc[0]["image-url"]}", caption=search, use_container_width=True
    )
    col1.link_button(
        "Click here to view the full recipes",
        url=filter_data.iloc[0]["URL"],
        type="primary",
        use_container_width=True,
    )

    col2.header(search)
    col2.write(f"- **Cusine**: {filter_data.iloc[0]["Cuisine"]}")
    col2.write("#### Ingredients: ")
    res = ", ".join(
        word.strip().capitalize()
        for word in filter_data.iloc[0]["Cleaned-Ingredients"].split(",")
    )
    col2.write(res)

    col2.write("#### Instructions")
    col2.write(filter_data.iloc[0]["TranslatedInstructions"])

    is_veg = filter_data.iloc[0]["is_vegetarian"]
    cuisine = filter_data.iloc[0]["Cuisine"]
    recomendations = (
        flavor_sorted[
            (
                (flavor_sorted["is_vegetarian"] == is_veg)
                & (flavor_sorted["Cuisine"] == cuisine)
            )
            & (
                flavor_sorted["TranslatedInstructions"]
                != filter_data.iloc[0]["TranslatedInstructions"]
            )
        ]
        .tail(5)
        .reset_index()
    )
    c.subheader("Recommendations")
    if len(recomendations) >= 5:
        columns = c.columns(5, gap="medium", border=True)
        for i, column in enumerate(columns):
            con = column.container(height=250, border=False)
            con.image(
                recomendations.iloc[i]["image-url"],
                caption=recomendations.iloc[i]["TranslatedRecipeName"],
            )
            if column.button(
                "View Recipe", key=f"f-{i}-button", use_container_width=True
            ):
                flavors_popup(
                    {
                        "Name": recomendations.iloc[i]["TranslatedRecipeName"],
                        "Image": recomendations.iloc[i]["image-url"],
                        "url": recomendations.iloc[i]["URL"],
                        "items": ", ".join(
                            word.strip().capitalize()
                            for word in recomendations.iloc[i][
                                "Cleaned-Ingredients"
                            ].split(",")
                        ),
                        "cuisine": recomendations.iloc[i]["Cuisine"],
                        "instructions": recomendations.iloc[i][
                            "TranslatedInstructions"
                        ],
                    }
                )
    else:
        c.write("No recommendations found!")

    c.divider()


def Places(c: DeltaGenerator) -> None:
    @st.dialog("Place", width="large")
    def places_popup(data: dict) -> None:
        st.header(data["data"]["place_name"])
        st.warning(
            "Sometimes the map might choose the city rather then the place itself!"
        )
        df = Location(data)
        st.map(df)
        st.write(f"- **City**: {data['data']['city']}")
        st.write(f"- **State**: {data['data']['state']}")
        st.write(f"- **Zone**: {data['data']['zone']}")
        st.write(f"- **Type**: {data['data']['type']}")
        st.write(f"- **Established Year**: {data['data']['established_year']}")
        st.write(f"- **Rating**: {data['data']['rating']}")
        st.write(f"- **Significance**: {data['data']['significance']}")
        st.write(f"- **Is Camera allowed ?**: {data['data']['dslr_allowed']}")
        st.write(f"- **Best time**: {data['data']['best_time_text']}")
        st.write(f"- **Weekly off**: {data['data']['weekly_off']}")

    c.header("Different Places to visit in india")
    c.subheader("Over 350+ places in india over here!")
    c.write(
        "They say the soul of a country lies in its landscapes — and what better way to discover India than by exploring its iconic landmarks and hidden gems, each telling a story of its own? 🇮🇳"
    )
    places = api.Tourist_places()
    places = places.sort_values(by=["significance", "rating"], ascending=False)
    search = c.selectbox("Search", places["place_name"].unique())
    filter_data = places[places["place_name"] == search]
    df = Location({
        "data":{
            "place_name": filter_data.iloc[0]['place_name'],
            "city": filter_data.iloc[0]["city"],
        }
    })

    col1, col2 = c.columns(2, gap="medium", border=True)
    col1.write("#### Map of the location")
    col1.warning("Sometimes it might choose the city rather then the place itself!")
    col1.map(df, use_container_width=True)

    col2.header(filter_data.iloc[0]["place_name"])
    col2.write(f"- **City**: {filter_data.iloc[0]['city']}")
    col2.write(f"- **State**: {filter_data.iloc[0]['state']}")
    col2.write(f"- **Zone**: {filter_data.iloc[0]['zone']}")
    col2.write(f"- **Type**: {filter_data.iloc[0]['type']}")
    col2.write(f"- **Established Year**: {filter_data.iloc[0]['established_year']}")
    col2.write(f"- **Rating**: {filter_data.iloc[0]['rating']}")
    col2.write(f"- **Significance**: {filter_data.iloc[0]['significance']}")
    col2.write(f"- **Is Camera allowed ?**: {filter_data.iloc[0]['dslr_allowed']}")
    col2.write(f"- **Best time**: {filter_data.iloc[0]['best_time_text']}")
    col2.write(f"- **Weekly off**: {filter_data.iloc[0]['weekly_off']}")

    c.subheader("Recommendations")
    recomendations = (
        places[
            (
                (places["type"] == filter_data.iloc[0]["type"])
                | (places["state"] == filter_data.iloc[0]["state"])
                & (places["significance"] == filter_data.iloc[0]["significance"])
            )
            & (
                (3 <= places["rating"])
                & (places["rating"] <= filter_data.iloc[0]["rating"])
            )
        ]
        .tail(5)
        .reset_index()
    )
    if len(recomendations) >= 5:
        columns = c.columns(5, gap="medium", border=True)
        for i, column in enumerate(columns):
            column.write(recomendations.iloc[i]["place_name"])

            if column.button(
                "View more details",
                key=f"p{i}-button",
                use_container_width=True,
                type="primary",
            ):
                places_popup(
                    {
                        "data": recomendations.iloc[i],
                    }
                )
    else:
        c.write("No recommendations found!")

    c.divider()
