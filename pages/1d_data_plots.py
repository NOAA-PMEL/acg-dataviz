# import dash
# from dash import html, dcc, callback, Output, Input, State, get_relative_path
# import plotly.graph_objects as go
# import dash_design_kit as ddk
# import dash_bootstrap_components as dbc
# import requests
# import xarray as xr
# import io
# import pandas as pd

# # Function to load data from URL and convert to DataFrame
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content)).set_coords("time").swap_dims({"row": "time"})
#         df = dataset.to_dataframe().reset_index()
#         return df
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return pd.DataFrame()  # Return an empty DataFrame in case of error

# # Load initial data to get unique flight IDs
# data_url = 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'
# df_initial = load_data(data_url)
# unique_flights = df_initial['trajectory_id'].unique()
# available_columns = df_initial.columns.tolist()

# # Register the page with Dash
# dash.register_page(__name__, path="/1d_data_plots")


# menu = ddk.Menu([
#     ddk.CollapsibleMenu(
#         title='1D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
#             dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
#             # dcc.Link('test page', href=get_relative_path('/test')),
#         ]
#     ),
#     ddk.CollapsibleMenu(
#         title='2D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('CDP', href=get_relative_path('/cdp')),
#             dcc.Link('MSEMS', href=get_relative_path('/msems')),
#             dcc.Link('POPS - not done', href=get_relative_path('/pops'))
#         ]
#     ),
#     ddk.CollapsibleMenu(
#         title='3D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/trajectory_3d')),
#             # dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/option2'))
#         ]
#     ),
# ])


# # Add layout function to match Trajectory page
# def layout(project="unknown", **kwargs): 


# # Define the layout using Dash Design Kit
#     layout = ddk.App([
#         ddk.Card("Welcome to DataViz! --This is a test program, NOT REAL--"),
#         ddk.Sidebar([
#                 menu
#             ], foldable=False), # style={'background-color': '#add8e6'}
#         dcc.Dropdown(
#             options=[
#                 {'label': '1 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'},
#                 {'label': '30 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_30s.nc'}
#             ],
#             value='https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc',
#             id='data-dropdown',
#             clearable=False
#         ),
#         dcc.Dropdown(
#             id='flight-dropdown',
#             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#             placeholder='Select a flight',
#             clearable=False
#         ),
#         ddk.Row([
#             ddk.Card([
#                 dcc.Dropdown(
#                     id='dropdown-plot1',
#                     options=[
#                         {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                         {'label': 'altitude', 'value': 'altitude'},
#                         {'label': 'true_air_speed', 'value': 'true_air_speed'}
#                     ],
#                     value='altitude',
#                     clearable=False
#                 ),
#                 dcc.Loading(dcc.Graph(figure={}, id='graph-plot1'))
#             ], width=50),
#             ddk.Card([
#                 dcc.Dropdown(
#                     id='dropdown-plot2',
#                     options=[
#                         {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                         {'label': 'altitude', 'value': 'altitude'},
#                         {'label': 'true_air_speed', 'value': 'true_air_speed'},
#                         {'label': 'ground_speed', 'value': 'ground_speed'},
#                         {'label': 'pressure_altitude', 'value': 'pressure_altitude'},
#                         {'label': 'height_agl', 'value': 'height_agl'}
#                     ],
#                     value='true_air_speed',
#                     clearable=False
#                 ),
#                 dcc.Loading(dcc.Graph(figure={}, id='graph-plot2'))
#             ], width=50),
#         ]),
#         ddk.Row([
#             ddk.Card([
#                 dcc.Loading(ddk.DataTable(data=[], page_size=12, style_table={'overflowX': 'auto'}, id='data-table'))
#             ], width=100)
#         ]),
#         html.Button('Full Download', id='btn-full-download', n_clicks=0),
#         dbc.Modal(
#             [
#                 dbc.ModalHeader(dbc.ModalTitle("Header"), close_button=True),
#                 dbc.ModalBody([
#                     "This modal is vertically centered. Click outside this modal to close.",
#                     dcc.Checklist(
#                         id='variable-checklist',
#                         options=[{'label': col, 'value': col} for col in available_columns],
#                         value=[],
#                         inline=True,
#                         style={'margin-top': '20px'}
#                     ),
#                     html.Button("Download Selected Variables", id="btn-download-selected", n_clicks=0),
#                     html.Button("Download Current Dataset: CSV", id="btn-download-csv"),
#                     html.Button("Download Current Dataset: NetCDF", id="btn-download-netcdf")
#                 ]),
#                 dbc.ModalFooter(
#                     dbc.Button(
#                         "Close",
#                         id="close-centered",
#                         className="ms-auto",
#                         n_clicks=0,
#                     ),
#                 ),
#                 html.A('Download Link: Full NetCDF', id='download-link', target='_blank', style={'display': 'block', 'margin-top': '20px'})
#             ],
#             id="modal-centered",
#             centered=True,
#             is_open=False,
#         ),
#         dcc.Download(id='download-selected'),
#         dcc.Download(id='download-dataframe-csv'),
#         dcc.Download(id='download-dataframe-netcdf')
#     ])
#     return layout

