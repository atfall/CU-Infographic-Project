import rebound
import streamlit as st

sim = rebound.Simulation()

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'])

sim.add("Sun")

if 'Mercury' in options:
    sim.add("Mercury")
if 'Venus' in options:
    sim.add("Venus")
 
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
