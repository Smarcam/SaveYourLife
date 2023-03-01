from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import streamlit as st
# LINK TO THE CSS FILE
def importar_css():
  with open('.streamlit/style.css')as f:
     st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
# selenium
chrome_options = Options()
chrome_options.add_argument("--headless") # Para ejecutar en modo headless
driver = webdriver.Chrome(options=chrome_options)
def navigate_to_search(term):
    driver.get(f"https://www.google.com/search?q={term}")
