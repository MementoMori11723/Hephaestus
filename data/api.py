import sqlite3

import pandas as pd


def fetch(table: str) -> pd.DataFrame:
    conn = sqlite3.Connection("data/base.db")
    cursor = conn.cursor()

    cursor.execute(f"PRAGMA table_info({table})")
    column_info = cursor.fetchall()
    column_info = [row[1] for row in column_info]

    cursor.execute(f"select * from {table}")
    rows = cursor.fetchall()

    conn.close()
    return pd.DataFrame(rows, columns=column_info)


def Flavors():
    return fetch("flavors")


def Top_videos():
    return fetch("top_videos")


def Tourist_places():
    return fetch("tourist_places")
