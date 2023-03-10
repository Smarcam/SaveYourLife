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
#Menu
show_pages_from_config()

st.header("Buscador")
term = st.text_input(" ",label_visibility=st.session_state.visibility,disabled=st.session_state.disabled,placeholder="Introduzca su búsqueda:",) 
if term:
  srch.on_enter_pressed(term)
st.image("img/logo.png")
def menu():
  return """
<nav class="navbar navbar-expand-md navbar-dark fixed-top" style="background: #31b0d5">
  <div class="container-fluid" style="margin-left: 35px">
    <a class="navbar-brand" "href="https://saveyourlife.streamlit.app" target="_self">SaveYourLife</a>
    <div class="navbar-collapse collapse" id="navbarCollapse">
      <ul class="navbar-nav me-auto mb-2 mb-md-0">
        <li class="nav-item">
          <a class="nav-link" href="https://saveyourlife.streamlit.app/Asistente" target="_self" style="color:#d1e9ff;font-size: 20px;">Asistente</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://saveyourlife.streamlit.app/Brain Tumor" target="_self" style="color:#d1e9ff;font-size: 20px;">Brain Tumor</a> 
        </li>
        <li class="nav-item">
         <a class="nav-link" href="https://saveyourlife.streamlit.app/About me" target="_self" style="color:#d1e9ff;font-size: 20px;">About me</a>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Introduzca su búsqueda..." aria-label="Search">
        <button class="btn btn-outline-light" type="submit">Buscar</button>
      </form>
    </div>
  </div>
</nav>
"""
st.markdown(menu(), unsafe_allow_html=True)

def fotos():
  return """
<div class="row" style="margin-top: 55px">
      <div class="col-lg-4">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/950a0795b6bab53667a60acd58ec3b8ede9dddeade8c4e8ab2510ae8.png" alt="Mi imagen" style="width:100;height:100px;margin-top:90px">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"/><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>
        <h2 class="fw-normal">Asistente</h2>
        <p>Asistente virtual que te ayudara a todo.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/Asistente" target="_self">IR  &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"/><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>
        <h2 class="fw-normal">Tumor Cerebal</h2>
        <p>Introduce una imagen de radio grafia cerebal y veremos que tal estas.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/Brain Tumor" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="#777"/><text x="50%" y="50%" fill="#777" dy=".3em">140x140</text></svg>
        <h2 class="fw-normal">Sobre Nosotros</h2>
        <p>Somos nosotros.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/About me" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
    </div><!-- /.row -->
"""
st.markdown(fotos(), unsafe_allow_html=True)

def testo():
  return """
<div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">¿A qué nos dedicamos?</h2>
        <p>La página web del SaveYourLife de Predicción de Tumores es un sitio enfocado a brindar información y servicios relacionados con la detección temprana y la predicción de tumores mediante el uso de inteligencia artificial. En la página principal, los visitantes pueden encontrar información sobre los trabajos que realizamos, el equipo de investigación, las tecnologías utilizadas y los resultados obtenidos. También se destacan los servicios disponibles, como la detección temprana de cáncer mediante la evaluación de imágenes médicas y la predicción del riesgo de desarrollar ciertos tipos de tumores.</p>
        <p>Además, la página web ofrece acceso a herramientas y recursos para pacientes y profesionales de la salud, como la carga de imágenes para la evaluación médica y la visualización de resultados de investigaciones recientes.</p>
        <p>Los visitantes también pueden acceder a un blog de Twitter actualizado regularmente con noticias, estudios y artículos relacionados con la investigación de tumores y la inteligencia artificial.</p>
      </div>
      <div class="col-md-5">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/9ecfcdb08bc77781235191f7f660d542dc3c03b7b18821471930be11.jpg" alt="Mi imagen" style="width:500px;height:300px;margin-top:90px">
      </div>
    </div>
"""
st.markdown(testo(), unsafe_allow_html=True)

st.markdown("""
  La página web de SaveYourLife de Predicción de Tumores es fácil de navegar y está diseñada para ser accesible tanto para expertos en el tema como para 
  el público en general. La plataforma es moderna y segura, y se encuentra respaldada por un equipo de expertos en tecnología y seguridad informática 
  para garantizar la protección de la información del usuario y la privacidad de los datos.
  """)
col1, col2 = st.columns([9, 20])
with col1:
   st.image('img/inicio_2.jpeg')

with col2:
   st.markdown("""
      ### La detección de tumores mediante MRI y redes neuronales

      La detección de tumores mediante imágenes de resonancia magnética (MRI) y redes neuronales es un proceso complejo que involucra varias etapas.

      Aquí te describo en términos generales cómo funciona este proceso: Adquisición de imágenes:

      El primer paso en la detección de tumores mediante MRI es adquirir imágenes de resonancia magnética de alta calidad. Las imágenes se adquieren 
      en múltiples planos y con diferentes secuencias, lo que permite obtener una vista completa y detallada del área afectada.

      Preprocesamiento de imágenes: Una vez que se adquieren las imágenes de resonancia magnética, se deben preprocesar para mejorar la calidad de la 
      imagen y reducir el ruido. Esto se logra mediante técnicas de filtrado y normalización.""")

st.markdown("""Segmentación de imágenes: La siguiente etapa consiste en segmentar la imagen para identificar el área donde se encuentra el tumor. Esto se realiza 
  mediante la aplicación de técnicas de segmentación de imágenes, que pueden ser manuales o automáticas.

  Extracción de características: Una vez que se identifica el área donde se encuentra el tumor, se extraen características de la imagen que son relevantes 
  para la detección de tumores. Las características pueden incluir la forma, el tamaño, la textura y la intensidad de los píxeles en la región del tumor.

  Entrenamiento de la red neuronal: Las características extraídas se utilizan para entrenar una red neuronal para que pueda clasificar las imágenes como 
  positivas o negativas para tumores. Durante el entrenamiento, la red neuronal ajusta los pesos de las conexiones entre las neuronas para mejorar su precisión 
  en la clasificación de imágenes.

  Validación y evaluación del modelo: Una vez que la red neuronal está entrenada, se utiliza para validar y evaluar el modelo. Esto se hace comparando la 
  salida de la red neuronal con los resultados reales de un conjunto de datos de prueba. Se utilizan métricas de evaluación como la sensibilidad, especificidad y 
  precisión para determinar la precisión del modelo en la detección de tumores.

  En resumen, la detección de tumores mediante imágenes de resonancia magnética y redes neuronales es un proceso complejo que involucra la adquisición de \
  imágenes, el preprocesamiento de imágenes, la segmentación de imágenes, la extracción de características, el entrenamiento de la red neuronal y la validación y \
  evaluación del modelo. A través de esta metodología, se pueden obtener resultados precisos y eficientes para la detección temprana de tumores.
  """)

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
#CCS
importar_css('.streamlit/style.css')
importar_css('bootstrap/css/bootstrap.min.css')
