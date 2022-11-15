import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'],
    ['Jupiter', 'Saturn', 'Uranus', 'Neptune'])

def planets(choices):
    match choices:
        case 'Mercury':
            sim.add("Mercury")
        case 'Venus':
            sim.add("Venus")
        case 'Earth':
            sim.add("Earth")

    
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
