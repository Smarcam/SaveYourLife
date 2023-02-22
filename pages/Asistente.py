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
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com',
		'About':'About your application: **Hello World!**'
	}
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
    ['mi nombre es (.*)', ['Hola! %1. Soy la Yeny. En que puedo ayudarte?']],
    ['hola', ['Hola Soy La Yeny. Que cojones quieres?????']],
    ['que puedes hacer', ['puedo hacer muchas cosas o que te crees subnormal, me tienes mas agobia que spiderman en un descampado.']],
    ['abrir (.*)', ['Lo siento, yo puedo buscarte %1 . Estoy en el parque se solipandi. y no puedo hacer esas cosas chikillo que me va a ve mi mare.']],
    ['piensas si hay un creador', ['si, aro ompare si no como voy a esta aqui hablando']],
    ['dime algo sobre ti', ['Pos aye estuve de aguaora por que venia la tres patos con mi primo']],
    ['quien soy', ['a mi que coño me importa']],
    ['quien te creo', ['un jartible.']],
    ['', ['En que puedo ayudarte baby']]
]

st.title("Chatbot")


def main():
    ref = st.text_input("Dime argo cojones")

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
