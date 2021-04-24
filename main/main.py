import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as pt

st.title("Test application")

st.sidebar.header('User input')

uploaded_file = st.sidebar.file_uploader("Upload your input file (CSV)")
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
