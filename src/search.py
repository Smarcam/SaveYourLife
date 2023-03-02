import streamlit as st
from googlesearch import search as google_search


def on_enter_pressed(term, num_results=10):
    if term:
        try:
            results = list(google_search(term, num_results=num_results))
            if results:
                url = f"https://www.google.com/search?q={'+'.join(term.split())}"
                st.markdown(f"[Resultados de la búsqueda]({url})")
            else:
                st.warning("No se encontraron resultados para su búsqueda.")
        except StopIteration:
            st.warning("No se encontraron resultados para su búsqueda o se alcanzó el límite máximo de solicitudes.")

