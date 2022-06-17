import streamlit as st

n = open('out2.mp4','rb')
b = n.read()
st.video(b)

st.write('Made by Ivan Tonon for $Nuclear$ $Safety$ course final assessment.')
st.write('Professors: Cesar Queral, Eduardo Gallego and Gonzalo Jimenez')
