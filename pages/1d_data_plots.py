from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='1D Data Tillamook',
    top_nav=True,
    path='/1d_data_plots'
)

def layout():
    return html.Div([
        html.H1("1D Data Here.")
    ])
    



# import dash
# from dash import html, dcc, callback, Output, Input, State
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




# # Define the layout using Dash Design Kit
# layout = ddk.App([
#     ddk.Card("Welcome to DataViz! --This is a test program, NOT REAL--"),
#     dcc.Dropdown(
#         options=[
#             {'label': '1 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc'},
#             {'label': '30 Second Data', 'value': 'https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_30s.nc'}
#         ],
#         value='https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc',
#         id='data-dropdown',
#         clearable=False
#     ),
#     dcc.Dropdown(
#         id='flight-dropdown',
#         options=[{'label': flight, 'value': flight} for flight in unique_flights],
#         placeholder='Select a flight',
#         clearable=False
#     ),
#     ddk.Row([
#         ddk.Card([
#             dcc.Dropdown(
#                 id='dropdown-plot1',
#                 options=[
#                     {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                     {'label': 'altitude', 'value': 'altitude'},
#                     {'label': 'true_air_speed', 'value': 'true_air_speed'}
#                 ],
#                 value='altitude',
#                 clearable=False
#             ),
#             dcc.Loading(dcc.Graph(figure={}, id='graph-plot1'))
#         ], width=50),
#         ddk.Card([
#             dcc.Dropdown(
#                 id='dropdown-plot2',
#                 options=[
#                     {'label': 'cdp_laser_current', 'value': 'cdp_laser_current'},
#                     {'label': 'altitude', 'value': 'altitude'},
#                     {'label': 'true_air_speed', 'value': 'true_air_speed'},
#                     {'label': 'ground_speed', 'value': 'ground_speed'},
#                     {'label': 'pressure_altitude', 'value': 'pressure_altitude'},
#                     {'label': 'height_agl', 'value': 'height_agl'}
#                 ],
#                 value='true_air_speed',
#                 clearable=False
#             ),
#             dcc.Loading(dcc.Graph(figure={}, id='graph-plot2'))
#         ], width=50),
#     ]),
#     ddk.Row([
#         ddk.Card([
#             dcc.Loading(ddk.DataTable(data=[], page_size=12, style_table={'overflowX': 'auto'}, id='data-table'))
#         ], width=100)
#     ]),
#     ddk.Row([
#         dcc.Download(id='download-dataframe-csv'),
#         dcc.Download(id='download-dataframe-netcdf'),
#         ddk.Card([
#             html.Button("Download Current Dataset: CSV", id="btn-download-csv")
#         ], width=50),
#         ddk.Card([
#             html.Button("Download Current Dataset: NetCDF", id="btn-download-netcdf")
#         ], width=50)
#     ]),
#     html.Button('Full Download', id='btn-full-download', n_clicks=0),
#     dbc.Modal(
#         [
#             dbc.ModalHeader(dbc.ModalTitle("Header"), close_button=True),
#             dbc.ModalBody([
#                 "This modal is vertically centered. Click outside this modal to close.",
#                 dcc.Checklist(
#                     id='variable-checklist',
#                     options=[{'label': col, 'value': col} for col in available_columns],
#                     value=[],
#                     inline=True,
#                     style={'margin-top': '20px'}
#                 ),
#                 html.Button("Download Selected Variables", id="btn-download-selected", n_clicks=0)
#             ]),
#             dbc.ModalFooter(
#                 dbc.Button(
#                     "Close",
#                     id="close-centered",
#                     className="ms-auto",
#                     n_clicks=0,
#                 ),
#             ),
#             html.A('Download Link: Full NetCDF', id='download-link', target='_blank', style={'display': 'block', 'margin-top': '20px'})
#         ],
#         id="modal-centered",
#         centered=True,
#         is_open=False,
#     ),
#     dcc.Download(id='download-selected')
# ])




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