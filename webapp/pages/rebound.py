import streamlit as st
import mpld3
import streamlit.components.v1 as components
import rebound

sim = rebound.Simulation()

sim.add("Sun")
sim.add("Mercury")
sim.add("Venus")
sim.add("Earth")
sim.add("Mars")
sim.add("Jupiter")
sim.add("Saturn")
sim.add("Uranus")
sim.add("Neptune")

fig, ax = rebound.OrbitPlot(sim)

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)


sim = rebound.Simulation()

sim.add("Sun")
sim.add("Mercury")
sim.add("Venus")
sim.add("Earth")
sim.add("Mars")

fig, ax = rebound.OrbitPlot(sim)

fig_html = mpld3.fig_to_html(fig)
components.html(fig_html, height=600)
