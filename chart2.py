import streamlit as st
import pandas as pd
import numpy as np

def show():
    st.subheader("Bar Chart")

    data = pd.DataFrame(
        np.random.randint(1, 100, (10, 3)),
        columns=["X", "Y", "Z"]
    )

    st.bar_chart(data)
