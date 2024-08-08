
import dash
from dash import Dash, html, dcc, callback, Output, Input, dash_table, State, get_relative_path
import pandas as pd
import plotly.graph_objects as go
import dash_design_kit as ddk
import requests
import xarray as xr
import io




# Function to load data from URL and convert to DataFrame
def load_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        dataset = xr.open_dataset(io.BytesIO(response.content)).set_coords("time").swap_dims({"row": "time"})
        df = dataset.to_dataframe().reset_index()
        return df
    except Exception as e:
        print(f"Error loading data from {url}: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error




# Load initial data to get unique flight IDs
data_url = 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'
df_initial = load_data(data_url)
unique_flights = df_initial['trajectory_id'].unique()




# Get available columns for dropdown options (excluding 'trajectory_id')
available_columns = [col for col in df_initial.columns if col != 'trajectory_id']




# Register the page with Dash
dash.register_page(__name__, path="/propPropPlot")


menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='1D Data Visualization',
        default_open=False,
        children=[
            dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
            dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
            # dcc.Link('test page', href=get_relative_path('/test')),
        ]
    ),
    ddk.CollapsibleMenu(
        title='2D Data Visualization',
        default_open=False,
        children=[
            dcc.Link('CDP', href=get_relative_path('/cdp')),
            dcc.Link('MSEMS', href=get_relative_path('/msems')),
            dcc.Link('POPS', href=get_relative_path('/pops'))
        ]
    ),
    ddk.CollapsibleMenu(
        title='3D Data Visualization',
        default_open=False,
        children=[
            dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/trajectory_3d')),
            # dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/option2'))
        ]
    ),
])


def layout(project="unknown", **kwargs):
    # Define the layout using Dash Design Kit
    layout = ddk.Block([
        ddk.Card("Property Property Plots"),
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False), # style={'background-color': '#add8e6'}
            ddk.Block([
                ddk.Card([
                    ddk.Row([
                        dcc.Dropdown(
                            options=[
                                {'label': '1 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'},
                                {'label': '30 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_30s.nc'}
                            ],
                            value='https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc',
                            id='data-dropdown',
                            clearable=False,
                            style={'width': '200px', 'margin-bottom': '10px'}
                        ),
                        dcc.Dropdown(
                            id='flight-dropdown',
                            options=[{'label': flight, 'value': flight} for flight in unique_flights],
                            placeholder='Select a flight',
                            clearable=False,
                            style={'width': '400px', 'margin-bottom': '10px'}
                        ),
                    ])
                ]),
                ddk.Card([
                    ddk.Row([
                        dcc.Dropdown(
                            id='x-axis-dropdown',
                            options=[{'label': col, 'value': col} for col in available_columns],
                            # placeholder='Select X-axis variable',
                            value='time',
                            style={'width': '300px', 'margin-bottom': '10px'}
                        ),
                        dcc.Dropdown(
                            id='y-axis-dropdown',
                            options=[{'label': col, 'value': col} for col in available_columns],
                            # placeholder='Select Y-axis variable',
                            value='altitude',
                            style={'width': '300px', 'margin-bottom': '10px'}
                        ),
                        dcc.Dropdown(
                            id='color-dropdown',
                            options=[{'label': col, 'value': col} for col in available_columns],
                            # placeholder='Select a variable for color',
                            value='fast_ambient_T',
                            clearable=False,
                            style={'width': '300px', 'margin-bottom': '10px'}
                        )
                    ]),
                    dcc.Loading(ddk.Graph(id='prop-prop-plot'))  # Use dcc.Loading and dcc.Graph to display the figure
                ])
            ])
        ]),
    ])
    return layout








# Define callback to update the scatter plot based on selected data, flight, x-axis, y-axis variables, and color variable
@callback(
    Output('prop-prop-plot', 'figure'),
    Input('data-dropdown', 'value'),
    Input('flight-dropdown', 'value'),
    Input('x-axis-dropdown', 'value'),
    Input('y-axis-dropdown', 'value'),
    Input('color-dropdown', 'value')
)
def update_prop_prop_plot(data_url, selected_flight, x_axis, y_axis, color_var):
    df = load_data(data_url)


    if df.empty or not x_axis or not y_axis or not color_var:
        return go.Figure()


    filtered_data = df[df['trajectory_id'] == selected_flight]


    # Extract the last two digits of the selected flight
    flight_suffix = str(selected_flight)[-2:]

    # Create scatter plot
    fig = go.Figure(data=go.Scatter(
        x=filtered_data[x_axis],
        y=filtered_data[y_axis],
        mode='markers',
        marker=dict(
            color=filtered_data[color_var],  # Color by selected variable
            colorscale='viridis',  # Set color scale to viridis
            colorbar=dict(title=color_var)  # Set color bar title
        )
    ))


    fig.update_layout(
        title=f"Flight {flight_suffix}: {y_axis} vs {x_axis}",
        xaxis_title=x_axis,
        yaxis_title=y_axis,
        showlegend=False,
        margin=dict(l=50, r=50, t=80, b=50)  # Adjust top margin (t) as needed
    )


    return fig
