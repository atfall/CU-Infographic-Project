import rebound
import streamlit as st
import datetime
import pandas as pd
import mpld3
import streamlit.components.v1 as components
import plotly.express as pe
#%matplotlib notebook

sim = rebound.Simulation()

mercury = st.checkbox('Mercury')
venus = st.checkbox('Venus')
earth = st.checkbox('Earth', value = True)
mars = st.checkbox('Mars')
jupiter = st.checkbox('Jupiter')
saturn = st.checkbox('Saturn')
uranus = st.checkbox('Uranus')
neptune = st.checkbox('Neptune')

d = st.date_input(
    "Pick a date",
    value = pd.to_datetime('today'))
d = str(d)
sim.add("Sun")

if mercury:
    sim.add("Mercury", date = d)
if venus:
    sim.add("Venus", date = d)
if earth:
    sim.add("Earth", date = d)
if mars:
    sim.add("Mars", date = d)
if jupiter:
    sim.add("Jupiter", date = d)
if saturn:
    sim.add("Saturn", date = d)
if uranus:
    sim.add("Uranus", date = d)
if neptune:
    sim.add("Neptune", date = d)
 
op = rebound.OrbitPlot(sim)

css = """
table
{
  border-collapse: collapse;
}
th
{
  color: #ffffff;
  background-color: #000000;
}
td
{
  background-color: #cccccc;
}
table, th, td
{
  font-family:Arial, Helvetica, sans-serif;
  border: 1px solid black;
  text-align: right;
}
"""
for axes in two_subplot_fig.axes:
    for line in axes.get_lines():
        # get the x and y coords
        xy_data = line.get_xydata()
        labels = []
        for x, y in xy_data:
            # Create a label for each point with the x and y coords
            html_label = f'<table border="1" class="dataframe"> <thead> <tr style="text-align: right;"> </thead> <tbody> <tr> <th>x</th> <td>{x}</td> </tr> <tr> <th>y</th> <td>{y}</td> </tr> </tbody> </table>'
            labels.append(html_label)
        # Create the tooltip with the labels (x and y coords) and attach it to each line with the css specified
        tooltip = plugins.PointHTMLTooltip(line, labels, css=css)
        # Since this is a separate plugin, you have to connect it
        plugins.connect(op.fig, tooltip)

fig_html = mpld3.fig_to_html(op.fig)
components.html(fig_html, height=600)

