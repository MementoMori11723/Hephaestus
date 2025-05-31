import pandas as pd
import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data.api import Flavors, Top_videos, Tourist_places


# Main function for culture page
def Sidebar(c: DeltaGenerator) -> None:
    data = state_data()
    option = c.selectbox("Select a state", data.keys())
    if option:
        c.write(data[option])


# First section
def History(c: DeltaGenerator) -> None:
    c.header("Heritage of India")
    c.write(
        """India is not just a country; it is an experience — of resilience, diversity, and vibrant tradition. The Culture page invites you on a journey through the soulful melodies, flavorful dishes, breathtaking places, and the deep history that has shaped the India we know and love today."""
    )
    c.subheader("🛡️ **A Journey Through Struggles & Triumphs**")
    c.write(
        """From the Vedic age to the digital age, India’s story is written in perseverance.
Colonized for over two centuries, India fought tirelessly for its independence — a struggle led by brave hearts like Mahatma Gandhi, Rani Lakshmi Bai, Bhagat Singh, and countless unsung heroes.

Post-independence, the nation transformed rapidly — developing its space program, digital infrastructure, and global cultural influence, all while holding onto its roots.

> “At the stroke of the midnight hour, when the world sleeps, India will awake to life and freedom.”
> — Jawaharlal Nehru, 15 August 1947"""
    )

    c.subheader("Map of India")
    expander = c.expander("Map of india")
    df = pd.DataFrame({"lat": [20.5937], "lon": [78.9629]})

    expander.map(df, zoom=4)
    c.divider()


# Second section
def Music(c: DeltaGenerator) -> None:
    @st.dialog("music-pop-up", width="large")
    def music_popup(data: str) -> None:
        st.video(data)

    c.subheader("🎶 **Melodies That Define Generations: Bollywood’s Musical Legacy**")
    c.write(
        """Indian cinema is not complete without music. Songs in Bollywood aren't just interludes — they’re emotions, traditions, and movements. Here are some of the **most iconic hits** that define cultural eras:"""
    )
    music_data = Top_videos()
    top_music_data = music_data.head(5)
    top_music_image_links = [
        "https://i.ytimg.com/vi/BBAyRBTfsOU/maxresdefault.jpg",
        "https://i.ytimg.com/vi/sCbbMZ-q4-I/hq720.jpg?sqp=-oaymwEhCK4FEIIDSFryq4qpAxMIARUAAAAAGAElAADIQj0AgKJD&rs=AOn4CLBr9JZw3tZFFUtjz4grufpn65sJKw",
        "https://i.ytimg.com/vi/J6i5vTNk12g/maxresdefault.jpg",
        "https://i.ytimg.com/vi/JFcgOboQZ08/maxresdefault.jpg",
        "https://i.ytimg.com/vi/vu5-aKf_QqA/maxresdefault.jpg",
    ]
    top_music_video_links = [
        "https://youtu.be/BBAyRBTfsOU?si=1k3rrjYqRJWgGPBP",
        "https://youtu.be/sCbbMZ-q4-I?si=JRIVYlQhe7zrzxgl",
        "https://youtu.be/N2-HsIYd0Go?si=Eef-8mbUBS3IB8xo",
        "https://youtu.be/JFcgOboQZ08?si=5tHwaNBnyLe1ZPA2",
        "https://youtu.be/vu5-aKf_QqA?si=zk0AMOUiVSmdM-ST",
    ]
    top_columns = c.columns(5)
    for i in range(5):
        top_columns[i].image(
            top_music_image_links[i],
            caption=f"{top_music_data['title'][i]}",
            use_container_width=True,
        )
        if top_columns[i].button("Click to preview", key=i, use_container_width=True):
            music_popup(top_music_video_links[i])

    c.write("#### Take a peak at the data")
    m_expander = c.expander("Music Data", expanded=True)
    m_expander.bar_chart(
        music_data,
        x="title",
        y="view_count",
        color=["#138808"],
        x_label="Title",
        y_label="View Count",
    )

    c.write(
        "These songs echo from weddings to road trips, shaping India’s modern soundscape."
    )
    c.divider()


