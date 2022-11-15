import rebound
import matplotlib.pyplot as plt
import numpy as np

sim = rebound.Simulation()
sim.add("Sun") #Star A
sim.add("Sun", a = 1.)
sim.add("Earth")
sim.move_to_com()
fig = rebound.OrbitPlot(sim)


fig, ax = plt.subplots(figsize=(5,5))
ax.set_aspect("equal")
ps = sim.particles

# manually set plot boundaries
lim = 2.3 
ax.set_xlim([-lim, lim])
ax.set_ylim([-lim, lim])

# plot the stars and planets with separate symbols
for star in ps[:2]:
    ax.scatter(star.x, star.y, s=35, marker='*', facecolor='black', zorder=3)
    
for planet in ps[2:]:
    ax.scatter(planet.x, planet.y, s=10, facecolor='black', zorder=3)
    
# Now individually plot orbit trails with appropriate orbit

from rebound.plotting import fading_line

ABb = ps[2] # circumbinary planet, use default jacobi coordinates
o = np.array(ABb.sample_orbit())
lc = fading_line(o[:,0], o[:,1])
ax.add_collection(lc)

Bb = ps[3] # planet in orbit around B, assign it as primary
o = np.array(Bb.sample_orbit(primary=ps[1]))
lc = fading_line(o[:,0], o[:,1])
ax.add_collection(lc);
