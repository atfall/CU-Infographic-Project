import rebound
import streamlit as st
import pandas as pd
import datetime
import mpld3
import streamlit.components.v1 as components
import matplotlib.pyplot as plt

sim_in = rebound.Simulation()
sim_out = rebound.Simulation()

col1, col2= st.columns(2)
with col1:
   st.header("Inner Solar System")
   st.write("Planets")
   mercury = st.checkbox('Mercury')
   venus = st.checkbox('Venus')
   earth = st.checkbox('Earth', value = True)
   mars = st.checkbox('Mars')
   st.write("Small Bodies")
   ceres = st.checkbox('Ceres')
   pallas = st.checkbox('Pallas')
   vesta = st.checkbox('Vesta')
                    
with col2:
   st.header("Outer Solar System")
   jupiter = st.checkbox('Jupiter')
   saturn = st.checkbox('Saturn')
   uranus = st.checkbox('Uranus')
   neptune = st.checkbox('Neptune')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)

sim_in.add("Sun")
sim_out.add("Sun")

small_bodies=[]

if mercury:
    sim_in.add("Mercury", date = d)
if venus:
    sim_in.add("Venus", date = d)
if earth:
    sim_in.add("Earth", date = d)
if mars:
    sim_in.add("Mars", date = d)
if ceres:
   sim_in.add("Ceres", hash = "Ceres", date = d)
   small_bodies.append("Ceres")
if pallas:
   sim_in.add("Pallas", hash = "Pallas", date = d)
   small_bodies.append("Pallas")
if vesta:
   sim_in.add("Vesta", hash = "Vesta", date = d)
   small_bodies.append("Vesta")
    
if jupiter:
    sim_out.add("Jupiter", date = d)
if saturn:
    sim_out.add("Saturn", date = d)
if uranus:
    sim_out.add("Uranus", date = d)
if neptune:
    sim_out.add("Neptune", date = d)
 
op1 = rebound.OrbitPlot(sim_in)
if small_bodies:
  op1_2 = rebound.OrbitPlot(sim_in, particles=small_bodies, ax=op1.ax, fig=op1.fig, lw=0.5, color="white")

op2 = rebound.OrbitPlot(sim_out)

col_in, col_out= st.columns(2)
with col_in:
   st.header("Inner Solar System")
   st.pyplot(op1.fig)

with col_out:
   st.header("Outer Solar System")
   st.pyplot(op2.fig)