# # Callback to update the table based on dropdown selection
# @callback(
#     Output('data-table', 'data'),
#     Input('flight-dropdown', 'value'),
#     State('data-dropdown', 'value')
# )
# def update_table(flight_chosen, data_url):
#     df = load_data(data_url)
#     # Filter data by the selected flight
#     if flight_chosen:
#         df = df[df['trajectory_id'] == flight_chosen]
#     return df.to_dict('records')

# # Callback to update the scatter plots
# @callback(
#     Output('graph-plot1', 'figure'),
#     Output('graph-plot2', 'figure'),
#     Input('flight-dropdown', 'value'),
#     Input('dropdown-plot1', 'value'),
#     Input('dropdown-plot2', 'value'),
#     State('data-dropdown', 'value')
# )
# def update_graph(flight_chosen, col_chosen1, col_chosen2, data_url):
#     df = load_data(data_url)
#     # Filter data by the selected flight
#     if flight_chosen:
#         df = df[df['trajectory_id'] == flight_chosen]
#     fig1 = go.Figure()
#     fig2 = go.Figure()
#     if not df.empty:
#         if col_chosen1 in df.columns:
#             fig1.add_trace(go.Scatter(x=df['time'], y=df[col_chosen1], mode='markers', marker=dict(color=df[col_chosen1], colorscale='viridis', colorbar=dict(title=col_chosen1))))
#             fig1.update_layout(title=col_chosen1)
#         if col_chosen2 in df.columns:
#             fig2.add_trace(go.Scatter(x=df['time'], y=df[col_chosen2], mode='markers', marker=dict(color=df[col_chosen2], colorscale='plasma', colorbar=dict(title=col_chosen2))))
#             fig2.update_layout(title=col_chosen2)
#     return fig1, fig2

# # Callback for CSV download
# @callback(
#     Output(component_id='download-dataframe-csv', component_property='data'),
#     Input(component_id='btn-download-csv', component_property='n_clicks'),
#     State('data-dropdown', 'value')
# )
# def download_csv(n_clicks, data_url):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     return dcc.send_data_frame(df.to_csv, "acg_tillamook2022_fvr-55_cloudysky_1s.csv", index=False)

# # Callback for NetCDF download
# @callback(
#     Output(component_id='download-dataframe-netcdf', component_property='data'),
#     Input(component_id='btn-download-netcdf', component_property='n_clicks'),
#     State('data-dropdown', 'value')
# )
# def download_netcdf(n_clicks, data_url):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     # Convert DataFrame back to xarray Dataset for NetCDF download
#     dataset = df.set_index(['time', 'trajectory_id']).to_xarray()
#     buffer = io.BytesIO()
#     dataset.to_netcdf(buffer)
#     buffer.seek(0)
#     return dcc.send_bytes(buffer.getvalue(), "acg_tillamook2022_fvr-55_cloudysky_1s.nc")

# # Combined callback to update the download link and control the modal display
# @callback(
#     Output('modal-centered', 'is_open'),
#     Output('download-link', 'href'),
#     [Input('btn-full-download', 'n_clicks'), Input('close-centered', 'n_clicks')],
#     [State('modal-centered', 'is_open'), State('data-dropdown', 'value')]
# )
# def toggle_modal(btn_full_clicks, btn_close_clicks, is_open, data_url):
#     ctx = dash.callback_context
#     if not ctx.triggered:
#         return is_open, dash.no_update
#     button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#     if button_id == 'btn-full-download':
#         if not is_open:
#             return True, data_url
#         return not is_open, data_url
#     elif button_id == 'close-centered':
#         return not is_open, data_url
#     return is_open, data_url

