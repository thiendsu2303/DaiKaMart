import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Config trang -----------------------------------------
st.set_page_config(
    page_title="Executive Information",
    page_icon="📊",
    layout="wide"
)

# Tieu de
col1, col2, col3 = st.columns([1,6,1])
with col1:
    st.write("")
with col2:
    st.markdown("<h1 style='text-align: center; color: #B799FF;'>EXECUTIVE</h1>", unsafe_allow_html=True)
    st.markdown("---", unsafe_allow_html=True)
with col3:
    st.write("")