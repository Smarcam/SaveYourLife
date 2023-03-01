import streamlit as st
# LINK TO THE CSS FILE
def importar_css():
  with open('.streamlit/style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
