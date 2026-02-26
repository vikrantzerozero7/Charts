import streamlit as st
import pandas as pd
import numpy as np

def show():
    st.subheader("Scatter Plot")

    df = pd.DataFrame({
        "x": np.random.randn(100),
        "y": np.random.randn(100)
    })

    st.scatter_chart(df)
