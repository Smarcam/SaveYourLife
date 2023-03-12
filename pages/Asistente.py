import streamlit as st
from streamlit_chat import message
import src.chatbot_code as chb
import src.search as srch
from st_pages import show_pages_from_config
import re
from functions import *
#PageConfig
page_config = importar_config()
show_pages_from_config()
#Menu
menu = menu()
#Footer
footerasistente = footer()

st.markdown(menu, unsafe_allow_html=True)
st.markdown("""
<span class="css-10trblm e16nr0p30" style="color:#28d0ff;text-shadow: 2px 1px 1px #0000002e, 3px 2px 1px #0000004f;">Chatbot</span>
""", unsafe_allow_html=True)

st.header("Chat SaveYourLife")

if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text = st.text_input("Tú: ","",
                                placeholder="¿En que puedo ayudarte?",
                                key="input")
    return input_text

def chatbot_response(user_input):
    response = chb.chatbot_response(user_input)
    return response

user_input = get_text()

if user_input:
    bot_response = chatbot_response(user_input)
    st.session_state.generated.append(bot_response)
    st.session_state.past.append(user_input)

if 'buscador' not in st.session_state:
    st.session_state['buscador'] = None

match = re.search(r"(busc[oa]|encontrar|hallar|búscame|busca)\b", user_input, re.IGNORECASE)
if match:
    # Extraer la consulta de búsqueda del usuario
    search_term = user_input[match.end():].strip()
    srch.on_enter_pressed(search_term)
else:
    split_ref = re.split(r"(búscame|busca)", user_input, re.IGNORECASE)
    if len(split_ref) > 1:
        search_term = split_ref[-1].strip()
        srch.on_enter_pressed(search_term)
    else:
        st.write("")


if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], avatar_style="bottts", key=str(i))
        message(st.session_state['past'][i], avatar_style="avataaars", is_user=True, key=str(i) + '_user')

st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)

st.markdown(footerasistente, unsafe_allow_html=True)
#CCS
importar_css('.streamlit/stylefooter.css') 
importar_css('bootstrap/css/bootstrap.min.css')
importar_css('.streamlit/style.css')

