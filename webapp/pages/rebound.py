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

st.pyplot(rebound.OrbitPlot(sim))
