from bcb import sgs
import streamlit as st
import pandas as pd

st.write("""
# My first app
IPCA""")

df = sgs.get({'IPCA': 433}, start='2002-02-01')
st.line_chart(df)

st.write("""SELIC Meta""")

df2 = sgs.get({'Meta': 13521}, start='2002-02-01')
st.bar_chart(df2)