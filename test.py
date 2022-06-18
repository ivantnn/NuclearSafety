import streamlit as st
from streamlit_lottie import st_lottie
import json


def load_lottie(filepath:str):
	with open(filepath,"r") as f:
		return json.load(f)



load_file1 = load_lottie('output.mp4.lottie.json')
load_file2 = load_lottie('out.mp4.lottie.json')
#n = open('out2.mp4','rb')
#b = n.read()
#st.video(b)
st.write('Here is a CFD video of a fire due to Propane')
st_lottie(load_file1,
	speed=1,
	reverse=False,
	quality="high")

st.write('Here is a CFD video of the firsts miliseconds of a hydrogen combustion')
st_lottie(load_file2,
	speed=1,
	reverse=False,
	quality="high")
st.write("Made by Ivan Tonon for $Nuclear$ $Safety$ course's final assessment")
st.write("Professors: Cesar Queral, Eduardo Gallego and Gonzalo Jimenez")