# Fourth section
def Most_visited(c: DeltaGenerator) -> None:
    c.subheader("🌍 **Top 5 Most Visited Places in India**")
    c.write(
        "India’s landscapes span snowy peaks to coastal sands. Its cultural landmarks attract millions:"
    )

    places_data = Tourist_places()
    places_data = places_data.sort_values(
        by=["rating", "google_reviews_lakh"], ascending=[False, False]
    )
    top_places = places_data.head(5).reset_index()
    top_places_image_links = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/The_Golden_Temple_of_Amrithsar_7.jpg/1200px-The_Golden_Temple_of_Amrithsar_7.jpg",
        "https://static.toiimg.com/photo/105293415.cms",
        "https://live.staticflickr.com/65535/52747273516_25f5597d09_b.jpg",
        "https://upload.wikimedia.org/wikipedia/commons/5/56/Kedarnath_Temple_in_Rainy_season.jpg",
        "https://www.mptourism.com/web/image/catalog/Blog%20Image/Mahakaleshwar.jpg",
    ]

    columns = c.columns(5)
    for i in range(5):
        columns[i].image(
            top_places_image_links[i],
            caption=f"{top_places["place_name"][i]}",
            use_container_width=True,
        )

    c.subheader("Take a peek at the data")
    p_expander = c.expander("Places Data", expanded=True)
    p_expander.write("#### Types of places vs Region")
    p_expander.bar_chart(
        places_data.head(30).sort_values(by="state", ascending=False),
        x="type",
        y="state",
        x_label="Type",
        y_label="State",
        color=["#FF7722"],
    )
    p_expander.write("#### Places vs Sigificance")
    p_expander.bar_chart(
        places_data.head(30),
        x="place_name",
        y="significance",
        x_label="Place Name",
        y_label="Significance",
        color=["#138808"],
    )

    c.write("Each location is a story, a flavor, a celebration of India’s soul.")
    c.divider()


# Third section
def Flavors_of_india(c: DeltaGenerator) -> None:
    c.subheader("🍛 **Famous Traditional Dishes of India**")
    c.write(
        "No cultural exploration is complete without tasting India’s diverse cuisine — where spices meet stories."
    )

    flavors_data = Flavors().sample(frac=1)
    top_recipes = (
        flavors_data.sort_values(
            by=["TotalTimeInMins", "Ingredient-count", "is_vegetarian"]
        )
        .sample(frac=1)
        .head(5)
    )

    columns = c.columns(5, gap="medium", vertical_alignment="bottom", border=True)
    for i in range(5):
        con = columns[i].container(height=320, border=False)
        con.image(
            top_recipes.iloc[i]["image-url"],
            caption=top_recipes.iloc[i]["TranslatedRecipeName"],
            use_container_width=True,
        )
        columns[i].link_button(
            "Click to view the recipe",
            url=top_recipes.iloc[i]["URL"],
            use_container_width=True,
        )

    c.subheader("Take a look at the data")
    f_expander = c.expander("Food Data", expanded=True)
    f_expander.write("#### ⏱️ Ingredients vs Preparation Time")
    f_expander.bar_chart(
        flavors_data.head(75),
        x="TranslatedRecipeName",
        y=["TotalTimeInMins", "Ingredient-count"],
        x_label="Recipe Name",
        y_label="Recipe Attributes",
        color=["#138808", "#FF7722"],
    )

    f_expander.write("#### 🥗 Vegetarian vs Non-Vegetarian Recipes")
    veg_counts = (
        flavors_data["is_vegetarian"]
        .value_counts()
        .reset_index()
        .replace({0: "Non-Vegetarian", 1: "Vegetarian"})
    )
    veg_counts.columns = ["is_vegetarian", "count"]
    f_expander.bar_chart(
        veg_counts,
        x="is_vegetarian",
        y="count",
        x_label="Is Vegetarian",
        y_label="Number of Recipes",
        color=["#312C6A"],
        horizontal=True,
    )

    c.write(
        "These dishes reflect regional traditions, seasonal ingredients, and centuries-old culinary wisdom."
    )
    c.divider()


# Final section
def Future(main: DeltaGenerator) -> None:
    main.subheader("🧭 **What Does It Mean to Be Indian Today?**")
    main.write(
        "Being Indian means finding unity in diversity — languages, religions, food, and fashion coexisting in harmony. It means celebrating Diwali and Eid in the same neighborhood, watching cricket together, and adding masala to both tea and conversation."
    )
    main.write(
        "India’s culture isn’t just preserved — it’s evolving. And through this website, you’re invited to explore it, taste it, and keep it alive."
    )


