import streamlit as st 
from selenium import webdriver
from nltk.chat.util import Chat, reflections
from PIL import Image
icon = Image.open('img/icon.png')
st.set_page_config(
	page_title = 'SaveYourLife Tumor Brain Predict!',
	page_icon = icon,
	layout = 'wide',
	initial_sidebar_state = 'collapsed',
	)
st.sidebar.title("Main Menu")

def google_search(term):
    if term:
        global browser
        browser = webdriver.Chrome()
        browser.get(f"https://www.google.com/search?q={term}")

        # Espera hasta que se cargue la página de resultados
        browser.implicitly_wait(5)

    else:
        st.warning("Por favor, ingrese un término de búsqueda.")

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
        google_search(search_term)
    st.write(respo)

if __name__ == "__main__":
    main()
# LINK TO THE CSS FILE
with open('.streamlit/style.css')as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
