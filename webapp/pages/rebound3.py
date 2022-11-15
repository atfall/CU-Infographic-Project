import rebound
import streamlit as st
import datetime
import pandas as pd

sim = rebound.Simulation()

mercury = st.checkbox('Mercury')
venus = st.checkbox('Venus')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)
sim.add("Sun")

if 'Mercury' in options:
    sim.add("Mercury", date = d)
if 'Venus' in options:
    sim.add("Venus", date = d)
if 'Earth' in options:
    sim.add("Earth", date = d)
if 'Jupiter' in options:
    sim.add("Jupiter", date = d)
 
fig, ax = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
st.write('You selected:', d)
