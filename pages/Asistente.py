import streamlit as st
from streamlit_chat import message
import src.chatbot_code as chb
import re

st.set_page_config(
    page_title="Chat SaveYourLife",
    page_icon=":robot:"
)

st.header("Chat SaveYourLife")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("You: ","Hola!!", key="input")
    return input_text

def chatbot_response(user_input):
    response = chb.chatbot_response(user_input)
    return response

user_input = get_text()

if user_input:
    bot_response = chatbot_response(user_input)
    st.session_state.generated.append(bot_response)
    st.session_state.past.append(user_input)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
