import streamlit as st
from streamlit.delta_generator import DeltaGenerator

from data import analysis


def Sidebar(c: DeltaGenerator) -> None:
    c.write("Sidebar")


def Quiz(c: DeltaGenerator) -> None:
    c.header("✨ Personalization")

    c.write(
        "Answer a few fun and thoughtful questions to get handpicked recipes, inspiring artworks, and travel recommendations tailored just for you."
    )

    if "active_expander" not in st.session_state:
        st.session_state.active_expander = "questions"

    questions = c.expander(
        "🎯 Start Your Personalization Quiz",
        st.session_state.active_expander == "questions",
    )

    questions.write(
        "#### Let's get to know you a little better so we can craft the perfect set of recommendations!"
    )

    form = questions.form(key="question", border=False)
    st.session_state.result = personal_questions(form)
    if form.form_submit_button("Submit", use_container_width=True, type="primary"):
        st.session_state.active_expander = "answers"
        st.rerun()
    c.subheader("🎉 Your Personalized Results")
    answers = c.expander(
        "🔍 See Your Recommendations", st.session_state.active_expander == "answers"
    )
    result(answers)
    if answers.button("Try Again", use_container_width=True):
        st.session_state.active_expander = "questions"
        st.rerun()


def personal_questions(c: DeltaGenerator) -> dict:
    col1, col2 = c.columns(2)
    color = col1.selectbox(
        "What's your favorite color?",
        ["Red", "Blue", "Green", "Yellow", "White", "Black", "Pink"],
    )
    number = col2.radio("Pick a number between 1 and 5", [1, 2, 3, 4, 5])

    month = col1.selectbox(
        "What’s your birth month?",
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
        ],
    )
    taste = col2.radio(
        "Do you prefer spicy, sweet, or tangy food?", ["Spicy", "Sweet", "Tangy"]
    )
    nature = col1.radio("Do you enjoy nature or cities more?", ["Nature", "Cities"])
    region = col2.selectbox(
        "Which region of India do you feel most connected to?",
        ["North", "South", "East", "West", "Central", "Northeast"],
    )
    outfit = col1.selectbox(
        "Pick a traditional Indian outfit you like.",
        ["Kurta", "Saree", "Dhoti", "Salwar Kameez", "Sherwani"],
    )
    art_form = col1.radio(
        "Do you prefer painting, dance, or music?", ["Painting", "Dance", "Music"]
    )
    festivals = col2.radio("Do you enjoy festivals?", ["Yes", "No"])
    time_of_day = col1.selectbox(
        "What's your favorite time of the day?",
        ["Morning", "Afternoon", "Evening", "Night"],
    )
    cultural_leaning = col2.radio(
        "Do you enjoy storytelling, rituals, or crafts more?",
        ["Storytelling", "Rituals", "Crafts"],
    )

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
    c.write(st.session_state.result)
