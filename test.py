import streamlit as st

n = open('out2.mp4','rb')
b = n.read()
st.video(b)
