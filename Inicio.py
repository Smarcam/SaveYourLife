import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from PIL import Image
import src.search as srch
import src.load_event as le
from functions import *

st.set_page_config(
	page_title = 'SaveYourLife Tumor Brain Predict!',
	page_icon = 'img/icon.png',
	layout = 'wide',
	initial_sidebar_state = 'collapsed',
	)

add_page_title() # By default this also adds indentation

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Inicio.py", "Inicio, "🏠"),
        Page("pages/Brain_tumor_predict.py", "Tumor Brain Predict", ":books:"),
	Page("pages/About_me.py", "Sobre Nosotros", ":books:"),
	Page("pages/Asistente.py", "Asistente", ":books:"),     Asistente
        Section("My section", icon="🎈️"),
        # Pages after a section will be indented
        Page("Another page", icon="💪"),
    ]
)

title_container = st.container()
col1, col2 = st.columns([3, 20])

image = Image.open('img/logo.png')

with title_container:
   with col1:
      st.image(image, width=130)
   with col2:
      st.markdown('<h1 style="color: #28cffe;">SaveYourLife</h1>',unsafe_allow_html=True)

st.header("Buscador")
term = st.text_input("Introduzca su búsqueda:")
if term:
   srch.on_enter_pressed(term) # Busca cuando se presiona Enter en el cuadro de texto

col1, col2 = st.columns([20, 8])
with col1:
   st.markdown('La página web del SaveYourLife de Predicción de Tumores es un sitio dedicado a brindar información y servicios relacionados con\
      la detección temprana y la predicción de tumores mediante el uso de inteligencia artificial. En la página principal, los visitantes pueden encontrar información\
      sobre los trabajos que realizamos, el equipo de investigación, las tecnologías utilizadas y los resultados obtenidos. También se destacan los servicios disponibles, como la detección\
      temprana de cáncer mediante la evaluación de imágenes médicas y la predicción del riesgo de desarrollar ciertos tipos de tumores.')

   st.markdown('Además, la página web ofrece acceso a herramientas y recursos para pacientes y profesionales de la salud, como la carga de imagenes para la evaluación médica\
      y la visualización de resultados de investigaciones recientes.')

   st.markdown('Los visitantes también pueden acceder a un blog de twitter actualizado regularmente con noticias, estudios\
      y artículos relacionados con la investigación de tumores y la inteligencia artificial.')

   st.markdown('La página web de SaveYourLife de Predicción de Tumores es fácil de navegar y está diseñada para ser accesible tanto para expertos\
      en el tema como para el público en general. La plataforma es moderna y segura, y\
      se encuentra respaldada por un equipo de expertos en tecnología y seguridad informática para garantizar la protección de la información del usuario y la privacidad de los datos.')

with col2:
   st.image('img/inicio.jpeg')

col1, col2 = st.columns([9, 20])
with col1:
   st.image('img/inicio_2.jpeg')

with col2:
   st.markdown('### La detección de tumores mediante MRI y redes neuronales')

   st.markdown('La detección de tumores mediante imágenes de resonancia magnética (MRI) y redes neuronales es un proceso complejo que involucra varias etapas.')

   st.markdown('Aquí te describo en términos generales cómo funciona este proceso: Adquisición de imágenes:')

   st.markdown('El primer paso en la detección de tumores mediante MRI es adquirir imágenes de resonancia magnética de alta calidad. Las imágenes se adquieren \
      en múltiples planos y con diferentes secuencias, lo que permite obtener una vista completa y detallada del área afectada.')

   st.markdown('Preprocesamiento de imágenes: Una vez que se adquieren las imágenes de resonancia magnética, se deben preprocesar para mejorar la calidad de la \
      imagen y reducir el ruido. Esto se logra mediante técnicas de filtrado y normalización.')
   st.markdown('Segmentación de imágenes: La siguiente etapa consiste en segmentar la imagen para identificar el área donde se encuentra el tumor. Esto se realiza \
      mediante la aplicación de técnicas de segmentación de imágenes, que pueden ser manuales o automáticas.')

st.markdown('Extracción de características: Una vez que se identifica el área donde se encuentra el tumor, se extraen características de la imagen que son relevantes \
   para la detección de tumores. Las características pueden incluir la forma, el tamaño, la textura y la intensidad de los píxeles en la región del tumor.')

st.markdown('Entrenamiento de la red neuronal: Las características extraídas se utilizan para entrenar una red neuronal para que pueda clasificar las imágenes como \
   positivas o negativas para tumores. Durante el entrenamiento, la red neuronal ajusta los pesos de las conexiones entre las neuronas para mejorar su precisión en la clasificación de imágenes.')

st.markdown('Validación y evaluación del modelo: Una vez que la red neuronal está entrenada, se utiliza para validar y evaluar el modelo. Esto se hace comparando la \
   salida de la red neuronal con los resultados reales de un conjunto de datos de prueba. Se utilizan métricas de evaluación como la sensibilidad, especificidad y \
   precisión para determinar la precisión del modelo en la detección de tumores.')

st.markdown('En resumen, la detección de tumores mediante imágenes de resonancia magnética y redes neuronales es un proceso complejo que involucra la adquisición de \
   imágenes, el preprocesamiento de imágenes, la segmentación de imágenes, la extracción de características, el entrenamiento de la red neuronal y la validación y \
   evaluación del modelo. A través de esta metodología, se pueden obtener resultados precisos y eficientes para la detección temprana de tumores.')

col1, col2 = st.columns([20, 10])
with col1:
   st.markdown('### Nuestros trabajos')
with col2:
   st.markdown('### Nuestros Blog')

#st.image('img/logo.png')
#st.title("SaveYourLife Tumor Brain Predict!")
col1, col2, col3 = st.columns([10, 10, 10])

with col1:
   # Llama a la función con la ruta de la imagen y la URL de destino
   le.image_clickable("img/cerebro.png", "pages/Brain_tumor_predict.py")
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
css = importar_css()

