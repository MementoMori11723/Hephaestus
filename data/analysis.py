import random

import pandas as pd
from geopy.geocoders import Nominatim

from . import api


def analyse(data: dict) -> dict:
    return {
        "tarot": tarot(data["Month"], data["Color"]),
        "dress": dress(data["Dress"]),
        "recipe": recipe(
            data["Taste"], data["Region"], data["Time"], data["Festivals"]
        ),
        "place": place(data["Nature"], data["Region"], data["Culture"]),
        "art": art(data["Art"], data["Number"]),
    }


def tarot(month: str, color: str) -> dict:
    data = api.Tarot()
    month = month.strip().capitalize()
    color = color.strip().capitalize()

    zodiac = data["month"].get(month, "Unknown")
    reading = data["color"].get(color, "No color found!")
    z_reading = data["sign"].get(zodiac, "No Zodiac found!")

    return {"Zodiac": zodiac, "Color Reading": reading, "Zodiac-reading": z_reading}


def dress(type: str) -> dict:
    res = api.Dress()[type]
    res["type"] = type
    return res 


def recipe(taste: str, region: str, time: str, festivals: str) -> dict:
    data = api.Flavors()

    filtered = data[data["Cuisine"].str.contains(region, case=False, na=False)]

    if festivals.lower() == "yes":
        filtered = filtered[filtered["is_vegetarian"] == True]
    else:
        filtered = filtered[
            filtered["is_vegetarian"] == (True if taste == "Yes" else False)
        ]

    if time.lower() == "morning":
        filtered = filtered[filtered["TotalTimeInMins"] <= 30]
    elif time.lower() == "night":
        filtered = filtered[filtered["TotalTimeInMins"] >= 45]

    if len(filtered) <= 0:
        filtered = data

    choice = filtered.sample(frac=1).iloc[0]

    return {
        "name": choice["TranslatedRecipeName"],
        "ingredients": choice["Cleaned-Ingredients"],
        "cuisine": choice["Cuisine"],
        "vegetarian": "Yes" if choice["is_vegetarian"] else "No",
        "instructions": choice["TranslatedInstructions"],
        "image": choice["image-url"],
        "url": choice["URL"],
    }


def place(nature: str, region: str, culture: str) -> dict:
    data = api.Tourist_places()

    culture_keywords = {
        "Storytelling": "legend",
        "Rituals": "temple",
        "Crafts": "handicraft",
    }

    keyword = culture_keywords.get(culture, "")

    filtered = data[
        (data["zone"].str.contains(region, case=False, na=False))
        & (data["type"].str.contains(nature, case=False, na=False))
    ]

    if keyword:
        filtered = filtered[
            filtered["significance"].str.contains(keyword, case=False, na=False)
        ]

    if len(filtered) <= 0:
        filtered = data

    choice = filtered.sample(frac=1).iloc[0]

    return {
        "data": choice,
    }


def art(type: str, num: int) -> dict:
    def music(num: int) -> dict:
        data = api.Top_videos()
        image = api.Music_images()
        res = (
            data.sample(frac=1)[["title", "view_count", "like_count"]]
            .head(5)
            .reset_index()
        )
        num -= 1
        return {
            "Name": res.iloc[num]["title"],
            "Url": random.choice(image),
            "View Count": int(res.iloc[num]["view_count"]),
            "Like Count": int(res.iloc[num]["like_count"]),
        }

    def dance(_: int) -> dict:
        data = api.Dance()
        keys = []
        for i in data.keys():
            keys.append(i)

        return data[random.choice(keys)]

    def painting(num: int) -> dict:
        data = api.Painting()
        item = random.choice(data)
        return {
            "Name": item["Name"],
            "desc": item["Desc"],
            "url": f"./static/{item['Field']}/{num}.jpg",
        }

    art_forms = {
        "Music": music,
        "Painting": painting,
        "Dance": dance,
    }

    result = art_forms[type](num)
    result["type"] = type
    return result


def Location(data) -> pd.DataFrame:
    geolocator = Nominatim(user_agent="streamlit_map_app")
    location = geolocator.geocode(f"{data['data']['place_name']}, india")
    if location == None:
        location = geolocator.geocode(f"{data['data']["city"]}")
    return pd.DataFrame({"lat": [location.latitude], "lon": [location.longitude]})
