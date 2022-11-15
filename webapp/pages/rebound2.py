import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'],
    ['Jupiter', 'Saturn', 'Uranus', 'Neptune'])

match options:
    case 'Mercury':
        sim.add("Mercury")
    case 'Venus':
        sim.add("Venus")
    case 'Earth':
        sim.add("Earth")
    case _:

    
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
