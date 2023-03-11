import streamlit as st
# LINK TO THE CSS FILE
def importar_css(archivo):
  with open(archivo)as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# CONFIG FOR PAGE
def importar_config():
  if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False
  st.set_page_config(
      page_title="SaveYourLife Tumor Brain Predict",
      page_icon='img/icon.png',
      initial_sidebar_state="collapsed",
      layout="wide"
  )
# MAIN MENU
def menu():
  return """
<nav class="navbar navbar-expand-md navbar-dark fixed-top" style="background: #0089b1">
  <div class="container-fluid" style="margin-left: 120px">
    <a class="navbar-brand" href="https://saveyourlife.streamlit.app" target="_self"><img src="https://saveyourlife.streamlit.app:443/~/+/media/93fd3ac7283a17deb7cf31fad8ecaa703bd9e169ca706a636245461f.png" alt="Mi imagen" style="width: 50px; margin-top: 0px; margin-left: -60px;"></a>
    <div class="navbar-collapse collapse" id="navbarCollapse" style="margin-left: -20px;">
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
    </div>
  </div>
</nav>
"""
#BRAND
def brand():
  return """
<div class="row" style="margin-top: 55px">
      <div class="col-lg-4">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/93fd3ac7283a17deb7cf31fad8ecaa703bd9e169ca706a636245461f.png" alt="Mi imagen" style="width: 100px; position: absolute;margin-left: 20px;margin-top: 23px;">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="rgba(0, 137, 177, 0.57)"/><text x="50%" y="50%" dy=".3em"></text></svg>
        <h2 class="fw-normal">Asistente</h2>
        <p>Asistente virtual que te ayudara a todo.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/Asistente" target="_self">IR  &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/93fd3ac7283a17deb7cf31fad8ecaa703bd9e169ca706a636245461f.png" alt="Mi imagen" style="width: 100px; position: absolute;margin-left: 20px;margin-top: 23px;">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="rgba(0, 137, 177, 0.57)"/><text x="50%" y="50%" fill="rgba(0, 137, 177, 0.57)" dy=".3em"></text></svg>
        <h2 class="fw-normal">Tumor Cerebal</h2>
        <p>Introduce una imagen de radio grafia cerebal y veremos que tal estas.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/Brain Tumor" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/93fd3ac7283a17deb7cf31fad8ecaa703bd9e169ca706a636245461f.png" alt="Mi imagen" style="width: 100px; position: absolute;margin-left: 20px;margin-top: 23px;">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="rgba(0, 137, 177, 0.57)"/><text x="50%" y="50%" fill="rgba(0, 137, 177, 0.57)" dy=".3em"></text></svg>
        <h2 class="fw-normal">Sobre Nosotros</h2>
        <p>Somos nosotros.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/About me" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
    </div><!-- /.row -->
"""
#CARDS WITH TEXT AND IMAGE
def cards():
  return """
<div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">¿A qué nos dedicamos?</h2>
        <p>La página web del SaveYourLife de Predicción de Tumores es un sitio enfocado a brindar información y servicios relacionados con la detección temprana y la predicción de tumores mediante el uso de inteligencia artificial. En la página principal, los visitantes pueden encontrar información sobre los trabajos que realizamos, el equipo de investigación, las tecnologías utilizadas y los resultados obtenidos. También se destacan los servicios disponibles, como la detección temprana de cáncer mediante la evaluación de imágenes médicas y la predicción del riesgo de desarrollar ciertos tipos de tumores.</p>
        <p>Además, la página web ofrece acceso a herramientas y recursos para pacientes y profesionales de la salud, como la carga de imágenes para la evaluación médica y la visualización de resultados de investigaciones recientes.</p>
        <p>Los visitantes también pueden acceder a un blog de Twitter actualizado regularmente con noticias, estudios y artículos relacionados con la investigación de tumores y la inteligencia artificial.</p>
      </div>
      <div class="col-md-5">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/bc45eaa9d7d95ba35fdb13cfadf6410841e8b5c72a28c72aa1fadde0.jpg" alt="Mi imagen" style="max-width:1000px;width:100%;height:auto;margin-top:100px;">
      </div>
</div>
<div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">¿Que hace nuestra app?</h2>
        <p>La página web de SaveYourLife de Predicción de Tumores es fácil de navegar y está diseñada para ser accesible tanto para expertos en el tema como para el público en general. La plataforma es moderna y segura, y se encuentra respaldada por un equipo de expertos en tecnología y seguridad informática para garantizar la protección de la información del usuario y la privacidad de los datos.</p>
        <p>La detección de tumores mediante MRI y redes neuronales La detección de tumores mediante imágenes de resonancia magnética (MRI) y redes neuronales es un proceso complejo que involucra varias etapas. Aquí te describo en términos generales cómo funciona este proceso: Adquisición de imágenes: El primer paso en la detección de tumores mediante MRI es adquirir imágenes de resonancia magnética de alta calidad. Las imágenes se adquieren en múltiples planos y con diferentes secuencias, lo que permite obtener una vista completa y detallada del área afectada. Preprocesamiento de imágenes: Una vez que se adquieren las imágenes de resonancia magnética, se deben preprocesar para mejorar la calidad de la imagen y reducir el ruido. Esto se logra mediante técnicas de filtrado y normalización.</p>
        <p>Segmentación de imágenes: La siguiente etapa consiste en segmentar la imagen para identificar el área donde se encuentra el tumor. Esto se realiza mediante la aplicación de técnicas de segmentación de imágenes, que pueden ser manuales o automáticas. Extracción de características: Una vez que se identifica el área donde se encuentra el tumor, se extraen características de la imagen que son relevantes para la detección de tumores. Las características pueden incluir la forma, el tamaño, la textura y la intensidad de los píxeles en la región del tumor. Entrenamiento de la red neuronal: Las características extraídas se utilizan para entrenar una red neuronal para que pueda clasificar las imágenes como positivas o negativas para tumores. Durante el entrenamiento, la red neuronal ajusta los pesos de las conexiones entre las neuronas para mejorar su precisión en la clasificación de imágenes. Validación y evaluación del modelo: Una vez que la red neuronal está entrenada, se utiliza para validar y evaluar el modelo. Esto se hace comparando la salida de la red neuronal con los resultados reales de un conjunto de datos de prueba. Se utilizan métricas de evaluación como la sensibilidad, especificidad y precisión para determinar la precisión del modelo en la detección de tumores. En resumen, la detección de tumores mediante imágenes de resonancia magnética y redes neuronales es un proceso complejo que involucra la adquisición de imágenes, el preprocesamiento de imágenes, la segmentación de imágenes, la extracción de características, el entrenamiento de la red neuronal y la validación y evaluación del modelo. A través de esta metodología, se pueden obtener resultados precisos y eficientes para la detección temprana de tumores.</p>
      </div>
      <div class="col-md-5">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/9ecfcdb08bc77781235191f7f660d542dc3c03b7b18821471930be11.jpg" alt="Mi imagen" style="max-width:1000px;width:100%;height:auto;margin-top:100px;">
      </div>
</div>
"""
#FOOTER
def footer():
  return """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
<div class="wrapper">
    <div class="button">
      <div class="icon">
          <i class="fab fa-python"></i>
      </div>
      <span>V.3.10</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Samuel</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-github"></i>
      </div>
      <span>Github</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Miguel Á</span>
      <a href="hola.com">⤴️</a>
    </div>
</div>
"""
#FOOTER
def footerasistente():
  return """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
<div style="position: relative;top: 230px;">
<div class="wrapper">
    <div class="button">
      <div class="icon">
          <i class="fab fa-python"></i>
      </div>
      <span>V.3.10</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Samuel</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-github"></i>
      </div>
      <span>Github</span>
      <a href="hola.com">⤴️</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Miguel Á</span>
      <a href="hola.com">⤴️</a>
    </div>
</div>
</div>
"""
#
