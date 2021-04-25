import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Test application")

st.sidebar.header('User input')

uploaded_file = st.sidebar.file_uploader("Upload your input file (CSV)")
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)

    fig = plt.figure()

    ax = fig.add_subplot(1,1,1)
    ax.scatter(
        input_df['Girth'],
        input_df['Height']
    )

    ax.set_xlabel("Girth (in)")
    ax.set_ylabel("Height (ft)")

    #x = input_df['Girth']
    #y = input_df['Height']
    #plt.plot(x, y)

    st.write(fig)


#fig, axs = plt.subplots(2, sharex=True)
#msft.plot("Index", "Girth (in)", ax=axs[0])
#msft.plot("Index", "Height (ft)", ax=axs[1])
