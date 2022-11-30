import rebound
import streamlit as st
import pandas as pd
import datetime
#import mpld3
#import streamlit.components.v1 as components
import matplotlib.pyplot as plt

sim_in = rebound.Simulation()
sim_out = rebound.Simulation()

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
   st.write("Small Bodies")
   orcus = st.checkbox('Orcus', value = True)
   pluto = st.checkbox('Pluto', value = True)
   haumea = st.checkbox('Haumea', value = True)
   quaoar = st.checkbox('Quaoar', value = True)
   makemake = st.checkbox('Makemake', value = True)
   gonggong = st.checkbox('Gonggong', value = True)
   eris = st.checkbox('Eris', value = True)
   sedna = st.checkbox('Sedna', value = True)

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)

sim_in.add("Sun")
sim_out.add("Sun")

is_body_type = []
is_colour = []
os_body_type = []
os_colour = []

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
if orcus:
   sim_out.add("Orcus", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if pluto:
   sim_out.add("Pluto", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if haumea:
   sim_out.add("Haumea", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if quaoar:
   sim_out.add("Quaoar", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if makemake:
   sim_out.add("Makemake", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if gonggong:
   sim_out.add("Gonggong", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if eris:
   sim_out.add("Eris", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if sedna:
   sim_out.add("Sedna", date = d)
   os_body_type.append("Dwarf")
   os_colour.append("Gray")

#never integrate ever!
op1 = rebound.OrbitPlot(sim_in)
for i in range(len(is_body_type)):
  if is_body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(is_colour)
 
op2 = rebound.OrbitPlot(sim_out)
for i in range(len(os_body_type)):
  if os_body_type[i] == "Dwarf":
    op2.orbits[i].set_linestyle("--")
    op2.particles.set_color(os_colour)

col_in, col_out= st.columns(2)
with col_in:
   st.header("Inner Solar System")
   st.pyplot(op1.fig)
with col_out:
   st.header("Outer Solar System")
   st.pyplot(op2.fig)