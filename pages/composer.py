import streamlit as st
from openai import OpenAI
import uuid

from utils.prompt import get_prompt_from_file, update_history

# Initialize openai client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
st.session_state["openai_model"] = "gpt-3.5-turbo"

st.title("Think of a theme 💭")

# Initialize app state
if "input_disabled" not in st.session_state:
    st.session_state.input_disabled = False

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Draw chat on screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if not st.session_state.input_disabled:
    if user_input := st.chat_input("Give a brief description..."):
        with st.chat_message("user"):
            llm_input = get_prompt_from_file(user_input)
            st.markdown(user_input)
            st.session_state.messages.append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            stream_response = client.chat.completions.create(
                model=st.session_state["openai_model"],
                messages=[{"role": "user", "content": llm_input}],
                stream=True,
            )
            response = st.write_stream(stream_response)
            st.session_state.messages.append({"role": "assistant", "content": response})

        update_history()
