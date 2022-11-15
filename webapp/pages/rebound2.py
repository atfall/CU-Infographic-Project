import rebound
import streamlit as st

options = st.multiselect(
    'What are your favorite colors',
    ['Mercury', 'Venus', 'Earth', 'Mars'])

#def planets(choices):
#    if 'Mercury' in choices:
#        sim.add("Mercury")
 
#if options is not null:
#    planets(options) 
#fig = rebound.OrbitPlot(sim)
#st.pyplot(fig)
st.write('You selected:', options)
