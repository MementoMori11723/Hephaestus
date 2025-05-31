import streamlit as st
from streamlit.delta_generator import DeltaGenerator


def Quiz(main: DeltaGenerator) -> None:
    main.header("Personalization")

    main.write(
        "Get personalized results to choose the best recipes to try and place to go"
    )
    if "active_expander" not in st.session_state:
        st.session_state.active_expander = "questions"

    questions = main.expander(
        "Personalization Test", st.session_state.active_expander == "questions"
    )
    questions.write(
        "### Here are a few question to give you a personalized recommendations"
    )
    personal_questions(questions)
    if questions.button("toggle"):
        st.session_state.active_expander = "answers"
        st.rerun()

    answers = main.expander("Result", st.session_state.active_expander == "answers")
    result(answers)
    if answers.button("Try Again"):
        st.session_state.active_expander = "questions"
        st.rerun()


def personal_questions(writer: DeltaGenerator) -> None:
    writer.write("test")


def result(writer: DeltaGenerator) -> None:
    writer.write("test")
