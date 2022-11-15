import rebound
from ipywidgets import HBox, VBox
sim = rebound.Simulation()
sim.getWidget()

sim.add(m=1) # add a star

for i in range(10):
    sim.add(m=1e-3,a=0.4+0.1*i,inc=0.03*i,omega=5.*i) # Jupiter mass planets on close orbits
sim.move_to_com() # Move to the centre of mass frame

sim.integrate(500)

sim.getWidget(size=(400,200),orbits=False)

widget_1 = sim.getWidget(orientation=(0,0,0,1),scale=2)
widget_2 = sim.getWidget(orientation=(0,1,0,1),scale=2,size=(50,200))
widget_3 = sim.getWidget(orientation=(1,0,0,1),scale=2,size=(200,50))

VBox((widget_3,HBox((widget_1, widget_2))))

sim.integrate(800)