# @callback(
#     Output('download-selected-data', 'data'),
#     Input('btn-download-selected', 'n_clicks'),
#     State('data-dropdown', 'value'),
#     State('checkboxes', 'value')
# )
# def download_selected_variables(n_clicks, data_url, selected_variables):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     if len(selected_variables) == 0:
#         return dash.no_update
#     df_selected = df[['time'] + selected_variables]
#     # Create a buffer to hold the file content
#     with io.BytesIO() as buffer:
#         if 'time' in df_selected.columns:
#             df_selected.set_index('time').to_xarray().to_netcdf(buffer)
#         else:
#             df_selected.to_xarray().to_netcdf(buffer)
#         buffer.seek(0)
#         return dcc.send_bytes(buffer.read(), "selected_data.nc")
































import dash
from dash import html, dcc, callback, Output, Input, State, get_relative_path
import plotly.graph_objects as go
import dash_design_kit as ddk
import dash_bootstrap_components as dbc
import requests
import xarray as xr
import io
import pandas as pd


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
available_columns = df_initial.columns.tolist()
plot_columns = [col for col in available_columns if col != 'trajectory_id']


# Register the page with Dash
dash.register_page(__name__, path="/1d_data_plots")


menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='1D Data Visualization',
        default_open=False,
        children=[
            dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
            dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
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
        ]
    ),
])


# Define the layout using Dash Design Kit
def layout(project="unknown", **kwargs):
    return ddk.Block([
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False, style={'width': '250px'}),
            ddk.Block([
                ddk.Card("Welcome to ACG-DataViz!"),
                dcc.Dropdown(
                    options=[
                        {'label': '1 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'},
                        {'label': '30 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_30s.nc'}
                    ],
                    value='https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc',
                    id='data-dropdown',
                    clearable=False
                ),
                dcc.Dropdown(
                    id='flight-dropdown',
                    options=[{'label': flight, 'value': flight} for flight in unique_flights],
                    placeholder='Select a flight',
                    clearable=False
                ),
                ddk.Row([
                    ddk.Block([
                        ddk.Card([
                            ddk.Row([
                                dcc.Dropdown(
                                    id='dropdown-plot1',
                                    options=[{'label': col, 'value': col} for col in plot_columns],
                                    value='pressure_altitude_ft',
                                    clearable=False,
                                    style={'width': '300px', 'margin-bottom': '10px'}
                                )
                            ]),
                            dcc.Loading(dcc.Graph(figure={}, id='graph-plot1'))
                        ], width=100, style={'margin-top': '20px'})
                    ], width=50),
                    ddk.Block([
                        ddk.Card([
                            dcc.Dropdown(
                                id='dropdown-plot2',
                                options=[{'label': col, 'value': col} for col in plot_columns],
                                value='fast_ambient_T',
                                clearable=False,
                                style={'width': '300px', 'margin-bottom': '10px'}
                            ),
                            dcc.Loading(dcc.Graph(figure={}, id='graph-plot2'))
                        ], width=100, style={'margin-top': '20px'})
                    ], width=50)
                ]),
                ddk.Row([
                    ddk.Card([
                        dcc.Loading(ddk.DataTable(data=[], page_size=12, style_table={'overflowX': 'auto'}, id='data-table'))
                    ], width=100)
                ]),
                html.Button('Download', id='btn-full-download', n_clicks=0),
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Header"), close_button=True),
                        dbc.ModalBody([
                            "This modal is vertically centered. Click outside this modal to close.",
                            dcc.Checklist(
                                id='variable-checklist',
                                options=[{'label': col, 'value': col} for col in available_columns],
                                value=[],
                                inline=True,
                                style={'margin-top': '20px'}
                            ),
                            html.Button("Download Selected Variables", id="btn-download-selected", n_clicks=0),
                            html.Button("Download Current Dataset: CSV", id="btn-download-csv"),
                            html.Button("Download Current Dataset: NetCDF", id="btn-download-netcdf")
                        ]),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close",
                                id="close-centered",
                                className="ms-auto",
                                n_clicks=0,
                            ),
                        ),
                        html.A('Download Link: Full NetCDF', id='download-link', target='_blank', style={'display': 'block', 'margin-top': '20px'})
                    ],
                    id="modal-centered",
                    centered=True,
                    is_open=False,
                ),
                dcc.Download(id='download-selected'),
                dcc.Download(id='download-dataframe-csv'),
                dcc.Download(id='download-dataframe-netcdf')
            ], style={'width': 'calc(100% - 250px)'})  # Adjust the width to fit the rest of the screen
        ])
    ])