def state_data() -> dict[str, str]:
    return {
        "Jammu & Kashmir": """ 
        - Home to the world's only floating post office on Dal Lake in Srinagar.
        - The region boasts breathtaking landscapes, including the famous Dal Lake and the Himalayas.
        - Known for its rich handicrafts, especially Pashmina shawls and Kashmiri carpets.
        """,
        "Himachal Pradesh": """ 
        - Nicknamed "Dev Bhoomi" or "Land of the Gods" due to its numerous temples.
        - Home to the Great Himalayan National Park, a UNESCO World Heritage Site.
        - The state is known for its apple orchards, contributing significantly to India's apple production.
        """,
        "Delhi": """
        - Home to three UNESCO World Heritage Sites: Qutub Minar, Red Fort, and Humayun's Tomb.
        - The Delhi Metro is one of the largest and busiest metro networks in the world.
        - The city has a rich history, having been the capital of several empires.
        """,
        "Punjab": """ 
        - The Golden Temple in Amritsar is a major pilgrimage site for Sikhs worldwide.
        - Bhangra and Giddha are traditional dance forms originating from Punjab.
        - Known as the "Granary of India" due to its extensive wheat and rice production.
        """,
        "Haryana": """ 
        - The ancient city of Kurukshetra is believed to be the battlefield of the Mahabharata.
        - Home to the Sultanpur National Park, a bird watcher's paradise.
        - Known for its rich tradition in wrestling and producing many national-level athletes.
        """,
        "Uttarakhand": """ 
        - Hosts the Char Dham pilgrimage sites: Yamunotri, Gangotri, Kedarnath, and Badrinath.
        - The Jim Corbett National Park, India's first national park, is located here.
        - Known as the "Land of Gods" due to its numerous Hindu temples and pilgrimage centers.
        """,
        "Uttar Pradesh": """ 
        - Home to the iconic Taj Mahal in Agra, one of the Seven Wonders of the World.
        - Varanasi, one of the world's oldest inhabited cities, is located here.
        - The state has a rich tradition in classical music and dance, including Kathak.
        """,
        "Madhya Pradesh": """ 
        - Known as the "Heart of India" due to its central location.
        - Hosts the Khajuraho Group of Monuments, famous for their erotic sculptures.
        - The Bhimbetka rock shelters exhibit prehistoric cave paintings.
        """,
        "Chhattisgarh": """
        - The name translates to "Thirty-Six Forts," though the exact origin is debated.
        - Rich in mineral resources and dense forests, supporting diverse wildlife.
        - Home to the Chitrakote Falls, often referred to as the "Niagara Falls of India."
        """,
        "Rajasthan": """
        - Known for its majestic forts and palaces, including the Amber Fort and City Palace.
        - Hosts the Thar Desert, the world's 17th largest desert.
        - The Pushkar Camel Fair is one of the world's largest livestock fairs.
        """,
        "Gujarat": """
        - The Gir National Park is the only natural habitat of the Asiatic lion.
        - Tulsi Shyam in Gujarat is known for a gravity hill where vehicles appear to roll uphill.
        - The state is famous for its vibrant Navratri festival celebrations.
        """,
        "Maharashtra": """
        - Mumbai, the capital, is the financial hub of India and home to Bollywood.
        - The Ajanta and Ellora caves are UNESCO World Heritage Sites known for their ancient rock-cut temples.
        - The state has a rich tradition of Lavani, a genre of music popular in Maharashtra.
        """,
        "Goa": """
        - Known for its pristine beaches and Portuguese heritage.
        - The Basilica of Bom Jesus in Old Goa is a UNESCO World Heritage Site.
        - Celebrates vibrant festivals like Carnival and Shigmo with great enthusiasm.
        """,
        "Andhra Pradesh": """
        - The city of Amaravati is being developed as the state's new capital.
        - Home to the Tirumala Venkateswara Temple, one of the world's richest temples.
        - The state has a rich tradition of Kuchipudi, a classical Indian dance form.
        """,
        "Telangana": """
        - Hyderabad, the capital, is known for its historic Charminar and delicious biryani.
        - The region celebrates the Bonalu festival, dedicated to the Goddess Mahakali.
        - Known for its unique art forms like Nirmal paintings and Bidriware.
        """,
        "Karnataka": """
        - Bengaluru, the capital, is known as the "Silicon Valley of India."
        - Home to Hampi, a UNESCO World Heritage Site with ruins of the Vijayanagara Empire.
        - The state is rich in biodiversity, with numerous wildlife sanctuaries and national parks.
        """,
        "Tamil Nadu": """
        - Chennai is considered the cultural capital of South India.
        - Bharatanatyam, one of the oldest classical dance forms, originated here.
        - The state has a rich tradition of temple architecture, evident in structures like the Meenakshi Temple.
        """,
        "Kerala": """
        - Known as "God's Own Country" for its scenic landscapes and backwaters.
        - The state has the highest literacy rate in India.
        - Celebrates the Onam festival with traditional boat races and dances.
        """,
        "Bihar": """
        - Bodh Gaya in Bihar is where Gautama Buddha attained enlightenment.
        - The ancient Nalanda University was a renowned center of learning.
        - Chhath Puja, dedicated to the Sun God, is a major festival here.
        """,
        "Jharkhand": """
        - Rich in mineral resources, contributing significantly to India's economy.
        - Home to the Betla National Park, known for its wildlife and waterfalls.
        - Hosts the tribal festival of Sarhul, celebrating nature and community.
        """,
        "Odisha": """
        - The Sun Temple at Konark is a UNESCO World Heritage Site.
        - Hosts the Rath Yatra festival in Puri, attracting millions of devotees.
        - Known for its classical dance form, Odissi.
        """,
        "West Bengal": """
        - Kolkata was the capital of British India until 1911.
        - The Sundarbans, the world's largest mangrove forest, is located here.
        - Celebrates Durga Puja with grandeur and artistic pandals.
        """,
        "Assam": """
        - Famous for its Assam tea, exported worldwide.
        - Kaziranga National Park is home to the one-horned rhinoceros.
        - Celebrates Bihu, marking the Assamese New Year and agricultural cycles.
        """,
        "Arunachal Pradesh": """
        - Known as the "Land of the Rising Sun" in India.
        - Home to diverse indigenous tribes with unique cultures.
        - Tawang Monastery is the largest monastery in India.
        """,
    }
