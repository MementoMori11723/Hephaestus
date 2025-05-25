import sqlite3

# def store_data(data:dict):
#     for name, df in zip(data.keys(), data.values()):
#         with sqlite3.connect("data/db/base.db") as conn:
#             df.to_sql(name.replace(".csv", ""), conn, if_exists="replace", index=False)
#     print("Added all files to .db")
