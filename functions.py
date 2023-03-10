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
          <a class="nav-link" href="https://saveyourlife.streamlit.app/~/+/Detector De Tumor Cerebral" target="_self" style="color:#d1e9ff;font-size: 20px;">Detector De Tumor Cerebral</a> 
        </li>
        <li class="nav-item">
         <a class="nav-link" href="https://saveyourlife.streamlit.app/~/+/Sobre Nosotros" target="_self" style="color:#d1e9ff;font-size: 20px;">Sobre Nosotros</a>
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
        <p>Introduce una imagen de radio graf??a cerebral y veremos que tal estas.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/~/+/Detector De Tumor Cerebral" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
      <div class="col-lg-4">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/93fd3ac7283a17deb7cf31fad8ecaa703bd9e169ca706a636245461f.png" alt="Mi imagen" style="width: 100px; position: absolute;margin-left: 20px;margin-top: 23px;">
        <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: 140x140" preserveAspectRatio="xMidYMid slice" focusable="false"><title>Placeholder</title><rect width="100%" height="100%" fill="rgba(0, 137, 177, 0.57)"/><text x="50%" y="50%" fill="rgba(0, 137, 177, 0.57)" dy=".3em"></text></svg>
        <h2 class="fw-normal">Sobre Nosotros</h2>
        <p>Somos Miguel ??ngel y Samuel. Hemos creado un modelo el cual permite introducir una Imagen MRI del cerebro y ver si est?? sano.</p>
        <p><a class="btn btn btn-info" href="https://saveyourlife.streamlit.app/~/+/Sobre Nosotros" target="_self">IR &raquo;</a></p>
      </div><!-- /.col-lg-4 -->
    </div><!-- /.row -->
"""
#CARDS WITH TEXT AND IMAGE
def cards():
  return """
<div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">??A qu?? nos dedicamos?</h2>
        <p>La p??gina web del SaveYourLife de Predicci??n de Tumores es un sitio enfocado a brindar informaci??n y servicios relacionados con la detecci??n temprana y la predicci??n de tumores mediante el uso de inteligencia artificial. En la p??gina principal, los visitantes pueden encontrar informaci??n sobre los trabajos que realizamos, el equipo de investigaci??n, las tecnolog??as utilizadas y los resultados obtenidos. Tambi??n se destacan los servicios disponibles, como la detecci??n temprana de c??ncer mediante la evaluaci??n de im??genes m??dicas y la predicci??n del riesgo de desarrollar ciertos tipos de tumores.</p>
        <p>Adem??s, la p??gina web ofrece acceso a herramientas y recursos para pacientes y profesionales de la salud, como la carga de im??genes para la evaluaci??n m??dica y la visualizaci??n de resultados de investigaciones recientes.</p>
        <p>Los visitantes tambi??n pueden acceder a un blog de Twitter actualizado regularmente con noticias, estudios y art??culos relacionados con la investigaci??n de tumores y la inteligencia artificial.</p>
      </div>
      <div class="col-md-5">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/bc45eaa9d7d95ba35fdb13cfadf6410841e8b5c72a28c72aa1fadde0.jpg" alt="Mi imagen" style="max-width:1000px;width:100%;height:auto;margin-top:100px;">
      </div>
