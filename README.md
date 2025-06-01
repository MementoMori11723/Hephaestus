# 🛕 Hephaestus

A **Streamlit** app built for the **YourStory Hackathon: Hero Challenge by Snowflake**.
**Hephaestus** is a data-first storytelling platform that celebrates India's rich tapestry of traditional art forms, diverse cultural practices, and promotes responsible tourism.

> “Dive into the heart of India's artistic and cultural heritage with a story that enriches both the traveller’s journey and preserves our cultural treasures—the data-first way!”

---

## 🌏 About the Project

India is home to one of the world's most vibrant and diverse cultural legacies. From intricate paintings to centuries-old festivals, each region brings its unique flavor to the nation's collective identity.

**Hephaestus** aims to:

* Showcase traditional Indian art forms
* Highlight cultural experiences from various regions
* Promote sustainable and responsible tourism
* Use data to personalize and enrich user journeys

This project uses **Streamlit** for the interactive UI and combines cultural storytelling with image galleries and basic analytics.

---

## 📁 Project Structure

```
hephaestus/
├── app.py                 # Main entry point
├── components/            # UI component modules
├── data/                  # SQLite DB, APIs, and analysis logic
├── pages/                 # Streamlit pages for navigation
├── static/                # Traditional art form image galleries
├── LICENSE
├── Makefile               # Task automation
├── README.md
```

### 🔹 `components/`

Reusable UI elements such as:

* `home.py`, `about.py`, `explore.py` – for individual sections
* `common.py` – shared functions and layout
* `personalize.py` – user-customized content

### 🔹 `data/`

Contains:

* `base.db` – SQLite database of artworks and cultural data
* `api.py` – APIs to retrieve regional or art-specific content
* `analysis.py` – logic for trend analysis or personalization

### 🔹 `pages/`

Each `.py` file here corresponds to a navigation page in Streamlit:

* `home.py`
* `about.py`
* `culture.py`
* `explore.py`
* `personalize.py`

### 🔹 `static/`

Images categorized by Indian art styles:

* Gond, Warli, Kalighat, Kangra, Madhubani, Kerala Mural, Mandana, Pichwai

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/hephaestus.git
cd hephaestus
```

### 2. Set up environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt  # Make sure to add one!
```

### 3. Run the app

```bash
streamlit run app.py
```

---

## 🖼️ Art Forms Featured

* **Gond** – Tribal art from Madhya Pradesh
* **Warli** – Nature-focused tribal art from Maharashtra
* **Kalighat** – Folk art from Bengal
* **Kangra** – Miniature painting from Himachal
* **Madhubani** – Mythological art from Bihar
* **Mandana** – Floor/wall paintings from Rajasthan
* **Pichwai** – Temple-centric art from Nathdwara
* **Kerala Mural** – Fresco art found in temples of Kerala

---

## 🧠 Tech Stack

* 🐍 Python 3.11+
* 📊 Streamlit
* 🗃️ SQLite
* 📦 Modular architecture (components/pages)
* 🎨 Static assets for rich cultural visuals

---

## 📜 License

This project is licensed under the [MIT License](./LICENSE).

---

## 🤝 Contributing

Pull requests are welcome! If you have ideas to improve the experience or add more art forms, feel free to open an issue or submit a PR.

---

## 📣 Acknowledgements

* **Snowflake & YourStory** – for organizing the hackathon
* Open-source contributors and cultural researchers
* Ministry of Culture (India) for preserving rich visual content
