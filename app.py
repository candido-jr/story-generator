import os
import streamlit as st


pages = [
    st.Page("pages/composer.py", title="Think of a theme"),
]


def get_json_files():
    files = os.listdir(".")
    json_files = [file for file in files if file.endswith(".json")]
    return json_files


pg = st.navigation(pages)
pg.run()
