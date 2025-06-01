import pandas as pd
import streamlit as st
from geopy.geocoders import Nominatim
from streamlit.delta_generator import DeltaGenerator

from data import api


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

    c.header("Different Artworks in india")
    section(
        {
            "Name": "Gond Art",
            "Field": "gond",
            "Desc": "Gond art is a vibrant and expressive form of folk art practiced by the Gond people, one of the largest tribal groups in India, primarily in Madhya Pradesh. It's known for its use of natural pigments, detailed depictions of nature and mythology, and intricate dot and line patterns.",
        }
    )
    section(
        {
            "Name": "Kalighat Art",
            "Field": "kalighat",
            "Desc": "Kalighat painting is a traditional art form from West Bengal, India, known for its vibrant colors, simplified forms, and strong lines. It originated in the mid-19th century near the Kalighat Kali Temple in Kolkata and was created by Patua artists, who were itinerant storytellers.",
        }
    )
    section(
        {
            "Name": "Kangra Art",
            "Field": "kangra",
            "Desc": "Kangra painting, also known as Kangra miniature painting, is a school of Pahari (hill) painting that originated in the Kangra region of Himachal Pradesh, India. This art form developed in the 18th century and is characterized by its delicate brushwork, vivid colors, and depiction of themes from Hindu mythology, particularly the love stories of Radha and Krishna.",
        }
    )
    section(
        {
            "Name": "Kerala Mural",
            "Field": "kerala-mural",
            "Desc": "Kerala mural paintings are a vibrant and traditional form of wall art found in temples and palaces throughout the state of Kerala, India. They are known for their intricate detailing, use of natural pigments, and depiction of scenes from Hindu mythology and epics like the Ramayana and Mahabharata.",
        }
    )
    section(
        {
            "Name": "Madhubani Art",
            "Field": "madhubani",
            "Desc": "Madhubani art, also known as Mithila painting, is a vibrant and intricate style of folk art from the Mithila region of Bihar, India. It's characterized by bright colors, geometric patterns, and the use of natural dyes and pigments. ",
        }
    )
    section(
        {
            "Name": "Mandana Art",
            "Field": "mandana",
            "Desc": "Mandana art is a traditional tribal art form from Madhya Pradesh and Rajasthan, primarily practiced by the Meena community. It involves creating paintings on walls and floors of homes, often using natural materials like clay, cow dung, and red ochre (geru). The art is a form of decoration and is used to mark auspicious occasions like births, weddings, and festivals, as well as to ward off evil spirits and invite good fortune. ",
        }
    )
    section(
        {
            "Name": "Pichwai Art",
            "Field": "pichwai",
            "Desc": "Pichwai art is a traditional painting style from Rajasthan, India, particularly known for its depiction of Lord Krishna and his life, These paintings, typically on cloth, are vibrant, detailed, and often used as devotional art in temples and homes. They are characterized by intricate floral motifs, bright natural colors, and a distinct style related to the town of Nathdwara.",
        }
    )
    section(
        {
            "Name": "Warli Art",
            "Field": "warli",
            "Desc": "Warli art is a traditional Indian folk art form from the Warli tribe in Maharashtra, known for its use of simple, geometric shapes and depictions of daily life, rituals, and nature. It's characterized by its minimalist graphic vocabulary, featuring circles, triangles, squares, and lines, often painted in white against a brown or red background.",
        }
    )
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
    columns = c.columns(5, gap="medium", border=True)
    for i, column in enumerate(columns):
        con = column.container(height=250, border=False)
        con.image(
            recomendations.iloc[i]["image-url"],
            caption=recomendations.iloc[i]["TranslatedRecipeName"],
        )
        if column.button("View Recipe", key=f"f-{i}-button", use_container_width=True):
            flavors_popup(
                {
                    "Name": recomendations.iloc[i]["TranslatedRecipeName"],
                    "Image": recomendations.iloc[i]["image-url"],
                    "url": recomendations.iloc[i]["URL"],
                    "items": ", ".join(
                        word.strip().capitalize()
                        for word in recomendations.iloc[i]["Cleaned-Ingredients"].split(
                            ","
                        )
                    ),
                    "cuisine": recomendations.iloc[i]["Cuisine"],
                    "instructions": recomendations.iloc[i]["TranslatedInstructions"],
                }
            )

    c.divider()


def Places(c: DeltaGenerator) -> None:
    @st.dialog("Place", width="large")
    def places_popup(data: dict) -> None:
        st.header(data["data"]["place_name"])
        st.warning(
            "Sometimes the map might choose the city rather then the place itself!"
        )
        geolocator = Nominatim(user_agent="streamlit_map_app")
        location = geolocator.geocode(f"{data['data']["place_name"]}, india")
        if location == None:
            location = geolocator.geocode(f"{data['data']["city"]}")
        df = pd.DataFrame({"lat": [location.latitude], "lon": [location.longitude]})
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
    geolocator = Nominatim(user_agent="streamlit_map_app")
    location = geolocator.geocode(f"{filter_data.iloc[0]["place_name"]}, india")
    if location == None:
        location = geolocator.geocode(f"{filter_data.iloc[0]["city"]}")
    df = pd.DataFrame({"lat": [location.latitude], "lon": [location.longitude]})
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

    c.divider()
