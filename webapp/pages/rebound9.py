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
inner_bodies = []
outer_bodies = []

if mercury:
    inner_bodies.append("Mercury")
    is_body_type.append("Planet")
    is_colour.append("Red")
if venus:
    inner_bodies.append("Venus")
    is_body_type.append("Planet")
    is_colour.append("Black")
if earth:
    inner_bodies.append("Earth")
    is_body_type.append("Planet")
    is_colour.append("Black")
if mars:
    inner_bodies.append("Mars")
    is_body_type.append("Planet")
    is_colour.append("Black")
if ceres:
   inner_bodies.append("Ceres")
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
if pallas:
   inner_bodies.append("Pallas")
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
if vesta:
   inner_bodies.append("Vesta")
   is_body_type.append("Dwarf")
   is_colour.append("Gray")
    
if jupiter:
    outer_bodies.append("Jupiter")
    os_body_type.append("Planet")
    os_colour.append("Black")
if saturn:
    outer_bodies.append("Saturn")
    os_body_type.append("Planet")
    os_colour.append("Black")
if uranus:
    outer_bodies.append("Uranus")
    os_body_type.append("Planet")
    os_colour.append("Black")
if neptune:
    outer_bodies.append("Neptune")
    os_body_type.append("Planet")
    os_colour.append("Black")
if orcus:
   outer_bodies.append("Orcus")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if pluto:
   outer_bodies.append("Pluto")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if haumea:
   outer_bodies.append("Hauma")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if quaoar:
   outer_bodies.append("Quaoar")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if makemake:
   outer_bodies.append("Makemake")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if gonggong:
   outer_bodies.append("Gonggong")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if eris:
   outer_bodies.append("Eris")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")
if sedna:
   outer_bodies.append("Sedna")
   os_body_type.append("Dwarf")
   os_colour.append("Gray")

#never integrate ever!
for i in range(len(inner_bodies)):
   sim_in.add(inner_bodies[i], date = d)
op1 = rebound.OrbitPlot(sim_in)
for i in range(len(is_body_type)):
  if is_body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(is_colour)

for i in range(len(outer_bodies)):
   sim_out.add(outer_bodies[i], date = d)
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
