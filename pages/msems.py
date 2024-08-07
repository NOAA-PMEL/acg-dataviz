
import dash
from dash import html, dcc, callback, Output, Input, get_relative_path
import dash_design_kit as ddk
import plotly.graph_objects as go
import requests
import xarray as xr
import io
import numpy as np




# Register the page with Dash
dash.register_page(__name__, path="/msems")

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




# Load the data for msems
data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_msems_30s.nc"
msems_table = load_data(data_url).set_index({"row": ["time", "msems_diameter"]}).unstack("row")




# Extract necessary variables
msems_table["trajectory_id"] = msems_table.trajectory_id.isel(msems_diameter=0).drop_vars("msems_diameter")
msems_table["latitude"] = msems_table.latitude.isel(msems_diameter=0).drop_vars("msems_diameter")
msems_table["longitude"] = msems_table.longitude.isel(msems_diameter=0).drop_vars("msems_diameter")
msems_table["altitude"] = msems_table.altitude.isel(msems_diameter=0).drop_vars("msems_diameter")




# Get unique flight IDs
unique_flights = np.unique(msems_table['trajectory_id'])



def layout(project="unknown", **kwargs): 

    # Define the layout using Dash Design Kit
    layout = ddk.Block([
        ddk.Card("MSEMS"),
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False), # style={'background-color': '#add8e6'}
            ddk.Block([
                ddk.Card(dcc.Dropdown(
                    id='flight-dropdown',
                    options=[{'label': flight, 'value': flight} for flight in unique_flights],
                    placeholder='Select a flight',
                    clearable=False
                ), style={'width':'25%', 'margin-bottom': 2}),
                # ddk.Card([
                #     html.Label("Select Variable to Display"),
                #     dcc.Checklist(
                #         id='variable-checklist',
                #         options=[
                #             {'label': 'msems_dNdlogDp', 'value': 'msems_dNdlogDp'},
                #             {'label': 'msems_dSdlogDp', 'value': 'msems_dSdlogDp'},
                #             {'label': 'msems_dVdlogDp', 'value': 'msems_dVdlogDp'}
                #         ],
                #         value=['msems_dNdlogDp'],  # Default selection
                #         inline=True
                #     ),
                # ], style={'width':'18%'}),
                # ddk.Card([
                #     html.Label("Select Color Scale Range"),
                #     dcc.Input(id='color-scale-min', type='number', placeholder='Min', value=0),
                #     dcc.Input(id='color-scale-max', type='number', placeholder='Max', value=300),
                # ], style={'width':'40%'}),
            ddk.Row([
                ddk.Card(dcc.Loading(dcc.Graph(id='msems-graph'))),  # Use dcc.Graph to display the figure
                ddk.Block([
                    ddk.Card([
                        html.Label("Select Variable to Display"),
                        dcc.Checklist(
                            id='variable-checklist',
                            options=[
                                {'label': 'msems_dNdlogDp', 'value': 'msems_dNdlogDp'},
                                {'label': 'msems_dSdlogDp', 'value': 'msems_dSdlogDp'},
                                {'label': 'msems_dVdlogDp', 'value': 'msems_dVdlogDp'}
                            ],
                            value=['msems_dNdlogDp'],  # Default selection
                            inline=True
                        ),
                    ]),
                    ddk.Card([
                        html.Label("Select Color Scale Range"),
                        dcc.Input(id='color-scale-min', type='number', placeholder='Min', value=0),
                        dcc.Input(id='color-scale-max', type='number', placeholder='Max', value=300),
                    ]),
                ], style={'width':'20%'})
            ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'}),  # Adjust margins here
            ]),
        ]),
        # ddk.Row([
        #     ddk.Card(dcc.Loading(dcc.Graph(id='msems-graph'))),  # Use dcc.Graph to display the figure
        # ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'}),  # Adjust margins here
    ])
    return layout

# Define the callback to update the graph based on flight selection and color scale range
@callback(
    Output('msems-graph', 'figure'),
    Input('flight-dropdown', 'value'),
    Input('variable-checklist', 'value'),
    Input('color-scale-min', 'value'),
    Input('color-scale-max', 'value')
)
def update_graph(selected_flight, selected_variable, min_value, max_value):
    if selected_flight is None:
        return go.Figure()  # Return an empty figure if no flight is selected

    # Filter data for the selected flight
    flight_data = msems_table.where(msems_table.trajectory_id == selected_flight).dropna(dim="time")

    # Extract the last two digits of the selected flight
    flight_suffix = str(selected_flight)[-2:]

    # Create the heatmap using go.Heatmap
    fig = go.Figure()

    for var in selected_variable:
        if var in flight_data:
            fig.add_trace(go.Heatmap(
                z=flight_data[var].transpose(),
                colorscale='Viridis',
                zmin=min_value,
                zmax=max_value,
                name=var
            ))

    fig.update_layout(
        title=f"Flight {flight_suffix}: MSEMS Time Series: Concentration of Diameters of Particles over Time",
        xaxis_title="Time",
        yaxis_title="Diameter",
        margin=dict(l=50, r=50, t=80, b=50)
    )
    fig.update_yaxes(type="log")

    return fig