import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from st_pages import show_pages_from_config
from functions import *

#PageConfig
page_config = importar_config()
show_pages_from_config()
#Menu
menu = menu()
#Footer
footer = footer()

st.markdown(menu, unsafe_allow_html=True)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

#footer       
st.markdown(footer, unsafe_allow_html=True)
#CCS
importar_css('.streamlit/stylefooter.css') 
importar_css('bootstrap/css/bootstrap.min.css')
importar_css('.streamlit/style.css')
