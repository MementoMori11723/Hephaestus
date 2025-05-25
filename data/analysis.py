import os
import pandas as pd
# from data.api import fetch

def load_data() -> dict[str, pd.DataFrame]:
    data = {}
    
    for file in os.listdir("datasets/"):
        data[file] = pd.read_csv(
            os.path.join("datasets/", file)
        )

    return data

def analyse():

    data = load_data()

    df = data["Crop_production.csv"]

    return df

