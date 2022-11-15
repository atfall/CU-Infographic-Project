import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'])

if 'Mercury' in choices:
    sim.add("Mercury")
if 'Venus' in choices:
    sim.add("Venus")
 
fig = rebound.OrbitPlot(sim)
st.pyplot(fig)
st.write('You selected:', options)
