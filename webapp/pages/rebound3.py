import rebound
import streamlit as st
import datetime
import pandas as pd

sim = rebound.Simulation()

mercury = st.checkbox('Mercury')
venus = st.checkbox('Venus')
earth = st.checkbox('Earth')
jupiter = st.checkbox('Jupiter')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)
sim.add("Sun")

if mercury:
    sim.add("Mercury", date = d)
if venus:
    sim.add("Venus", date = d)
if earth:
    sim.add("Earth", date = d)
if jupiter:
    sim.add("Jupiter", date = d)
 
fig, ax = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
st.write('You selected:', d)
