import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from st_pages import show_pages_from_config
from functions import *
import src.load_event as le

#PageConfig
page_config = importar_config()
show_pages_from_config()
#Menu
menu = menu()
#Footer
footer = footer()

st.markdown(menu, unsafe_allow_html=True)

with st.container():
   le.logo_clickable('img/logo.png', "https://saveyourlife.streamlit.app")


col1, col2, col3 = st.columns([11,15,11])

with col1:
    st.write("")

with col2:
    st.image('img/brain_about.jpg', use_column_width='auto')

with col3:
    st.write("")

col1, col2 = st.columns([30,10])

with col1:
    st.markdown("""
            Somos Miguel Ángel y Samuel, dos alumnos del Master FP en Inteligencia Artificial y Big Data del centro CPIFP 
            Nuevo que hemos creado una red neuronal para la predicción del tipo de tumor cerebral que tiene un paciente. 
            Utilizando nuestro conocimiento en lenguaje de programación Python, hemos desarrollado un modelo preciso para
            respaldar los ánalisis médicos en neurología y oncología.

            Además, hemos aplicado técnicas avanzadas de procesamiento del lenguaje natural para desarrollar un chatbot 
            que brinda información y asesoramiento a los usuarios de la web. Estamos orgullosos 
            de presentar nuestro proyecto en forma de una página web de fácil acceso para el público en general y los 
            profesionales médicos.

            Nos enorgullece ofrecer una herramienta innovadora de predicción de tumores cerebrales que puede ser útil 
            en la detección temprana y el tratamiento de esta enfermedad. Esperamos que nuestro proyecto pueda marcar una 
            diferencia significativa en la vida de las personas que luchan contra el cáncer cerebral y pueda ser utilizado por 
            los profesionales médicos para mejorar la calidad de vida de sus pacientes.
            """)
with col2:
    components.html('<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Sunsets don&#39;t get much better than this one over <a href="https://twitter.com/GrandTetonNPS?ref_src=twsrc%5Etfw">@GrandTetonNPS</a>. <a href="https://twitter.com/hashtag/nature?src=hash&amp;ref_src=twsrc%5Etfw">#nature</a> <a href="https://twitter.com/hashtag/sunset?src=hash&amp;ref_src=twsrc%5Etfw">#sunset</a> <a href="http://t.co/YuKy2rcjyU">pic.twitter.com/YuKy2rcjyU</a></p>&mdash; US Department of the Interior (@Interior) <a href="https://twitter.com/Interior/status/463440424141459456?ref_src=twsrc%5Etfw">May 5, 2014</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>',height=420,width=350)

#footer       
st.markdown(footer, unsafe_allow_html=True)
#CCS
importar_css('.streamlit/stylefooter.css') 
importar_css('bootstrap/css/bootstrap.min.css')
importar_css('.streamlit/style.css')
