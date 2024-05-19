from bcb import sgs
import streamlit as st

st.write("""
# My first app
Hello *world!*
""")

df = sgs.get({'IPCA': 433}, start='2002-02-01')
st.line_chart(df)