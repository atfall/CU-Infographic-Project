import rebound
import streamlit as st
import datetime
import pandas as pd
import mpld3
import streamlit.components.v1 as components
import plotly.express as pe
#%matplotlib notebook

sim = rebound.Simulation()

mercury = st.checkbox('Mercury')
venus = st.checkbox('Venus')
earth = st.checkbox('Earth', value = True)
mars = st.checkbox('Mars')
jupiter = st.checkbox('Jupiter')
saturn = st.checkbox('Saturn')
uranus = st.checkbox('Uranus')
neptune = st.checkbox('Neptune')

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
if mars:
    sim.add("Mars", date = d)
if jupiter:
    sim.add("Jupiter", date = d)
if saturn:
    sim.add("Saturn", date = d)
if uranus:
    sim.add("Uranus", date = d)
if neptune:
    sim.add("Neptune", date = d)
 
fig, ax = rebound.OrbitPlot(sim)
#st.pyplot(fig)
df = pe.fig
fig = pe.plot(df)
fig.show()
