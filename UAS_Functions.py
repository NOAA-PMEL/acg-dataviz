import dash
from dash import html, dcc, callback, Output, Input, State, get_relative_path
import plotly.graph_objects as go
import dash_design_kit as ddk
import dash_bootstrap_components as dbc
import requests
import xarray as xr
import io
import pandas as pd
import plotly.express as px


def say_hello():
    return "hello"



def generate_scatter_plot(df, x_column, y_column, graph_id):
    figure = px.scatter(df, x=x_column, y=y_column, title=f'{x_column} vs {y_column}')
    return dcc.Loading(dcc.Graph(figure=figure, id=graph_id))