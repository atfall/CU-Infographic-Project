import rebound
import streamlit as st
import pandas as pd
import datetime
#import mpld3
#import streamlit.components.v1 as components
import matplotlib.pyplot as plt

sim_in = rebound.Simulation()
sim_out = rebound.Simulation()
sim_sb = rebound.Simulation()
sim_sb_out = rebound.Simulation()
sim_sun = rebound.Simulation()

col1, col2= st.columns(2)
with col1:
   st.header("Inner Solar System")
   st.write("Planets")
   mercury = st.checkbox('Mercury', value = True)
   venus = st.checkbox('Venus')
   earth = st.checkbox('Earth', value = True)
   mars = st.checkbox('Mars')
   st.write("Small Bodies")
   ceres = st.checkbox('Ceres', value = True)
   pallas = st.checkbox('Pallas', value = True)
   vesta = st.checkbox('Vesta')
                    
with col2:
   st.header("Outer Solar System")
   jupiter = st.checkbox('Jupiter', value = True)
   saturn = st.checkbox('Saturn')
   uranus = st.checkbox('Uranus')
   neptune = st.checkbox('Neptune')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)

sim_in.add("Sun")
sim_out.add("Sun")

body_type = []
colour = []

if mercury:
    sim_in.add("Mercury", date = d)
    body_type.append("Planet")
    colour.append("Red")
if venus:
    sim_in.add("Venus", date = d)
    body_type.append("Planet")
    colour.append("Black")
if earth:
    sim_in.add("Earth", hash = "Earth", date = d)
    body_type.append("Planet")
    colour.append("Black")
if mars:
    sim_in.add("Mars", date = d)
    body_type.append("Planet")
    colour.append("Black")
if ceres:
   sim_in.add("Ceres", hash = "Ceres", date = d)
   body_type.append("Dwarf")
   colour.append("Gray")
if pallas:
   sim_in.add("Pallas", hash = "Pallas", date = d)
   body_type.append("Dwarf")
   colour.append("Gray")
if vesta:
   sim_in.add("Vesta", hash = "Vesta", date = d)
   body_type.append("Dwarf")
   colour.append("Gray")
    
if jupiter:
    sim_out.add("Jupiter", date = d)
if saturn:
    sim_out.add("Saturn", date = d)
if uranus:
    sim_out.add("Uranus", date = d)
if neptune:
    sim_out.add("Neptune", date = d)

#never integrate ever!
op1 = rebound.OrbitPlot(sim_in)
for i in range(len(body_type)):
  if body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(colour)

st.pyplot(op1.fig)