# Callback to update the table based on dropdown selection
@callback(
    Output('data-table', 'data'),
    Input('flight-dropdown', 'value'),
    State('data-dropdown', 'value')
)
def update_table(flight_chosen, data_url):
    df = load_data(data_url)
    # Filter data by the selected flight
    if flight_chosen:
        df = df[df['trajectory_id'] == flight_chosen]
    return df.to_dict('records')


# Callback to update the scatter plots
@callback(
    Output('graph-plot1', 'figure'),
    Output('graph-plot2', 'figure'),
    Input('flight-dropdown', 'value'),
    Input('dropdown-plot1', 'value'),
    Input('dropdown-plot2', 'value'),
    State('data-dropdown', 'value')
)
def update_graph(flight_chosen, col_chosen1, col_chosen2, data_url):
    df = load_data(data_url)
    # Filter data by the selected flight
    if flight_chosen:
        df = df[df['trajectory_id'] == flight_chosen]
    fig1 = go.Figure()
    fig2 = go.Figure()
    if not df.empty:
        if col_chosen1 in df.columns:
            fig1.add_trace(go.Scatter(x=df['time'], y=df[col_chosen1], mode='markers', marker=dict(color=df[col_chosen1], colorscale='viridis', colorbar=dict(title=col_chosen1))))
            fig1.update_layout(title=col_chosen1)
        if col_chosen2 in df.columns:
            fig2.add_trace(go.Scatter(x=df['time'], y=df[col_chosen2], mode='markers', marker=dict(color=df[col_chosen2], colorscale='viridis', colorbar=dict(title=col_chosen2))))
            fig2.update_layout(title=col_chosen2)
    return fig1, fig2


# Callback for CSV download
@callback(
    Output(component_id='download-dataframe-csv', component_property='data'),
    Input(component_id='btn-download-csv', component_property='n_clicks'),
    State('data-dropdown', 'value')
)
def download_csv(n_clicks, data_url):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    df = load_data(data_url)
    return dcc.send_data_frame(df.to_csv, "acg_tillamook2022_fvr-55_cloudysky_1s.csv", index=False)


# Callback for NetCDF download
@callback(
    Output(component_id='download-dataframe-netcdf', component_property='data'),
    Input(component_id='btn-download-netcdf', component_property='n_clicks'),
    State('data-dropdown', 'value')
)

def download_netcdf(n_clicks, data_url):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    df = load_data(data_url)
    # Convert DataFrame back to xarray Dataset for NetCDF download
    dataset = df.set_index(['time', 'trajectory_id']).to_xarray()
    buffer = io.BytesIO()
    dataset.to_netcdf(buffer)
    buffer.seek(0)
    return dcc.send_bytes(buffer.getvalue(), "acg_tillamook2022_fvr-55_cloudysky_1s.nc")




# Combined callback to update the download link and control the modal display
@callback(
    Output('modal-centered', 'is_open'),
    Output('download-link', 'href'),
    [Input('btn-full-download', 'n_clicks'), Input('close-centered', 'n_clicks')],
    [State('modal-centered', 'is_open'), State('data-dropdown', 'value')]
)
def toggle_modal(btn_full_clicks, btn_close_clicks, is_open, data_url):
    ctx = dash.callback_context
    if not ctx.triggered:
        return is_open, dash.no_update
    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    if button_id == 'btn-full-download':
        if not is_open:
            return True, data_url
        return not is_open, data_url
    elif button_id == 'close-centered':
        return not is_open, data_url
    return is_open, data_url




@callback(
    Output('download-selected-data', 'data'),
    Input('btn-download-selected', 'n_clicks'),
    State('data-dropdown', 'value'),
    State('checkboxes', 'value')
)
def download_selected_variables(n_clicks, data_url, selected_variables):
    if n_clicks is None:
        raise dash.exceptions.PreventUpdate
    df = load_data(data_url)
    if len(selected_variables) == 0:
        return dash.no_update
    df_selected = df[['time'] + selected_variables]
    # Create a buffer to hold the file content
    with io.BytesIO() as buffer:
        if 'time' in df_selected.columns:
            df_selected.set_index('time').to_xarray().to_netcdf(buffer)
        else:
            df_selected.to_xarray().to_netcdf(buffer)
        buffer.seek(0)
        return dcc.send_bytes(buffer.read(), "selected_data.nc")

































