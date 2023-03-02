import streamlit as st
import webbrowser
from googlesearch import search as google_search


def my_google_search(query):
    if query:
        results = []
        for j in google_search(query):
            results.append(j)
        return results
    else:
        st.warning("Por favor, ingrese un término de búsqueda.")


def on_enter_pressed(term):
    if term:
        results = my_google_search(term)
        if results:
            # Abre la búsqueda en una nueva pestaña del navegador
            url = f"https://www.google.com/search?q={'+'.join(term.split())}"
            webbrowser.open_new_tab(url)
        else:
            st.warning("No se encontraron resultados para su búsqueda.")

