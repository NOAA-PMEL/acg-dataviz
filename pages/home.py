import dash
from dash import Dash, html, dcc, callback, Output, Input
# import numpy
import pandas as pd
import plotly.express as px
import dash_design_kit as ddk

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
dash.register_page(__name__, path="/home")
# app = Dash(__name__, use_pages=True)
# server = app.server  # expose server variable for Procfile

# app.layout = [
layout = ddk.App(show_editor=True, children=[
    # html.H1(children='ACG DataViz!', style={'textAlign':'center'}),
    ddk.Header(ddk.Title('ACG DataViz!')),
    ddk.ControlCard([
    ddk.ControlItem(dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection')),
    ddk.Graph(id='graph-content')
    ])
])