# import dash
# from dash import html, dcc, callback, Output, Input, State, get_relative_path
# import plotly.graph_objects as go
# import dash_design_kit as ddk
# import dash_bootstrap_components as dbc
# import requests
# import xarray as xr
# import io
# import pandas as pd


# # Function to load data from URL and convert to DataFrame
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content)).set_coords("time").swap_dims({"row": "time"})
#         df = dataset.to_dataframe().reset_index()
#         return df
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return pd.DataFrame()  # Return an empty DataFrame in case of error


# # Load initial data to get unique flight IDs
# data_url = 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'
# df_initial = load_data(data_url)
# unique_flights = df_initial['trajectory_id'].unique()
# available_columns = df_initial.columns.tolist()


# # Register the page with Dash
# dash.register_page(__name__, path="/1d_data_plots")


# menu = ddk.Menu([
#     ddk.CollapsibleMenu(
#         title='1D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
#             dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
#         ]
#     ),
#     ddk.CollapsibleMenu(
#         title='2D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('CDP', href=get_relative_path('/cdp')),
#             dcc.Link('MSEMS', href=get_relative_path('/msems')),
#             dcc.Link('POPS - not done', href=get_relative_path('/pops'))
#         ]
#     ),
#     ddk.CollapsibleMenu(
#         title='3D Data Visualization',
#         default_open=False,
#         children=[
#             dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/trajectory_3d')),
#         ]
#     ),
# ])


# def layout(project="unknown", **kwargs):
#     return ddk.App([
#         ddk.Card("Welcome to DataViz! --This is a test program, NOT REAL--"),
#         ddk.Sidebar([
#                 menu
#             ], foldable=False),
#         dcc.Dropdown(
#             options=[
#                 {'label': '1 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'},
#                 {'label': '30 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_30s.nc'}
#             ],
#             id='data-dropdown',
#             clearable=False,
#             placeholder='Select data'
#         ),
#         dcc.Dropdown(
#             id='flight-dropdown',
#             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#             placeholder='Select a flight',
#             clearable=False
#         ),
#         ddk.Row([
#             ddk.Card([
#                 dcc.Dropdown(
#                     id='dropdown-plot1',
#                     options=[
#                         {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                         {'label': 'altitude', 'value': 'altitude'},
#                         {'label': 'true_air_speed', 'value': 'true_air_speed'}
#                     ],
#                     placeholder='Select variable',
#                     clearable=False
#                 ),
#                 dcc.Loading(dcc.Graph(figure={}, id='graph-plot1'))
#             ], width=50),
#             ddk.Card([
#                 dcc.Dropdown(
#                     id='dropdown-plot2',
#                     options=[
#                         {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                         {'label': 'altitude', 'value': 'altitude'},
#                         {'label': 'true_air_speed', 'value': 'true_air_speed'},
#                         {'label': 'ground_speed', 'value': 'ground_speed'},
#                         {'label': 'pressure_altitude', 'value': 'pressure_altitude'},
#                         {'label': 'height_agl', 'value': 'height_agl'}
#                     ],
#                     placeholder='Select variable',
#                     clearable=False
#                 ),
#                 dcc.Loading(dcc.Graph(figure={}, id='graph-plot2'))
#             ], width=50),
#         ]),
#         ddk.Row([
#             ddk.Card([
#                 dcc.Loading(ddk.DataTable(data=[], page_size=12, style_table={'overflowX': 'auto'}, id='data-table'))
#             ], width=100)
#         ]),
#         html.Button('Full Download', id='btn-full-download', n_clicks=0),
#         dbc.Modal(
#             [
#                 dbc.ModalHeader(dbc.ModalTitle("Header"), close_button=True),
#                 dbc.ModalBody([
#                     "This modal is vertically centered. Click outside this modal to close.",
#                     dcc.Checklist(
#                         id='variable-checklist',
#                         options=[{'label': col, 'value': col} for col in available_columns],
#                         value=[],
#                         inline=True,
#                         style={'margin-top': '20px'}
#                     ),
#                     html.Button("Download Selected Variables", id="btn-download-selected", n_clicks=0),
#                     html.Button("Download Current Dataset: CSV", id="btn-download-csv"),
#                     html.Button("Download Current Dataset: NetCDF", id="btn-download-netcdf")
#                 ]),
#                 dbc.ModalFooter(
#                     dbc.Button(
#                         "Close",
#                         id="close-centered",
#                         className="ms-auto",
#                         n_clicks=0,
#                     ),
#                 ),
#                 html.A('Download Link: Full NetCDF', id='download-link', target='_blank', style={'display': 'block', 'margin-top': '20px'})
#             ],
#             id="modal-centered",
#             centered=True,
#             is_open=False,
#         ),
#         dcc.Download(id='download-selected'),
#         dcc.Download(id='download-dataframe-csv'),
#         dcc.Download(id='download-dataframe-netcdf')
#     ])


