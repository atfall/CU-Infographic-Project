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
