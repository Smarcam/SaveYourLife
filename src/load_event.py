from base64 import b64encode
import streamlit as st

def image_clickable(image_path, target_url):
    """Función que crea una imagen clickeable"""
    # Carga la imagen desde el archivo
    image = open(image_path, 'rb').read()
    # Agrega el evento de clic a la imagen
    clickable_image = f'<a href="{target_url}"><img src="data:image/png;base64,{b64encode(image).decode()}" style="max-width: 100%;"></a>'
    # Muestra la imagen clickeable
    st.markdown(clickable_image, unsafe_allow_html=True)