# # Callback to update the table based on dropdown selection
# @callback(
#     Output('data-table', 'data'),
#     Input('flight-dropdown', 'value'),
#     State('data-dropdown', 'value')
# )
# def update_table(flight_chosen, data_url):
#     if not data_url or not flight_chosen:
#         return []  # Return empty data if no flight or data URL is selected
#     df = load_data(data_url)
#     # Filter data by the selected flight
#     if flight_chosen:
#         df = df[df['trajectory_id'] == flight_chosen]
#     return df.to_dict('records')


# # Callback to update the scatter plots
# @callback(
#     Output('graph-plot1', 'figure'),
#     Output('graph-plot2', 'figure'),
#     Input('flight-dropdown', 'value'),
#     Input('dropdown-plot1', 'value'),
#     Input('dropdown-plot2', 'value'),
#     State('data-dropdown', 'value')
# )
# def update_graph(flight_chosen, col_chosen1, col_chosen2, data_url):
#     if not data_url or not flight_chosen or not col_chosen1 or not col_chosen2:
#         return go.Figure(), go.Figure()  # Return empty figures if necessary values are not selected
#     df = load_data(data_url)
#     # Filter data by the selected flight
#     if flight_chosen:
#         df = df[df['trajectory_id'] == flight_chosen]
#     fig1 = go.Figure()
#     fig2 = go.Figure()
#     if not df.empty:
#         if col_chosen1 in df.columns:
#             fig1.add_trace(go.Scatter(x=df['time'], y=df[col_chosen1], mode='markers', marker=dict(color=df[col_chosen1], colorscale='viridis', colorbar=dict(title=col_chosen1))))
#             fig1.update_layout(title=col_chosen1)
#         if col_chosen2 in df.columns:
#             fig2.add_trace(go.Scatter(x=df['time'], y=df[col_chosen2], mode='markers', marker=dict(color=df[col_chosen2], colorscale='plasma', colorbar=dict(title=col_chosen2))))
#             fig2.update_layout(title=col_chosen2)
#     return fig1, fig2


# # Callback for CSV download
# @callback(
#     Output(component_id='download-dataframe-csv', component_property='data'),
#     Input(component_id='btn-download-csv', component_property='n_clicks'),
#     State('data-dropdown', 'value')
# )
# def download_csv(n_clicks, data_url):
#     if n_clicks is None or not data_url:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     return dcc.send_data_frame(df.to_csv, "data.csv")


# # Callback for NetCDF download
# @callback(
#     Output('download-dataframe-netcdf', 'data'),
#     Input('btn-download-netcdf', 'n_clicks'),
#     State('data-dropdown', 'value')
# )
# def download_netCDF(n_clicks, data_url):
#     if n_clicks is None or not data_url:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     return dcc.send_data_frame(df.to_xarray().to_netcdf, "data.nc")


# # Callback for selected variables download
# @callback(
#     Output('download-selected', 'data'),
#     Input('btn-download-selected', 'n_clicks'),
#     State('data-dropdown', 'value'),
#     State('variable-checklist', 'value')
# )
# def download_selected_vars(n_clicks, data_url, selected_vars):
#     if n_clicks is None or not data_url or not selected_vars:
#         raise dash.exceptions.PreventUpdate
#     df = load_data(data_url)
#     df_selected = df[selected_vars]
#     return dcc.send_data_frame(df_selected.to_csv, "selected_variables.csv")


# # Callback for updating download link
# @callback(
#     Output('download-link', 'href'),
#     Input('btn-full-download', 'n_clicks')
# )
# def update_download_link(n_clicks):
#     if n_clicks is None:
#         raise dash.exceptions.PreventUpdate
#     return data_url  # Update with the actual download link logic






