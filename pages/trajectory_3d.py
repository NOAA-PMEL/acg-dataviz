# from dash import html, register_page 

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
from dash import html, dcc, callback, Output, Input, no_update
import dash_design_kit as ddk
import requests
import xarray as xr
import io
import numpy as np
import plotly.graph_objects as go




# Register the page with Dash
dash.register_page(__name__, path_template="/<project>/trajectory_3d")
# dash.register_page(__name__, path_template="/trajectory")

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
# global df
df = load_data(data_url)
# # print(df)



# Get unique flight IDs
if df is not None:
    unique_flights = np.unique(df['trajectory_id'].values)
else:
    unique_flights = []
# print(unique_flights)



# Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
if df is not None:
    columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
else:
    columns = []

# print(columns)


# Define the layout using Dash Design Kit
# layout = ddk.Block([
def layout(project="unknown", **kwargs): 
    layout = ddk.Block([
        ddk.Card(f"3D Trajectory of 1D Data ({project})"),
        ddk.Card(dcc.Dropdown(
            id='flight-dropdown-2',
            options=[{'label': flight, 'value': flight} for flight in unique_flights],
            placeholder='Select a flight',
            clearable=False
        )),
        ddk.Card([
            dcc.Dropdown(
                id='color-dropdown-2',
                options=[{'label': col, 'value': col} for col in columns],
                placeholder='Select a variable for color',
                clearable=False,
                style={'width': '200px', 'margin-bottom': '10px'}
            ),
            dcc.Loading(dcc.Graph(id='trajectory-graph-2', style={'height': '600px'}))  # Use dcc.Loading and dcc.Graph
            # dcc.Graph(id='trajectory-graph-2', style={'height': '600px'})  # Use dcc.Loading and dcc.Graph
        ]),
        ddk.Card([
            ddk.Block(width=50, children=[
                dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2'))  # Use dcc.Loading and dcc.Graph
            ]),
            ddk.Block(width=50, children=[
                dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2'))  # Use dcc.Loading and dcc.Graph
            ])
        ])
    ])
    return layout
    
# print(layout)

# Define callback to update trajectory information based on flight and color variable selection
@callback(
    Output('trajectory-graph-2', 'figure'),
    Output('longitude-altitude-plot-2', 'figure'),
    Output('latitude-altitude-plot-2', 'figure'),
    Input('flight-dropdown-2', 'value'),
    Input('color-dropdown-2', 'value')
)
def update_trajectory_info_2(selected_flight, color_var):
    # global df 

    print(f"here:1 {selected_flight}, {color_var}")
    if selected_flight is None or color_var is None:
        return go.Figure(), go.Figure(), go.Figure()
    
    print(f"pre-error {selected_flight}, {color_var}")
    
    # Filter data for the selected flight
    if df is None:
        return dash.no_update, dash.no_update, dash.no_update
    selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

    print(f"post-error {selected_data}")


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
    print("here:2")

    return fig_3d, fig_long_alt, fig_lat_alt


print("bottom")