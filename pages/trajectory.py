# from dash import html, register_page  #, callback # If you need callbacks, import it here.

# register_page(
#     __name__,
#     name='1D Data Trajectory',
#     top_nav=True,
#     path='/trajectory'
# )

# def layout():
#     return html.Div([
#         html.H1("1D Data Trajectory Here.")
#     ])
    


import dash
from dash import html, dcc, callback, Output, Input
import dash_design_kit as ddk
import requests
import xarray as xr
import io
import numpy as np
import plotly.graph_objects as go




# Register the page with Dash
dash.register_page(__name__, path="/trajectory")




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




# Load the data for CDP (assuming similar structure as previous page)
data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
df = load_data(data_url)




# Get unique flight IDs
unique_flights = np.unique(df['trajectory_id'].values)




# Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']




# Define the layout using Dash Design Kit
layout = ddk.App([
    ddk.Card("Page 5: Trajectory CDP"),
    ddk.Card(dcc.Dropdown(
        id='flight-dropdown',
        options=[{'label': flight, 'value': flight} for flight in unique_flights],
        placeholder='Select a flight',
        clearable=False
    )),
    ddk.Card([
        dcc.Dropdown(
            id='color-dropdown',
            options=[{'label': col, 'value': col} for col in columns],
            placeholder='Select a variable for color',
            clearable=False,
            style={'width': '200px', 'margin-bottom': '10px'}
        ),
        dcc.Loading(dcc.Graph(id='trajectory-graph', style={'height': '600px'}))  # Use dcc.Loading and dcc.Graph
    ]),
    ddk.Card([
        ddk.Block(width=50, children=[
            dcc.Loading(dcc.Graph(id='longitude-altitude-plot'))  # Use dcc.Loading and dcc.Graph
        ]),
        ddk.Block(width=50, children=[
            dcc.Loading(dcc.Graph(id='latitude-altitude-plot'))  # Use dcc.Loading and dcc.Graph
        ])
    ])
])




# Define callback to update trajectory information based on flight and color variable selection
@callback(
    Output('trajectory-graph', 'figure'),
    Output('longitude-altitude-plot', 'figure'),
    Output('latitude-altitude-plot', 'figure'),
    Input('flight-dropdown', 'value'),
    Input('color-dropdown', 'value')
)
def update_trajectory_info(selected_flight, color_var):
    if selected_flight is None or color_var is None:
        return go.Figure(), go.Figure(), go.Figure()


    # Filter data for the selected flight
    selected_data = df.where(df.trajectory_id == selected_flight, drop=True)


    # Extract latitude, longitude, and altitude columns
    x = selected_data['longitude'].values
    y = selected_data['latitude'].values
    z = selected_data['altitude'].values
    color = selected_data[color_var].values


    # Create 3D scatter plot
    fig_3d = go.Figure(data=[go.Scatter3d(
        x=x,
        y=y,
        z=z,
        mode='markers',
        marker=dict(
            size=4,
            color=color,  # set color to selected variable values
            colorscale='Viridis',  # choose a colorscale
            opacity=0.8,
            colorbar=dict(
                title=color_var
            )
        )
    )])


    # Update 3D scatter plot layout
    fig_3d.update_layout(
        title=f'3D Scatter Plot of Latitude, Longitude, and Altitude for Flight {selected_flight}',
        scene=dict(
            xaxis_title='Longitude',
            yaxis_title='Latitude',
            zaxis_title='Altitude'
        ),
        margin=dict(l=50, r=50, t=80, b=50)
    )


    # Create 2D scatter plot: Longitude vs Altitude
    fig_long_alt = go.Figure(data=[go.Scatter(
        x=x,
        y=z,
        mode='markers',
        marker=dict(
            size=4,
            color=color,  # set color to selected variable values
            colorscale='Viridis',  # choose a colorscale
            opacity=0.8
        )
    )])


    # Update 2D scatter plot layout for Longitude vs Altitude
    fig_long_alt.update_layout(
        title=f'2D Scatter Plot of Longitude and Altitude for Flight {selected_flight}',
        xaxis_title='Longitude',
        yaxis_title='Altitude',
        margin=dict(l=50, r=50, t=80, b=50)
    )


    # Create 2D scatter plot: Latitude vs Altitude
    fig_lat_alt = go.Figure(data=[go.Scatter(
        x=y,
        y=z,
        mode='markers',
        marker=dict(
            size=4,
            color=color,  # set color to selected variable values
            colorscale='Viridis',  # choose a colorscale
            opacity=0.8
        )
    )])


    # Update 2D scatter plot layout for Latitude vs Altitude
    fig_lat_alt.update_layout(
        title=f'2D Scatter Plot of Latitude and Altitude for Flight {selected_flight}',
        xaxis_title='Latitude',
        yaxis_title='Altitude',
        margin=dict(l=50, r=50, t=80, b=50)
    )


    return fig_3d, fig_long_alt, fig_lat_alt
