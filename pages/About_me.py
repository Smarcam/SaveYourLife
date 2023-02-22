import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
icon = Image.open('img/icon.png')
st.set_page_config(
	page_title = 'SaveYourLife Tumor Brain Predict!',
	page_icon = icon,
	layout = 'wide',
	initial_sidebar_state = 'collapsed',
	menu_items={
		'Get Help': 'https://streamlit.io',
		'Report a bug': 'https://github.com',
		'About':'About your application: **Hello World!**'
	}
	)
st.sidebar.title("Main Menu")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)
# LINK TO THE CSS FILE
with open('.streamlit/style.css')as f:
 st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
