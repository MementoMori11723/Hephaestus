from streamlit.delta_generator import DeltaGenerator


def About(main: DeltaGenerator, sidebar: DeltaGenerator, content: dict) -> None:
    main.header("About Us")
    main.divider()
    sidebar.write("## Sections")
    for question, answer in zip(content.keys(), content.values()):
        sidebar.write(f"- {question}")
        main.subheader(question)
        main.write(answer)
        if question != "How can I contact you?":
            main.divider()


def Questions() -> list[str]:
    return [
        "Who built this project?",
        "Why did you choose Indian culture as the theme?",
        "Why does the website look so... patriotic?",
        "Why Streamlit? Isn’t it for data apps?",
        "Is this open source? Can I contribute?",
        "Will this project support other cultures or themes in the future?",
        "How can I contact you?",
    ]


def Answers() -> list[str]:
    return [
        """This project was developed as part of the YourStory Hackathon by Snowflake, which encouraged the use of Streamlit to showcase creativity, storytelling, and data in meaningful ways. While it was a team effort, most of the development, design, and content was created by me — from crafting the user interface to writing the cultural content and coding the logic behind the scenes.""",
        """India is not just a country — it’s a cultural universe. From philosophy and food to festivals and fashion, India represents a living, breathing story of human creativity and diversity. This platform is my way of celebrating that richness and making it accessible, personalized, and engaging — especially for those curious to discover or reconnect with Indian heritage.""",
        """Great observation! The visual theme of the website is directly inspired by the colors of the Indian flag. The white background offers a clean and peaceful canvas that keeps the focus on content clarity. Navy blue text reflects the color of the Ashoka Chakra, symbolizing truth and Dharma. Orange buttons were chosen to evoke energy, courage, and a sense of action, while green links represent growth, harmony, and prosperity. The typeface, Ancizar Serif, was selected for its classic elegance and readability, perfectly complementing the traditional yet refined essence of Indian culture.""",
        """Yes — and that’s what makes this project unique! Streamlit is often used for data dashboards, but I wanted to push its boundaries to build a visually engaging and interactive cultural experience. It’s simple, Pythonic, and allowed for rapid development during the hackathon timeframe. Plus, it aligns perfectly with the goals of the YourStory challenge.""",
        """Yes! If you’re interested in contributing, feel free to reach out or check out the GitHub repo (if available). Contributions, ideas, and feedback are always welcome.""",
        """Absolutely! People are welcome to use this template to create projects around other cultures or themes. You can also contribute by submitting a pull request to the repository to add new content or features.""",
        """You can reach out via email at [contact@yasasvi.site](mailto:contact@yasasvi.site). Feel free to ask questions, offer feedback, or just say hi!"""
    ]
