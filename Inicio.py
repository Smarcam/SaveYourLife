import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import src.search as srch
import src.load_event as le
from st_pages import show_pages_from_config
from functions import *
import datetime

#PageConfig
page_config = importar_config()
show_pages_from_config()
#Menu
menu = menu()
#Footer
footer = footermain()
#Elements of web
brand = brand()
cards = cards()
def stylish_button(link, text):
    button_html = f'''
    <style>
        .my-button {{
            display: inline-block;
            padding: 10px 20px;
            font-size: 18px;
            font-weight: bold;
            text-decoration: none;
            background-color: #0089b1;
            color: #fff;
            border-radius: 5px;
            transition: background-color 0.3s ease;
        }}
        .my-button:hover {{
            background-color: #006d90;
        }}
    </style>
    <a href="{link}" class="my-button">{text}</a>
    '''
    st.markdown(button_html, unsafe_allow_html=True)

# Uso del botón personalizado
donate_link = "https://www.paypal.com/donate?hosted_button_id=K9MYJDDJU35TN"
button_text = "Donar con PayPal"
stylish_button(donate_link, button_text)

col1, col2 = st.columns([5, 20])
with col1:
   le.image_clickable("img/textlogo.png", "https://saveyourlife.streamlit.app/~/+/Detector De Tumor Cerebral")
with col2:
  term = st.text_input(" ",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder="Introduzca su búsqueda:",) 
  if term:
    srch.on_enter_pressed(term)

st.image("img/logo.png")
st.image("img/icon.png")
st.image("img/inicio.png")
st.image("img/inicio_2.jpeg")

st.markdown(menu, unsafe_allow_html=True)
st.markdown(brand, unsafe_allow_html=True)
st.markdown(cards, unsafe_allow_html=True)
st.markdown(footer, unsafe_allow_html=True)
#CCS
importar_css('.streamlit/stylefooter.css') 
importar_css('bootstrap/css/bootstrap.min.css')
importar_css('.streamlit/mainstyle.css')
