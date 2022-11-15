import rebound
import streamlit as st

sim = rebound.Simulation()

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter'],
    ['Earth'])

sim.add("Sun")

if 'Mercury' in options:
    sim.add("Mercury")
if 'Venus' in options:
    sim.add("Venus")
if 'Earth' in options:
    sim.add("Mars")
if 'Jupiter' in options:
    sim.add("Jupiter")
 
fig, ax = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
