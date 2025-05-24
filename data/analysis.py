import os
import pandas as pd
# from data.api import fetch

def load_data() -> dict:
    data = {}
    
    for file in os.listdir("datasets/"):
        data[file] = pd.read_csv(
            os.path.join("datasets/", file)
        )

    return data

def analyse():
    pass
