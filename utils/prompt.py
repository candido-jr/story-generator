import os
import streamlit as st
import json


def get_prompt_from_file(input):
    with open("prompt.md", "r") as file:
        return f'{file.read()}\n\n"{input}"'


def update_history():
    os.makedirs("history", exist_ok=True)

    with open(f"history/{st.session_state.session_id}.json", "w") as f:
        json.dump(st.session_state.messages, f)

    st.session_state.input_disabled = True
    st.rerun()
