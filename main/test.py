import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.title("Test application")

st.sidebar.header('Configuration')

plot_type = st.sidebar.radio(
    "Plot type",
    ('Scatter plot', 'Line plot'))

uploaded_file = st.sidebar.file_uploader("Upload your input file (CSV)", type='csv')
if uploaded_file is not None:

    header_list = ["Index", "Girth", "Height", "Volume"]
    input_df = pd.read_csv(uploaded_file)

    x_value = st.selectbox(
    "X-axis",
    ('Girth (in)', 'Height (ft)', 'Volume (cm^3)'))

    y_value = st.selectbox(
    "Y-axis",
    ('Girth (in)', 'Height (ft)', 'Volume (cm^3)'))

    x_label = ''
    y_label = ''

    if x_value == 'Girth (in)':
        x_label = 'Girth'
    elif x_value == 'Height (ft)':
        x_label = 'Height'
    else:
        x_label = 'Volume'

    if y_value == 'Girth (in)':
        y_label = 'Girth'
    elif y_value == 'Height (ft)':
        y_label = 'Height'
    else:
        y_label = 'Volume'

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    if plot_type == 'Scatter plot':
        ax.scatter(
            input_df[x_label],
            input_df[y_label]
        )

    elif plot_type == 'Line plot':
        ax.plot(
            input_df[x_label],
            input_df[y_label]
        )

    #endif

    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    st.write(fig)
