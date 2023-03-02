import streamlit as st 
from nltk.chat.util import Chat, reflections
from PIL import Image
from functions import *
import src.search as srch


pairs = [
    ['mi nombre es (.*)', ['Hola! %1. Soy medical robot. ¿En que puedo ayudarte?']],
    ['hola', ['Hola Soy medical robot. ¿Que quiere?']],
    ['que puedes hacer', ['puedo hacer muchas cosas como buscar , cosas sobre medicina y mucho más.']],
    ['abrir (.*)', ['Lo siento, yo puedo buscarte %1 . No tengo acceso a eso.']],
    ['piensas si hay un creador', ['Puede que si.']],
    ['dime algo sobre ti', ['Soy un bot para ayudarte en todo lo que pueda.']],
    ['quien soy', ['Una IA.']],
    ['quien te creo', ['Unos humanos.']],
    ['', ['']]
]

st.title("Chatbot")


def main():
    ref = st.text_input("¿En que puedo ayudarte?")

    chat = Chat(pairs, reflections)
    respo = chat.respond(ref)
    if "abrir" in ref:
        search_term = ref.split("abrir")[1]
        srch.on_enter_pressed(search_term)
    st.write(respo)

if __name__ == "__main__":
    main()
#CSS 
css = importar_css()
