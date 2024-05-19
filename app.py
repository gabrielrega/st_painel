from bcb import sgs
import streamlit as st

df = sgs.get({'IPCA': 433}, start='2002-02-01')
st.line_chart(df)