import rebound
import streamlit as st
import pandas as pd
import datetime
#import mpld3
#import streamlit.components.v1 as components
import matplotlib.pyplot as plt

sim = rebound.Simulation()


col1, col2= st.columns(2)
with col1:
   st.header("Inner Solar System")
   st.write("Planets")
   planets = st.checkbox('Planets', value = True)
                    
with col2:
   st.write("Small Bodies")
   ceres = st.checkbox('Ceres', value = True)
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

sim.add("Sun")

body_type = []
colour = []
inner_bodies = []
outer_bodies = []

if planets:
   sim.add("Mercury", hash = "Mercury", date = d)
   inner_bodies.append("Mercury")
   body_type.append("Planet")
   colour.append("Gray") 
   sim.add("Venus", hash = "Venus", date = d)
   inner_bodies.append("Venus")
   body_type.append("Planet")
   colour.append("Brown") 
   sim.add("Earth", hash = "Earth", date = d)
   inner_bodies.append("Earth")
   body_type.append("Planet")
   colour.append("Blue") 
   sim.add("Mars", hash = "Mars", date = d)
   inner_bodies.append("Mars")
   body_type.append("Planet")
   colour.append("Red") 
   sim.add("Jupiter", hash = "Jupiter", date = d)
   outer_bodies.append("Jupiter")
   body_type.append("Planet")
   colour.append("Orange") 
   sim.add("Saturn", hash = "Saturn", date = d)
   outer_bodies.append("Saturn")
   body_type.append("Planet")
   colour.append("Gold") 
   sim.add("Uranus", hash = "Uranus", date = d)
   outer_bodies.append("Uranus")
   body_type.append("Planet")
   colour.append("Green") 
   sim.add("Neptune", hash = "Neptune", date = d)
   outer_bodies.append("Neptune")
   body_type.append("Planet")
   colour.append("Blue") 

if ceres:
   sim.add("Ceres", hash = "Ceres", date = d)
   inner_bodies.append("Ceres")
   body_type.append("Dwarf")
   colour.append("Gray")    

if orcus:
   sim.add("Orcus", hash = "Orcus", date = d)
   outer_bodies.append("Orcus")
   body_type.append("Dwarf")
   colour.append("Gray")
if pluto:
   sim.add("Pluto", hash = "Pluto", date = d)
   outer_bodies.append("Pluto")
   body_type.append("Dwarf")
   colour.append("Gray")
if haumea:
   sim.add("Haumea", hash = "Haumea", date = d)
   outer_bodies.append("Haumea")
   body_type.append("Dwarf")
   colour.append("Gray")
if quaoar:
   sim.add("Quaoar", hash = "Quaoar", date = d)
   outer_bodies.append("Quaoar")
   body_type.append("Dwarf")
   colour.append("Gray")
if makemake:
   sim.add("Makemake", hash = "Makemake", date = d)
   outer_bodies.append("Makemake")
   body_type.append("Dwarf")
   colour.append("Gray")
if gonggong:
   sim.add("Gonggong", hash = "Gonggong", date = d)
   outer_bodies.append("Gonggong")
   body_type.append("Dwarf")
   colour.append("Gray")
if eris:
   sim.add("Eris", hash = "Eris", date = d)
   outer_bodies.append("Eris")
   body_type.append("Dwarf")
   colour.append("Gray")
if sedna:
   sim.add("Sedna", hash = "Sedna", date = d)
   outer_bodies.append("Sedna")
   body_type.append("Dwarf")
   colour.append("Gray")

#never integrate ever!
op1 = rebound.OrbitPlot(sim, particles = inner_bodies)
for i in range(len(body_type)):
  if body_type[i] == "Dwarf":
    op1.orbits[i].set_linestyle("--")
    op1.particles.set_color(colour)


op2 = rebound.OrbitPlot(sim,  particles = outer_bodies)
for i in range(len(body_type)):
  if body_type[i] == "Dwarf":
    op2.orbits[i].set_linestyle("--")
    op2.particles.set_color(colour)

col_in, col_out= st.columns(2)
with col_in:
   st.header("Inner Solar System")
   st.pyplot(op1.fig)
with col_out:
   st.header("Outer Solar System")
   st.pyplot(op2.fig)
