import streamlit as st
# LINK TO THE CSS FILE
def importar_css():
  with open('.streamlit/style.css')as f:
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
