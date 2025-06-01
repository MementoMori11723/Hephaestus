import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data import analysis, api


def Sidebar(c: DeltaGenerator) -> None:
    facts = api.Month()
    c.subheader("Fun Facts")
    month = c.selectbox("Select a month", facts.keys())
    for i in facts[month]:
        c.write(i)


def Quiz(c: DeltaGenerator) -> None:
    if "active_expander" not in st.session_state:
        st.session_state.active_expander = "questions"

    c.header("✨ Personalization")
    c.write(
        "Answer a few fun and thoughtful questions to get handpicked recipes, inspiring artworks, and travel recommendations tailored just for you."
    )
    questions = c.expander(
        "🎯 Start Your Personalization Quiz",
        st.session_state.active_expander == "questions",
    )
    questions.write(
        "#### Let's get to know you a little better so we can craft the perfect set of recommendations!"
    )

    form = questions.form(key="question", border=False)
    st.session_state.result = personal_questions(form)

    c.subheader("🎉 Your Personalized Results")
    result(
        c.expander(
            "🔍 See Your Recommendations", st.session_state.active_expander == "answers"
        )
    )


def personal_questions(c: DeltaGenerator) -> dict:
    data = api.Personal_Options()
    col1, col2 = c.columns(2)
    color = col1.selectbox(
        "What's your favorite color?",
        data["color"],
    )
    number = col2.radio("Pick a number between 1 and 5", data["num"])

    month = col1.selectbox(
        "What’s your birth month?",
        data["month"],
    )
    taste = col2.radio("Are you a vegetarian?", data["true"])
    nature = col1.radio("Do you enjoy nature or cities more?", data["nature"])
    region = col2.selectbox(
        "Which region of India do you feel most connected to?",
        data["region"],
    )
    outfit = col1.selectbox(
        "Pick a traditional Indian outfit you like.",
        data["dress"],
    )
    art_form = col1.radio("Do you prefer painting, dance, or music?", data["art"])
    festivals = col2.radio("Do you enjoy festivals?", data["true"])
    time_of_day = col1.selectbox(
        "What's your favorite time of the day?",
        data["time"],
    )
    cultural_leaning = col2.radio(
        "Do you enjoy storytelling, rituals, or crafts more?",
        data["culture"],
    )

    if c.form_submit_button("Submit", use_container_width=True, type="primary"):
        st.session_state.active_expander = "answers"
        st.rerun()

    return analysis.analyse(
        {
            "Color": color,
            "Number": number,
            "Month": month,
            "Taste": taste,
            "Nature": nature,
            "Dress": outfit,
            "Region": region,
            "Art": art_form,
            "Festivals": festivals,
            "Time": time_of_day,
            "Culture": cultural_leaning,
        }
    )


def result(c: DeltaGenerator) -> None:
    c.header("🔮 Astrology Reading")
    c.write(f"**Sign**: [{st.session_state.result["tarot"]["Zodiac"]}](#)")
    for i in st.session_state.result["tarot"]["Zodiac-reading"]:
        c.write(f"\t - {i}")
    c.write("**Color Reading**:")
    for i in st.session_state.result["tarot"]["Color Reading"]:
        c.write(f"- {i}")

    c.divider()

    col1, col2 = c.columns(2, border=True)

    with col1:
        st.image(
            st.session_state.result["recipe"]["image"],
            caption=st.session_state.result["recipe"]["name"],
            use_container_width=True,
        )
        st.header(st.session_state.result["recipe"]["name"])
        st.write(f"- **Cusine**: {st.session_state.result["recipe"]["cuisine"]}")
        st.write(
            f"- **Is Vegetarian**: {st.session_state.result["recipe"]["vegetarian"]}"
        )
        st.write("#### Ingredients: ")
        res = ", ".join(
            word.strip().capitalize()
            for word in st.session_state.result["recipe"]["ingredients"].split(",")
        )
        st.write(res)
        st.write("#### Instructions")
        st.write(st.session_state.result["recipe"]["instructions"])
        st.link_button(
            "Click here to view the full recipes",
            url=st.session_state.result["recipe"]["url"],
            type="primary",
            use_container_width=True,
        )

    with col2:
        df = analysis.Location(st.session_state.result["place"])
        st.map(df)
        st.warning(
            "Sometimes the map might choose the city rather then the place itself!"
        )
        st.header(st.session_state.result["place"]["data"]["place_name"])
        st.write(f"- **City**: {st.session_state.result["place"]['data']['city']}")
        st.write(f"- **State**: {st.session_state.result["place"]['data']['state']}")
        st.write(f"- **Zone**: {st.session_state.result["place"]['data']['zone']}")
        st.write(f"- **Type**: {st.session_state.result["place"]['data']['type']}")
        st.write(f"- **Rating**: {st.session_state.result["place"]['data']['rating']}")
        st.write(
            f"- **Significance**: {st.session_state.result["place"]['data']['significance']}"
        )
        st.write(
            f"- **Is Camera allowed ?**: {st.session_state.result["place"]['data']['dslr_allowed']}"
        )
        st.write(
            f"- **Best time**: {st.session_state.result["place"]['data']['best_time_text']}"
        )
        st.write(
            f"- **Weekly off**: {st.session_state.result["place"]['data']['weekly_off']}"
        )

    col3, col4 = c.columns(2, border=True)

    with col3:
        st.image(
            st.session_state.result["dress"]["url"],
            caption=st.session_state.result["dress"]["type"],
            use_container_width=True,
        )
        st.header(st.session_state.result["dress"]["type"])
        st.write(st.session_state.result["dress"]["desc"])

    with col4:

        def music():
            st.image(st.session_state.result["art"]["Url"])
            st.subheader(st.session_state.result["art"]["Name"])
            st.write(f"##### **View Count**: {st.session_state.result["art"]["View Count"]}")
            st.write(f"##### **Like Count**: {st.session_state.result["art"]["Like Count"]}")

        def painting():
            st.image(
                st.session_state.result["art"]["url"],
                caption=st.session_state.result["art"]["Name"],
                use_container_width=True,
            )
            st.header(st.session_state.result["art"]["Name"])
            st.write(st.session_state.result["art"]["desc"])

        def dance():
            @st.dialog("sidebar-popup", width="large")
            def sidebar_popup(link: str) -> None:
                st.video(link)

            c.image(st.session_state.result["art"]["img"], use_container_width=True)
            c.write(st.session_state.result["art"]["info"])
            if c.button("Click for preview", use_container_width=True):
                sidebar_popup(st.session_state.result["art"]["url"])

        art = {
            "Music": music,
            "Painting": painting,
            "Dance": dance,
        }

        art[st.session_state.result["art"]["type"]]()

    if c.button("Try Again", use_container_width=True):
        st.session_state.active_expander = "questions"
        st.rerun()