</div>
<div class="row featurette">
      <div class="col-md-7">
        <h2 class="featurette-heading fw-normal lh-1">??Que hace nuestra app?</h2>
        <p>La p??gina web de SaveYourLife de Predicci??n de Tumores es f??cil de navegar y est?? dise??ada para ser accesible tanto para expertos en el tema como para el p??blico en general. La plataforma es moderna y segura, y se encuentra respaldada por un equipo de expertos en tecnolog??a y seguridad inform??tica para garantizar la protecci??n de la informaci??n del usuario y la privacidad de los datos.</p>
        <p>La detecci??n de tumores mediante MRI y redes neuronales La detecci??n de tumores mediante im??genes de resonancia magn??tica (MRI) y redes neuronales es un proceso complejo que involucra varias etapas. Aqu?? te describo en t??rminos generales c??mo funciona este proceso: Adquisici??n de im??genes: El primer paso en la detecci??n de tumores mediante MRI es adquirir im??genes de resonancia magn??tica de alta calidad. Las im??genes se adquieren en m??ltiples planos y con diferentes secuencias, lo que permite obtener una vista completa y detallada del ??rea afectada. Preprocesamiento de im??genes: Una vez que se adquieren las im??genes de resonancia magn??tica, se deben preprocesar para mejorar la calidad de la imagen y reducir el ruido. Esto se logra mediante t??cnicas de filtrado y normalizaci??n.</p>
        <p>Segmentaci??n de im??genes: La siguiente etapa consiste en segmentar la imagen para identificar el ??rea donde se encuentra el tumor. Esto se realiza mediante la aplicaci??n de t??cnicas de segmentaci??n de im??genes, que pueden ser manuales o autom??ticas. Extracci??n de caracter??sticas: Una vez que se identifica el ??rea donde se encuentra el tumor, se extraen caracter??sticas de la imagen que son relevantes para la detecci??n de tumores. Las caracter??sticas pueden incluir la forma, el tama??o, la textura y la intensidad de los p??xeles en la regi??n del tumor. Entrenamiento de la red neuronal: Las caracter??sticas extra??das se utilizan para entrenar una red neuronal para que pueda clasificar las im??genes como positivas o negativas para tumores. Durante el entrenamiento, la red neuronal ajusta los pesos de las conexiones entre las neuronas para mejorar su precisi??n en la clasificaci??n de im??genes. Validaci??n y evaluaci??n del modelo: Una vez que la red neuronal est?? entrenada, se utiliza para validar y evaluar el modelo. Esto se hace comparando la salida de la red neuronal con los resultados reales de un conjunto de datos de prueba. Se utilizan m??tricas de evaluaci??n como la sensibilidad, especificidad y precisi??n para determinar la precisi??n del modelo en la detecci??n de tumores. En resumen, la detecci??n de tumores mediante im??genes de resonancia magn??tica y redes neuronales es un proceso complejo que involucra la adquisici??n de im??genes, el preprocesamiento de im??genes, la segmentaci??n de im??genes, la extracci??n de caracter??sticas, el entrenamiento de la red neuronal y la validaci??n y evaluaci??n del modelo. A trav??s de esta metodolog??a, se pueden obtener resultados precisos y eficientes para la detecci??n temprana de tumores.</p>
      </div>
      <div class="col-md-5">
        <img src="https://saveyourlife.streamlit.app:443/~/+/media/9ecfcdb08bc77781235191f7f660d542dc3c03b7b18821471930be11.jpg" alt="Mi imagen" style="max-width:1000px;width:100%;height:auto;margin-top:100px;">
      </div>
</div>
"""
#FOOTER
def footermain():
  return """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
<div class="wrapper">
    <div class="button">
      <div class="icon">
          <i class="fab fa-python"></i>
      </div>
      <span>V.3.10</span>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Samuel</span>
      <a href="https://www.linkedin.com/in/samuelmc-dev/">??????</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-github"></i>
      </div>
      <span>Github</span>
      <a href="https://github.com/Smarcam/SaveYourLife">??????</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Miguel ??</span>
      <a href="https://www.linkedin.com/in/mortdur/">??????</a>
    </div>
</div>
"""
#FOOTER
def footer():
  return """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"/>
<div style="position: fixed;bottom: 230px;">
<div class="wrapper">
    <div class="button">
      <div class="icon">
          <i class="fab fa-python"></i>
      </div>
      <span>V.3.10</span>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Samuel</span>
      <a href="https://www.linkedin.com/in/samuelmc-dev/">??????</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-github"></i>
      </div>
      <span>Github</span>
      <a href="https://github.com/Smarcam/SaveYourLife">??????</a>
    </div>
    <div class="button">
      <div class="icon">
          <i class="fab fa-linkedin"></i>
      </div>
      <span>Miguel ??</span>
      <a href="https://www.linkedin.com/in/mortdur/">??????</a>
    </div>
</div>
</div>
"""
#
