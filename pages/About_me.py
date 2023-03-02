import pandas as pd
import numpy as np
import streamlit as st
import streamlit.components.v1 as components
from functions import *

#PageConfig
page_config = importar_config()

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"])

st.bar_chart(chart_data)

#CSS
css = importar_css()
