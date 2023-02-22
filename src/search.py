import atexit
import streamlit as st
from selenium import webdriver

# Función de limpieza que se ejecuta al finalizar el script
@atexit.register
def clean_up():
    try:
        browser.quit()
    except NameError:
        pass

def google_search(term):
    if term:
        global browser
        browser = webdriver.Chrome()
        browser.get(f"https://www.google.com/search?q={term}")

        # Espera hasta que se cargue la página de resultados
        browser.implicitly_wait(5)

    else:
        st.warning("Por favor, ingrese un término de búsqueda.")

def on_enter_pressed(term):
    if term:
        google_search(term)
