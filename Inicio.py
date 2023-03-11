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
footer = footer()
#Elements of web
brand = brand()
cards = cards()

col1, col2 = st.columns([5, 20])
with col1:
   le.image_clickable("img/textlogo.png", "https://saveyourlife.streamlit.app/Brain%20Tumor")
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

col1, col2 = st.columns([20, 10])
with col1:
   st.markdown('### Nuestros trabajos')
with col2:
   st.markdown('### Nuestros Blog')

col1, col2, col3 = st.columns([10, 10, 10])

with col1:
   # Llama a la función con la ruta de la imagen y la URL de destino
   le.image_clickable("img/cerebro.png", "https://saveyourlife.streamlit.app/Brain%20Tumor")
   with st.expander("Tumor cerebral"):
      st.write("Un tumor cerebral es una masa o bulto de células anormales que se encuentra en el cerebro.\
            Existen varios tipos de tumores cerebrales. Algunos tumores cerebrales no son cancerosos (benignos) y algunos tumores sí lo son (malignos).\
            Los tumores cerebrales se pueden originar en el cerebro (tumores cerebrales primarios) o el cáncer se puede originar en otras partes del\
            cuerpo y luego extenderse hasta el cerebro (tumores cerebrales secundarios o metastásicos). La rapidez del crecimiento de un tumor\
            cerebral puede variar en gran medida. La tasa de crecimiento y la ubicación del tumor cerebral determinan cómo afectará el funcionamiento\
            del sistema nervioso. Las opciones de tratamiento del tumor cerebral dependen del tipo de tumor cerebral que tengas, así como también de su tamaño y ubicación.")

with col2:
   # Llama a la función con la ruta de la imagen y la URL de destino
   le.image_clickable("img/cerebro.png", "Brain_tumor_predict.py")
   with st.expander("Cancer de mama"):
      st.write("El cáncer de mama es un tipo de cáncer que se forma en las células de las mamas. Después del cáncer de piel, el cáncer de mama es el\
            tipo más común diagnosticado en mujeres en Estados Unidos. El cáncer de mama se puede presentar tanto en hombres como en mujeres; sin embargo,\
            es mucho más común en las mujeres. El considerable apoyo para la concientización y la financiación de investigaciones sobre el cáncer de mama\
            ha ayudado a crear avances en el diagnóstico y tratamiento de esta enfermedad. Las tasas de supervivencia al cáncer de mama han aumentado y\
            el número de muertes asociadas con esta enfermedad está disminuyendo constantemente, en gran medida debido a factores como la detección temprana,\
            un nuevo enfoque de tratamiento personalizado y una mejor comprensión de la enfermedad.")

with col3:
   components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sunsets don&#39;t get much better than this one over <a href="https://twitter.com/GrandTetonNPS?ref_src=twsrc%5Etfw">@GrandTetonNPS</a>. <a href="https://twitter.com/hashtag/nature?src=hash&amp;ref_src=twsrc%5Etfw">#nature</a> <a href="https://twitter.com/hashtag/sunset?src=hash&amp;ref_src=twsrc%5Etfw">#sunset</a> <a href="http://t.co/YuKy2rcjyU">pic.twitter.com/YuKy2rcjyU</a></p>&mdash; US Department of the Interior (@Interior) <a href="https://twitter.com/Interior/status/463440424141459456?ref_src=twsrc%5Etfw">May 5, 2014</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>',height=420,width=350)

st.markdown(footer, unsafe_allow_html=True)
#CCS
importar_css('.streamlit/stylefooter.css') 
importar_css('bootstrap/css/bootstrap.min.css')
importar_css('.streamlit/style.css')
