import streamlit as st
from streamlit_lottie import st_lottie
import json


def load_lottie(filepath:str):
	with open(filepath,"r") as f:
		return json.load(f)

load_file = load_lottie('out.mp4.lottie.json')
#n = open('out2.mp4','rb')
#b = n.read()
#st.video(b)
st_lottie(load_file,
	speed=1,
	reverse=False,
	quality="high")
st.write("Made by Ivan Tonon for $Nuclear$ $Safety$ course's final assessment")
st.write("Professors: Cesar Queral, Eduardo Gallego and Gonzalo Jimenez")
