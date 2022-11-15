import rebound
import streamlit as st
import datetime
import pandas as pd

sim = rebound.Simulation()

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'],
    ['Earth'])

d = st.date_input(
    "When's your birthday",
    pd.to_dateinput('today'))

sim.add("Sun")

if 'Mercury' in options:
    sim.add("Mercury", date = d)
if 'Venus' in options:
    sim.add("Venus", date = d)
if 'Earth' in options:
    sim.add("Mars", date = "2022-9-9")
if 'Jupiter' in options:
    sim.add("Jupiter", date = d)
 
fig, ax = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
