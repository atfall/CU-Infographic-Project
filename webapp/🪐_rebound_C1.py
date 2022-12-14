import rebound
import streamlit as st
import pandas as pd


st.title('Bodies in the Solar System')

st.header('Start Date')
date = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(date)


@st.cache(allow_output_mutation=True)
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
	sim.move_to_com()
	return sim


sim = init_sim()

if 'count' not in st.session_state:
	st.session_state.count = 0

in_body_type = []
in_colour = []
out_colour = []
out_body_type = []
inner_bodies = []
outer_bodies = []
days = []

#checkboxes
st.header("Planets")
col1, col2, col3, col4 = st.columns(4)

with col1:
    mercury = st.checkbox('Mercury', value = True)
    jupiter = st.checkbox('Jupiter', value = True)

with col2:
    venus = st.checkbox('Venus', value = True)
    saturn = st.checkbox('Saturn', value = True)

with col3:
    earth = st.checkbox('Earth', value = True)
    uranus = st.checkbox('Uranus', value = True)

with col4:
    mars = st.checkbox('Mars', value = True)
    neptune = st.checkbox('Neptune', value = True)

st.header("Dwarf Planets")
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    ceres = st.checkbox('Ceres', value = True)

with col2:
    pluto = st.checkbox('Pluto', value = True)

with col3:
    haumea = st.checkbox('Haumea', value = True)

with col4:
    makemake = st.checkbox('Makemake', value = True)             

with col5:
    eris = st.checkbox('Eris', value = True)



st.header('Small Solar System Bodies')
col1, col2, col3, col4 = st.columns(4)

with col1:
    orcus = st.checkbox('Orcus')
                 
with col2:
    quaoar = st.checkbox('Quaoar')

with col3:
    gonggong = st.checkbox('Gonggong')

with col4:
    sedna = st.checkbox('Sedna')

#add checked bodies to plot
if mercury:
    inner_bodies.append("Mercury")
    in_body_type.append("Planet")
    in_colour.append("Gray")
if venus:
    inner_bodies.append("Venus")
    in_body_type.append("Planet")
    in_colour.append("Brown")
if earth:
    inner_bodies.append("Earth")
    in_body_type.append("Planet")
    in_colour.append("Blue")
if mars:
    inner_bodies.append("Mars")
    in_body_type.append("Planet")
    in_colour.append("Red")
    
if jupiter:
    outer_bodies.append("Jupiter")
    out_body_type.append("Planet")
    out_colour.append("Orange")
if saturn:
    outer_bodies.append("Saturn")
    out_body_type.append("Planet")
    out_colour.append("Gold")
if uranus:
    outer_bodies.append("Uranus")
    out_body_type.append("Planet")
    out_colour.append("Green")
if neptune:
    outer_bodies.append("Neptune")
    out_body_type.append("Planet")
    out_colour.append("Blue")

if ceres:
    inner_bodies.append("Ceres")
    in_body_type.append("Dwarf")
    in_colour.append("Black")    

if orcus:
    outer_bodies.append("Orcus")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if pluto:
    outer_bodies.append("Pluto")
    out_body_type.append("Dwarf")
    out_colour.append("Black")
if haumea:
    outer_bodies.append("Haumea")
    out_body_type.append("Dwarf")
    out_colour.append("Black")
if quaoar:
    outer_bodies.append("Quaoar")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if makemake:
    outer_bodies.append("Makemake")
    out_body_type.append("Dwarf")
    out_colour.append("Black")
if gonggong:
    outer_bodies.append("Gonggong")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
if eris:
    outer_bodies.append("Eris")
    out_body_type.append("Dwarf")
    out_colour.append("Black")
if sedna:
    outer_bodies.append("Sedna")
    out_body_type.append("Dwarf")
    out_colour.append("Gray")
    
#create orbit plots
op1 = rebound.OrbitPlot(sim, unitlabel="[AU]", particles = inner_bodies) 
op2 = rebound.OrbitPlot(sim, unitlabel="[AU]", particles = outer_bodies)

#integrate/stepping
def step1():
    sim.steps(5)
    st.session_state.count += 5
    op1.update()
    op2.update()

def step2():
    sim.steps(100)
    st.session_state.count += 100
    op1.update()
    op2.update()

def step3():
    sim.steps(500)
    st.session_state.count += 500
    op1.update()
    op2.update()
    

#stepping buttons
st.header('Time Step')
col_1, col_2, col_3 = st.columns(3)

with col_1:
    step_btn_1 = st.button('+5 Days')

with col_2:	
    step_btn_2 = st.button('+100 Days')

with col_3:	
    step_btn_3 = st.button('+500 Days')	

if step_btn_1:
    step1()

if step_btn_2:
	step2()

if step_btn_3:
	step3()

st.write(f'Time Elapsed: {st.session_state.count} Days')
current_date = date + pd.Timedelta(days=st.session_state.count)
#current_date = current_date.to_datetime()
st.write(f'Current Date: {current_date}')

#plotting
op1.particles.set_color(in_colour)
for i in range(len(in_body_type)):
    if in_body_type[i] == "Dwarf":
        op1.orbits[i].set_linestyle("--")

op2.particles.set_color(out_colour)
for i in range(len(out_body_type)):
    if out_body_type[i] == "Dwarf":
      op2.orbits[i].set_linestyle("--")
	
#Display plots
col_in, col_out = st.columns(2)

with col_in:
    st.header("Inner Solar System")
    st.pyplot(op1.fig)

with col_out:
    st.header("Outer Solar System")
    st.pyplot(op2.fig)

#Experimental animate
animate = st.radio('Animate: !Experimental!', ('Off', 'Slow', 'Fast'))

if animate == 'Slow':
    step1()
elif animate == 'Fast':
    step2()

if animate != 'Off':
    st.experimental_rerun()