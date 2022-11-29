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

is_body_type = []
is_colour = []

if mercury:
    sim_in.add("Mercury", date = d)
    is_body_type.append("Planet")
    is_colour.append("Red")
if venus:
    sim_in.add("Venus", date = d)
    is_body_type.append("Planet")
    is_colour.append("Black")
if earth:
    sim_in.add("Earth", hash = "Earth", date = d)
    is_body_type.append("Planet")
    is_colour.append("Black")
if mars:
    sim_in.add("Mars", date = d)
    is_body_type.append("Planet")
    is_colour.append("Black")
if ceres:
   sim_in.add("Ceres", hash = "Ceres", date = d)
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
if pallas:
   sim_in.add("Pallas", hash = "Pallas", date = d)
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
if vesta:
   sim_in.add("Vesta", hash = "Vesta", date = d)
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
    
if jupiter:
    sim_out.add("Jupiter", date = d)
    os_body_type.append("Planet")
    os_colour.append("Black")
if saturn:
    sim_out.add("Saturn", date = d)
    os_body_type.append("Planet")
    os_colour.append("Black")
if uranus:
    sim_out.add("Uranus", date = d)
    os_body_type.append("Planet")
    os_colour.append("Black")
if neptune:
    sim_out.add("Neptune", date = d)
    os_body_type.append("Planet")
    os_colour.append("Black")

#never integrate ever!
op1 = rebound.OrbitPlot(sim_in)
for i in range(len(is_body_type)):
  if is_body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(is_colour)
 
op2 = rebound.OrbitPlot(sim_in)
for i in range(len(os_body_type)):
  if os_body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(os_colour)

st.pyplot(op1.fig)
st.pyplot(op2.fig)
