import streamlit as st 
from functions import *
import src.search as srch
import src.chatbot_code as chb
import re

#PageConfig
page_config = importar_config()
st.title("Chatbot")

def main():
    ref = st.text_input("", label_visibility=st.session_state.visibility,
        disabled=st.session_state.disabled,
        placeholder="¿En que puedo ayudarte?")
    
    # Use una expresión regular para buscar cualquier variante de "buscar"
    # en la entrada del usuario
    match = re.search(r"(busc[oa]|encontrar|hallar)\b", ref, re.IGNORECASE)
    if match:
        # Extraer la consulta de búsqueda del usuario
        search_term = ref[match.end():].strip()
        srch.on_enter_pressed(search_term)
    else:    
        split_ref = re.split(r"(búscame|busca)", ref, re.IGNORECASE)
        if len(split_ref) > 1:
            search_term = split_ref[-1].strip()
            srch.on_enter_pressed(search_term)
        else:
            respo = chb.chatbot_response(ref)
            st.write(respo)

if __name__ == "__main__":
    main()
#CSS 
css = importar_css()
