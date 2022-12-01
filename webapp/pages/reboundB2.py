import rebound
import streamlit as st
import pandas as pd
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import plotly.tools as tls

in_body_type = []
in_colour = []
out_colour = []
out_body_type = []
inner_bodies = []
outer_bodies = []

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)

@st.cache
def init_sim():
	sim = rebound.Simulation()
	sim.add("Sun", date = d)
	sim.add("Mercury", hash = "Mercury", date = d)
	sim.add("Venus", hash = "Venus", date = d)
	sim.add("Earth", hash = "Earth", date = d)
	sim.add("Mars", hash = "Mars", date = d)
	sim.add("Jupiter", hash = "Jupiter", date = d)
	sim.add("Saturn", hash = "Saturn", date = d)
	sim.add("Uranus", hash = "Uranus", date = d)
	sim.add("Neptune", hash = "Neptune", date = d)
	sim.add("Ceres", hash = "Ceres", date = d)
	sim.add("Orcus", hash = "Orcus", date = d)
	sim.add("Pluto", hash = "Pluto", date = d)
	sim.add("Haumea", hash = "Haumea", date = d)
	sim.add("Quaoar", hash = "Quaoar", date = d)
	sim.add("Makemake", hash = "Makemake", date = d)
	sim.add("Gonggong", hash = "Gonggong", date = d)
	sim.add("Eris", hash = "Eris", date = d)
	sim.add("Sedna", hash = "Sedna", date = d)
    return sim

sim = init_sim()

st.write("Planets")
planets = st.checkbox('Planets', value = True)

st.write("Dwarf Planets")
col1, col2, col3= st.columns(3)
with col1:
   ceres = st.checkbox('Ceres', value = True)
   orcus = st.checkbox('Orcus', value = True)
   pluto = st.checkbox('Pluto', value = True)
                    
with col2:
   haumea = st.checkbox('Haumea', value = True)
   quaoar = st.checkbox('Quaoar', value = True)
   makemake = st.checkbox('Makemake', value = True)

with col3:
   gonggong = st.checkbox('Gonggong', value = True)
   eris = st.checkbox('Eris', value = True)
   sedna = st.checkbox('Sedna')

def update():
    if planets:
        inner_bodies.append("Mercury")
        in_body_type.append("Planet")
        in_colour.append("Gray") 
        inner_bodies.append("Venus")
        in_body_type.append("Planet")
        in_colour.append("Brown") 
        inner_bodies.append("Earth")
        in_body_type.append("Planet")
        in_colour.append("Blue") 
        inner_bodies.append("Mars")
        in_body_type.append("Planet")
        in_colour.append("Red") 
        outer_bodies.append("Jupiter")
        out_body_type.append("Planet")
        out_colour.append("Orange") 
        outer_bodies.append("Saturn")
        out_body_type.append("Planet")
        out_colour.append("Gold") 
        outer_bodies.append("Uranus")
        out_body_type.append("Planet")
        out_colour.append("Green") 
        outer_bodies.append("Neptune")
        out_body_type.append("Planet")
        out_colour.append("Blue") 

    if ceres:
        inner_bodies.append("Ceres")
        in_body_type.append("Dwarf")
        in_colour.append("Gray")    

    if orcus:
        outer_bodies.append("Orcus")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if pluto:
        outer_bodies.append("Pluto")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if haumea:
        outer_bodies.append("Haumea")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if quaoar:
        outer_bodies.append("Quaoar")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if makemake:
        outer_bodies.append("Makemake")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if gonggong:
        outer_bodies.append("Gonggong")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if eris:
        outer_bodies.append("Eris")
        out_body_type.append("Dwarf")
        out_colour.append("Gray")
    if sedna:
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
