import streamlit as st
import chart1
import chart2
import chart3

st.set_page_config(page_title="Multi Tab App", layout="wide")

st.title("📊 Streamlit Multi-Tab Dashboard")

tab1, tab2, tab3 = st.tabs([
    "📈 Line Chart",
    "📊 Bar Chart",
    "🎯 Scatter Plot"
])

with tab1:
    chart1.show()

with tab2:
    chart2.show()

with tab3:
    chart3.show()
