import dash
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import dash_design_kit as ddk
import plotly.graph_objects as go
import requests
import xarray as xr
import io
import numpy as np
import re

# Register the page with Dash
dash.register_page(__name__, path="/pops")

# Function to load data from URL and convert to xarray Dataset
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        dataset = xr.open_dataset(io.BytesIO(response.content))
        return dataset
    except Exception as e:
        print(f"Error loading data from {url}: {e}")
        return None

# Load the data for POPS
data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_clearsky_pops_30s.nc"
pops_table = load_data(data_url).set_index({"row": ["time", "pops_diameter"]}).unstack("row")

pops_table["trajectory_id"] = pops_table.trajectory_id.isel(pops_diameter=3).drop_vars("pops_diameter")
pops_table["latitude"] = pops_table.latitude.isel(pops_diameter=0).drop_vars("pops_diameter")
pops_table["longitude"] = pops_table.longitude.isel(pops_diameter=0).drop_vars("pops_diameter")
pops_table["altitude"] = pops_table.altitude.isel(pops_diameter=0).drop_vars("pops_diameter")

# Convert trajectory_id to string, filter out NaNs, and filter by pattern
trajectory_ids = pops_table["trajectory_id"].values.astype(str)

# Use a regular expression to match valid trajectory IDs
pattern = re.compile(r"Tillamook2022_FVR-55_Flight_\d+")

filtered_trajectory_ids = []
for tid in trajectory_ids:
    if pattern.match(tid):
        filtered_trajectory_ids.append(tid)

# Get unique, valid trajectory IDs
unique_flights = np.unique(filtered_trajectory_ids)


def layout(project="unknown", **kwargs): 

    # Define the layout using Dash Design Kit
    layout = ddk.Block([
        ddk.Card("Page 4: POPS"),
        ddk.Card(dcc.Dropdown(
            id='flight-dropdown',
            options=[{'label': flight, 'value': flight} for flight in unique_flights],
            placeholder='Select a flight',
            clearable=False
        )),
        ddk.Card([
            html.Label("Select Color Scale Range for dN/dlogDp"),
            dcc.Input(id='color-scale-min', type='number', placeholder='Min', value=0),
            dcc.Input(id='color-scale-max', type='number', placeholder='Max', value=300),
        ]),
        ddk.Card(dcc.Loading(dcc.Graph(id='pops-graph')))  # Use dcc.Loading and dcc.Graph to display the figure
    ])
    return layout

# Define the callback to update the graph based on flight selection and color scale range
@callback(
    Output('pops-graph', 'figure'),
    Input('flight-dropdown', 'value'),
    Input('color-scale-min', 'value'),
    Input('color-scale-max', 'value')
)
def update_graph(selected_flight, min_value, max_value):
    if selected_flight is None:
        return go.Figure()  # Return an empty figure if no flight is selected

    # Filter data for the selected flight
    flight_data = pops_table.where(pops_table.trajectory_id == selected_flight).dropna(dim="time")

    # Create the heatmap using px.imshow
    pops_fig = px.imshow(
        flight_data.pops_dNdlogDp.transpose(),
        color_continuous_scale='viridis',
        zmin=min_value,
        zmax=max_value,
        origin='lower',
        title=f"Flight {selected_flight}: Cloud Droplet dN/dlogDp",
        labels={"x": "time", "y": "pops_diameter"}
    )
    pops_fig.update_layout(coloraxis=dict(cauto=False)).update_yaxes(type="log")

    return pops_fig