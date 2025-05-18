import streamlit as st
import os

def main():
    try:
        # Variables
        pages_dir = "pages/" 
        priority = ["Home", "About"]
        unsorted_routes = {} 
        pages = [] 

        # Pre - setup config for streamlit!
        st.set_page_config(
            page_title="Hephaestus",
            page_icon="🗺️",
            layout="wide",
            initial_sidebar_state="expanded",
        )

        # Listing all files from pages folder! 
        for file in os.listdir(path=pages_dir):
           unsorted_routes[os.path.splitext(file)[0].capitalize()] = os.path.join(pages_dir, file)

        # This first sets the priority routes at the top! 
        routes = {
            k: unsorted_routes[k] for k in priority if k in unsorted_routes
        }

        # This will then append the rest of the routes!
        for k in sorted(set(unsorted_routes) - set(priority)):
            routes[k] = unsorted_routes[k]

        # Creating page objects and appending them to a list!
        for route, path in routes.items():
            isHome = True if route == "Home" else False
            pages.append(
                st.Page(
                    path, title=route,
                    default=isHome
                )
            )
        
        # Setting Sidebar Navigation!
        navigation = st.navigation(pages=pages)
        navigation.run()
    except Exception as e:
        raise e

if __name__ == "__main__":
    main()
