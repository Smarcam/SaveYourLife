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
