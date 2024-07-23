import dash
from dash import html, dcc, callback, Output, Input, get_relative_path
import dash_design_kit as ddk
import plotly.graph_objects as go
import requests
import xarray as xr
import io
import numpy as np




# Register the page with Dash
dash.register_page(__name__, path="/cdp")
# dash.register_page(__name__, path_template="/<project>/cdp") # ask

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
            dcc.Link('POPS - not done', href=get_relative_path('/pops'))
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




# Load the data for CDP
data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_cdp_1s.nc"
cdp_table = load_data(data_url).set_index({"row": ["time", "cdp_diameter"]}).unstack("row")




# Extract necessary variables
cdp_table["trajectory_id"] = cdp_table.trajectory_id.isel(cdp_diameter=0).drop_vars("cdp_diameter")
cdp_table["latitude"] = cdp_table.latitude.isel(cdp_diameter=0).drop_vars("cdp_diameter")
cdp_table["longitude"] = cdp_table.longitude.isel(cdp_diameter=0).drop_vars("cdp_diameter")
cdp_table["altitude"] = cdp_table.altitude.isel(cdp_diameter=0).drop_vars("cdp_diameter")




# Get unique flight IDs
unique_flights = np.unique(cdp_table['trajectory_id'])



def layout(project="unknown", **kwargs): 

# Define the layout using Dash Design Kit
    layout = ddk.Block([
        ddk.Card("Page 2: CDP"),
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
                ), width=50),
                ddk.Card([
                    html.Label("Select Variables to Display"),
                    dcc.Checklist(
                        id='variable-checklist',
                        options=[
                            {'label': 'cdp_dNdlogDp', 'value': 'cdp_dNdlogDp'},
                            {'label': 'cdp_dSdlogDp', 'value': 'cdp_dSdlogDp'},
                            {'label': 'cdp_dVdlogDp', 'value': 'cdp_dVdlogDp'}
                        ],
                        value=['cdp_dNdlogDp'],  # Default selection
                        inline=True
                    ),
                    html.Label("Select Color Scale Range"),
                    dcc.Input(id='color-scale-min', type='number', placeholder='Min', value=0),
                    dcc.Input(id='color-scale-max', type='number', placeholder='Max', value=300),
                ], width=50),
                ddk.Row([
            ddk.Card(dcc.Loading(dcc.Graph(id='cdp-graph'))),  # Use dcc.Loading and dcc.Graph to display the figure
        ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'}),  # Adjust margins here
        ddk.Row([
            ddk.Card(dcc.Loading(dcc.Graph(id='average-plot')))  # Use dcc.Loading and dcc.Graph for the average plot
        ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'})  # Adjust margins here
            ]),
        ]),
        # ddk.Row([
        #     ddk.Card(dcc.Loading(dcc.Graph(id='cdp-graph'))),  # Use dcc.Loading and dcc.Graph to display the figure
        # ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'}),  # Adjust margins here
        # ddk.Row([
        #     ddk.Card(dcc.Loading(dcc.Graph(id='average-plot')))  # Use dcc.Loading and dcc.Graph for the average plot
        # ], style={'marginTop': '20px', 'marginBottom': '20px', 'marginLeft': '10px', 'marginRight': '10px'})  # Adjust margins here
    ])
    return layout



# Define the callback to update the graphs based on flight selection, variables, and color scale range
@callback(
    Output('cdp-graph', 'figure'),
    Output('average-plot', 'figure'),
    Input('flight-dropdown', 'value'),
    Input('variable-checklist', 'value'),
    Input('color-scale-min', 'value'),
    Input('color-scale-max', 'value')
)
def update_graph(selected_flight, selected_variables, min_value, max_value):
    if selected_flight is None:
        return go.Figure(), go.Figure()  # Return empty figures if no flight is selected

    # Filter data for the selected flight
    flight_data = cdp_table.where(cdp_table.trajectory_id == selected_flight).dropna(dim="time")

    # Create the 2D heatmap using go.Heatmap
    fig = go.Figure()
    for var in selected_variables:
        if var in flight_data:
            fig.add_trace(go.Heatmap(
                z=flight_data[var].transpose(),
                colorscale='Viridis',
                zmin=min_value,
                zmax=max_value,
                name=var
            ))

    fig.update_layout(
        title=f"Flight {selected_flight}: CDP Variables",
        xaxis_title="Time",
        yaxis_title="Diameter",
        margin=dict(l=50, r=50, t=80, b=50)  # Adjust margins as needed
    )
    fig.update_yaxes(type="log")

    # Calculate average of cdp_dNdlogDp across all times
    if 'cdp_dNdlogDp' in selected_variables:
        average_values = flight_data['cdp_dNdlogDp'].mean(dim='time')
        average_fig = go.Figure()
        average_fig.add_trace(go.Scatter(
            x=np.log10(average_values['cdp_diameter']),  # Convert diameter to logarithmic scale
            y=average_values,
            mode='lines+markers',
            marker=dict(size=8),
            line=dict(color='blue', width=2),
            name='Average cdp_dNdlogDp'
        ))
        average_fig.update_layout(
            title=f"Flight {selected_flight}: Average cdp_dNdlogDp",
            xaxis_title="Log Diameter",  # Update x-axis title
            yaxis_title="Average cdp_dNdlogDp",
            margin=dict(l=50, r=50, t=80, b=50)  # Adjust margins as needed
        )
        average_fig.update_xaxes(type="log")  # Set logarithmic scale for x-axis
        average_fig.update_yaxes(type="log")
    else:
        average_fig = go.Figure()

    return fig, average_fig