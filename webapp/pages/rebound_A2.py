import rebound
import streamlit as st
import pandas as pd
import datetime
#import mpld3
#import streamlit.components.v1 as components
import matplotlib.pyplot as plt

in_body_type = []
in_colour = []
out_colour = []
out_body_type = []
inner_bodies = []
outer_bodies = []

sim = rebound.Simulation()

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)

col1, col2, col3= st.columns(3)

st.write("Planets")
planets = st.checkbox('Planets', value = True)

st.write("Dwarf Planets")
with col1:
   ceres = st.checkbox('Ceres', value = True)
   orcus = st.checkbox('Orcus', value = True)
   pluto = st.checkbox('Pluto', value = True)
                    
with col2:
   haumea = st.checkbox('Haumea', value = True)
   quaoar = st.checkbox('Quaoar', value = True)
   makemake = st.checkbox('Makemake', value = True)
   gonggong = st.checkbox('Gonggong', value = True)
   eris = st.checkbox('Eris', value = True)
   sedna = st.checkbox('Sedna', value = True)

with col3:
   gonggong = st.checkbox('Gonggong', value = True)
   eris = st.checkbox('Eris', value = True)
   sedna = st.checkbox('Sedna', value = True)
   
sim.add("Sun")

if planets:
   sim.add("Mercury", hash = "Mercury", date = d)
   inner_bodies.append("Mercury")
   in_body_type.append("Planet")
   in_colour.append("Gray") 
   sim.add("Venus", hash = "Venus", date = d)
   inner_bodies.append("Venus")
   in_body_type.append("Planet")
   in_colour.append("Brown") 
   sim.add("Earth", hash = "Earth", date = d)
   inner_bodies.append("Earth")
   in_body_type.append("Planet")
   in_colour.append("Blue") 
   sim.add("Mars", hash = "Mars", date = d)
   inner_bodies.append("Mars")
   in_body_type.append("Planet")
   in_colour.append("Red") 
   sim.add("Jupiter", hash = "Jupiter", date = d)
   outer_bodies.append("Jupiter")
   out_body_type.append("Planet")
   out_colour.append("Orange") 
   sim.add("Saturn", hash = "Saturn", date = d)
   outer_bodies.append("Saturn")
   out_body_type.append("Planet")
   out_colour.append("Gold") 
   sim.add("Uranus", hash = "Uranus", date = d)
   outer_bodies.append("Uranus")
   out_body_type.append("Planet")
   out_colour.append("Green") 
   sim.add("Neptune", hash = "Neptune", date = d)
   outer_bodies.append("Neptune")
   out_body_type.append("Planet")
   out_colour.append("Blue") 

if ceres:
   sim.add("Ceres", hash = "Ceres", date = d)
   inner_bodies.append("Ceres")
   in_body_type.append("Dwarf")
   in_colour.append("Gray")    

if orcus:
   sim.add("Orcus", hash = "Orcus", date = d)
   outer_bodies.append("Orcus")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if pluto:
   sim.add("Pluto", hash = "Pluto", date = d)
   outer_bodies.append("Pluto")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if haumea:
   sim.add("Haumea", hash = "Haumea", date = d)
   outer_bodies.append("Haumea")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if quaoar:
   sim.add("Quaoar", hash = "Quaoar", date = d)
   outer_bodies.append("Quaoar")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if makemake:
   sim.add("Makemake", hash = "Makemake", date = d)
   outer_bodies.append("Makemake")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if gonggong:
   sim.add("Gonggong", hash = "Gonggong", date = d)
   outer_bodies.append("Gonggong")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if eris:
   sim.add("Eris", hash = "Eris", date = d)
   outer_bodies.append("Eris")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")
if sedna:
   sim.add("Sedna", hash = "Sedna", date = d)
   outer_bodies.append("Sedna")
   out_body_type.append("Dwarf")
   out_colour.append("Gray")

#never integrate ever!
op1 = rebound.OrbitPlot(sim, particles = inner_bodies)
op1.particles.set_color(in_colour)
for i in range(len(in_body_type)):
  if in_body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")

op2 = rebound.OrbitPlot(sim,  particles = outer_bodies)
op2.particles.set_color(out_colour)
for i in range(len(out_body_type)):
  if out_body_type[i] == "Dwarf":
    op2.orbits[i].set_linestyle("--")
    
col_in, col_out= st.columns(2)
with col_in:
   st.header("Inner Solar System")
   st.pyplot(op1.fig)
with col_out:
   st.header("Outer Solar System")
   st.pyplot(op2.fig)
