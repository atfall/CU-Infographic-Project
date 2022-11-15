import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'],
    ['Jupiter', 'Saturn', 'Uranus', 'Neptune'])

def planets(choices):
    if 'Mercury' in choices:
        sim.add("Mercury")
 

def(options) 
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
