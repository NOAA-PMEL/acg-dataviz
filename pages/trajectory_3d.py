#############################################################################################
###############################     3D, Two companions        ###############################
#############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, no_update, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go




# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")
# # dash.register_page(__name__, path_template="/trajectory")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None




# # Load the data for CDP (assuming similar structure as previous page)
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# # global df
# df = load_data(data_url)
# # # print(df)



# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []
# # print(unique_flights)



# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # print(columns)


# # Define the layout using Dash Design Kit
# # layout = ddk.Block([
# def layout(project="unknown", **kwargs): 
#     layout = ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False), # style={'background-color': '#add8e6'}
#             ddk.Block([
#                 ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Card(dcc.Dropdown(
#                     id='flight-dropdown-2',
#                     options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                     placeholder='Select a flight',
#                     clearable=False
#                 )),
#                 ddk.Card([
#                     dcc.Dropdown(
#                         id='color-dropdown-2',
#                         options=[{'label': col, 'value': col} for col in columns],
#                         # placeholder='Select a variable for color',
#                         value='cdp_intN',
#                         clearable=False,
#                         style={'width': '200px', 'margin-bottom': '10px'}
#                     ),
#                     dcc.Loading(dcc.Graph(id='trajectory-graph-2', style={'height': '600px'}))  # Use dcc.Loading and dcc.Graph
#                     # dcc.Graph(id='trajectory-graph-2', style={'height': '600px'})  # Use dcc.Loading and dcc.Graph
#                 ]),
#                 ddk.Card([
#                     ddk.Block(width=50, children=[
#                         dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2'))  # Use dcc.Loading and dcc.Graph
#                     ]),
#                     ddk.Block(width=50, children=[
#                         dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2'))  # Use dcc.Loading and dcc.Graph
#                     ])
#                 ])
#             ])
#         ])
#     ])
#     return layout
    


# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     # global df 

#     print(f"here:1 {selected_flight}, {color_var}")
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure()
    
#     print(f"pre-error {selected_flight}, {color_var}")
    
#     # Filter data for the selected flight
#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update
#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     print(f"post-error {selected_data}")


#     # Extract latitude, longitude, and altitude columns
#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values


#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])

#     # Update 3D scatter plot layout
#     fig_3d.update_layout(
#         title=f'3D Scatter Plot of Latitude, Longitude, and Altitude for Flight {selected_flight}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )


#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8
#         )
#     )])


#     # Update 2D scatter plot layout for Longitude vs Altitude
#     fig_long_alt.update_layout(
#         title=f'2D Scatter Plot of Longitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )


#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8
#         )
#     )])


#     # Update 2D scatter plot layout for Latitude vs Altitude
#     fig_lat_alt.update_layout(
#         title=f'2D Scatter Plot of Latitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )
#     print("here:2")

#     return fig_3d, fig_long_alt, fig_lat_alt


#############################################################################################
############################     End of 3D, Two companions        ###########################
#############################################################################################
































#############################################################################################
##################     3D, Two companions, top view, top view map        ####################
#############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),  # style={'background-color': '#add8e6'}
#             ddk.Block([
#                 ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Card(dcc.Dropdown(
#                     id='flight-dropdown-2',
#                     options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                     placeholder='Select a flight',
#                     clearable=False
#                 )),
#                 ddk.Block([
#                     dcc.Dropdown(
#                         id='color-dropdown-2',
#                         options=[{'label': col, 'value': col} for col in columns],
#                         value='cdp_intN',
#                         clearable=False,
#                         style={'width': '200px', 'margin-bottom': '10px'}
#                     ),
#                     ddk.Row([
#                         ddk.Block(width=33, children=[
#                             dcc.Loading(dcc.Graph(id='trajectory-graph-2'))
#                         ]),
#                         ddk.Block(width=33, children=[
#                             dcc.Loading(dcc.Graph(id='lat-long-plot-2'))
#                         ]),
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block(width=33, children=[
#                         dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2'))
#                     ]),
#                     ddk.Block(width=33, children=[
#                         dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2'))
#                     ]),
#                 ]),
#                 ddk.Block([
#                     dcc.Loading(dl.Map(
#                         center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                         zoom=13,
#                         children=[
#                             dl.TileLayer(
#                                 url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                 attribution="© CartoDB"
#                             ),
#                             dl.LayerGroup(id="flight-path-layer"),
#                         ],
#                         style={'width': '100%', 'height': '600px'}
#                     ))
#                 ])
#             ])
#         ])
#     ])

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('lat-long-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'3D Scatter Plot of Latitude, Longitude, and Altitude for Flight {selected_flight}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'2D Scatter Plot of Longitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'2D Scatter Plot of Latitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Longitude
#     fig_lat_long = go.Figure(data=[go.Scatter(
#         x=x,
#         y=y,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_long.update_layout(
#         title=f'2D Scatter Plot of Latitude and Longitude for Flight {selected_flight}',
#         xaxis_title='Longitude',
#         yaxis_title='Latitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, fig_lat_long, [flight_path]


#############################################################################################
###############     End of 3D, Two companions, top view, top view map        ################
#############################################################################################

































#############################################################################################
#######################     3D, Two companions, top view map        #########################
#############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),  # style={'background-color': '#add8e6'}
#             ddk.Block([
#                 ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Row([
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='flight-dropdown-2',
#                             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                             placeholder='Select a flight',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ]),
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='color-dropdown-2',
#                             options=[{'label': col, 'value': col} for col in columns],
#                             value='cdp_intN',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ])
#                 ]),
#                 ddk.Block([
#                     ddk.Row([
#                         ddk.Block(width=50, children=[
#                             ddk.Card(dcc.Loading(dcc.Graph(id='trajectory-graph-2')))
#                         ]),
#                         ddk.Block(width=50, children=[
#                             ddk.Card(dcc.Loading(dl.Map(
#                                 center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                                 zoom=12,
#                                 children=[
#                                     dl.TileLayer(
#                                         url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                         attribution="© CartoDB"
#                                     ),
#                                     dl.LayerGroup(id="flight-path-layer"),
#                                 ],
#                                 style={'width': '100%', 'height': '450px'}
#                             )))
#                         ]),
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block(width=50, children=[
#                         ddk.Card(dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')))
#                     ]),
#                     ddk.Block(width=50, children=[
#                         ddk.Card(dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2')))
#                     ]),
#                 ])
#             ])
#         ])
#     ])

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'3D Scatter Plot of Latitude, Longitude, and Altitude for Flight {selected_flight}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'2D Scatter Plot of Longitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'2D Scatter Plot of Latitude and Altitude for Flight {selected_flight}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]


#############################################################################################
####################     End of 3D, Two companions, top view map        #####################
#############################################################################################























### currently my favorite
#############################################################################################
###############     3D, Two companions stacked, top view map, card right     ################
#############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),  # style={'background-color': '#add8e6'}
#             ddk.Block([
#                 ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Row([
#                     ddk.Card(width=1, children=[
#                         dcc.Dropdown(
#                             id='flight-dropdown-2',
#                             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                             placeholder='Select a flight',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ]),
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='color-dropdown-2',
#                             options=[{'label': col, 'value': col} for col in columns],
#                             value='cdp_intN',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block([
#                         ddk.Card([dcc.Loading(dcc.Graph(id='trajectory-graph-2'))], style={'margin-bottom': 2}),
#                         ddk.Card(dcc.Loading(dl.Map(
#                             center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                             zoom=12,
#                             children=[
#                                 dl.TileLayer(
#                                     url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                     attribution="© CartoDB"
#                                 ),
#                                 dl.LayerGroup(id="flight-path-layer"),
#                             ],
#                             style={'width': '100%', 'height': '450px'}
#                         )))
#                     ]),
#                     ddk.Block([
#                         # ddk.Card([
#                         #     ddk.Card(dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2'), style={'height': 200}), style={'height': 440}),
#                         #     ddk.Card(dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2'), style={'height': 400}), style={'height': 440})
#                         # ], style={'height': 970})

#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')),
#                             html.Div(style={'height': '38px'}),
#                             dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2'))
#                         ])
#                     ])
#                 ])
#             ]),
#             ddk.Card([
#                 html.B("3D Trajectory Plot"), html.Br(), html.Br(), "Select a flight and variable to view the drone's flight trajectory with concentration levels.", html.Br(),html.Br(), "See the built-in toolbar for options: Download png of plot, zoom in/out, multiple rotation options, and camera reset.",
#                 html.Br(),html.Br(),html.Br(),
#                 html.B("2D Companion Plots"), html.Br(),html.Br(), "These plots will be populated with the data from the flight selected. These show side views of the flight trajectory with the same color concentration levels.",
#                 html.Br(),html.Br(),html.Br(),
#                 html.B("Map Topview"), html.Br(),html.Br(), "This map shows the top view of the flight trajectory over a map for context. Zoom in and move around the map to see where the drone flew."
#             ], style={'width': 300})
#         ])
#     ])

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Extract the last two digits of the selected flight for titles
#     flight_suffix = str(selected_flight)[-2:]

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis', 
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'Trajectory of Flight {flight_suffix}', #3D Scatter Plot of Latitude, Longitude, and Altitude for Flight {selected_flight}
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'Sideview: Longitude and Altitude Flight {flight_suffix}', #2D Scatter Plot of Longitude and Altitude for Flight {selected_flight}
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'Sideview: Latitude and Altitude Flight {flight_suffix}', #2D Scatter Plot of Latitude and Altitude for Flight {selected_flight}
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]



#############################################################################################
############   End of 3D, Two companions stacked, top view map, card right      #############
#############################################################################################






















## best with expandable
# #############################################################################################
# ############      3D, Two companions stacked, top view map, pop up full        ##############
# #############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, State, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet
# import dash_bootstrap_components as dbc

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),
#             ddk.Block([
#                 # ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Row([
#                     ddk.Card(width=1, children=[
#                         dcc.Dropdown(
#                             id='flight-dropdown-2',
#                             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                             placeholder='Select a flight',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ]),
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='color-dropdown-2',
#                             options=[{'label': col, 'value': col} for col in columns],
#                             value='cdp_intN',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='trajectory-graph-2')),
#                             dbc.Button("Expand", id="open-modal-trajectory", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'margin-bottom': 0}),
#                         ddk.Card([
#                             dcc.Loading(dl.Map(
#                                 center=[45.4470, -123.8428],  # Default center (Tillamook, OR)
#                                 zoom=12,
#                                 children=[
#                                     dl.TileLayer(
#                                         url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                         attribution="© CartoDB"
#                                     ),
#                                     dl.LayerGroup(id="flight-path-layer"),
#                                 ],
#                                 style={'width': '100%', 'height': '400px'}
#                             )),
#                             dbc.Button("Expand", id="open-modal-map", n_clicks=0, color="primary", className="mt-2")
#                         ])
#                     ]),
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')),
#                             html.Br(),
#                             dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2')),
#                             dbc.Button("Expand", id="open-modal-sideplots", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'height': 998})
#                     ])
#                 ]),
#                 # Define modals
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Trajectory Graph"),
#                     dbc.ModalBody(dcc.Graph(id='trajectory-graph-modal')),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-trajectory", className="ml-auto")
#                     ),
#                 ], id="modal-trajectory", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Map"),
#                     dbc.ModalBody(dl.Map(
#                         center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                         zoom=12,
#                         children=[
#                             dl.TileLayer(
#                                 url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                 attribution="© CartoDB"
#                             ),
#                             dl.LayerGroup(id="flight-path-layer-modal"),
#                         ],
#                         style={'width': '100%', 'height': '80vh'}
#                     )),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-map", className="ml-auto")
#                     ),
#                 ], id="modal-map", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Side Plots"),
#                     dbc.ModalBody(html.Div([
#                         dcc.Graph(id='longitude-altitude-plot-modal'),
#                         html.Br(),
#                         dcc.Graph(id='latitude-altitude-plot-modal')
#                     ])),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-sideplots", className="ml-auto")
#                     ),
#                 ], id="modal-sideplots", size="xl", is_open=False)
#             ])
#         ])
#     ])

# # Define callbacks to handle the modals
# @callback(
#     Output("modal-trajectory", "is_open"),
#     Output("trajectory-graph-modal", "figure"),
#     Input("open-modal-trajectory", "n_clicks"),
#     Input("close-modal-trajectory", "n_clicks"),
#     State("modal-trajectory", "is_open"),
#     State("trajectory-graph-2", "figure")
# )
# def toggle_modal_trajectory(n1, n2, is_open, figure):
#     if n1 or n2:
#         return not is_open, figure
#     return is_open, figure

# @callback(
#     Output("modal-map", "is_open"),
#     Output("flight-path-layer-modal", "children"),
#     Input("open-modal-map", "n_clicks"),
#     Input("close-modal-map", "n_clicks"),
#     State("modal-map", "is_open"),
#     State("flight-path-layer", "children")
# )
# def toggle_modal_map(n1, n2, is_open, flight_path):
#     if n1 or n2:
#         return not is_open, flight_path
#     return is_open, flight_path

# @callback(
#     Output("modal-sideplots", "is_open"),
#     Output("longitude-altitude-plot-modal", "figure"),
#     Output("latitude-altitude-plot-modal", "figure"),
#     Input("open-modal-sideplots", "n_clicks"),
#     Input("close-modal-sideplots", "n_clicks"),
#     State("modal-sideplots", "is_open"),
#     State("longitude-altitude-plot-2", "figure"),
#     State("latitude-altitude-plot-2", "figure")
# )
# def toggle_modal_sideplots(n1, n2, is_open, long_fig, lat_fig):
#     if n1 or n2:
#         return not is_open, long_fig, lat_fig
#     return is_open, long_fig, lat_fig

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Extract the last two digits of the selected flight
#     flight_suffix = str(selected_flight)[-2:]

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'3D Trajectory for Flight {flight_suffix}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'Sideview: Longitude Flight {flight_suffix}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'Sideview: Latitude Flight {flight_suffix}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]

# #############################################################################################
# ################     End of 3D, Two companions stacked, top view map        #################
# #############################################################################################

























# ## 2
# #############################################################################################
# #######      3D, Two companions stacked, top view map, pop up full, text RIGHT        #######
# #############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, State, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet
# import dash_bootstrap_components as dbc

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),
#             ddk.Block([
#                 # ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Row([
#                     ddk.Card(width=1, children=[
#                         dcc.Dropdown(
#                             id='flight-dropdown-2',
#                             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                             placeholder='Select a flight',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ]),
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='color-dropdown-2',
#                             options=[{'label': col, 'value': col} for col in columns],
#                             value='cdp_intN',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='trajectory-graph-2')),
#                             dbc.Button("Expand", id="open-modal-trajectory", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'margin-bottom': 0}),
#                         ddk.Card([
#                             dcc.Loading(dl.Map(
#                                 center=[45.4470, -123.8428],  # Default center (Tillamook, OR)
#                                 zoom=12,
#                                 children=[
#                                     dl.TileLayer(
#                                         url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                         attribution="© CartoDB"
#                                     ),
#                                     dl.LayerGroup(id="flight-path-layer"),
#                                 ],
#                                 style={'width': '100%', 'height': '400px'}
#                             )),
#                             dbc.Button("Expand", id="open-modal-map", n_clicks=0, color="primary", className="mt-2")
#                         ])
#                     ]),
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')),
#                             html.Br(),
#                             dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2')),
#                             dbc.Button("Expand", id="open-modal-sideplots", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'height': 998})
#                     ])
#                 ]),
#                 # Define modals
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Trajectory Graph"),
#                     dbc.ModalBody(dcc.Graph(id='trajectory-graph-modal')),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-trajectory", className="ml-auto")
#                     ),
#                 ], id="modal-trajectory", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Map"),
#                     dbc.ModalBody(dl.Map(
#                         center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                         zoom=12,
#                         children=[
#                             dl.TileLayer(
#                                 url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                 attribution="© CartoDB"
#                             ),
#                             dl.LayerGroup(id="flight-path-layer-modal"),
#                         ],
#                         style={'width': '100%', 'height': '80vh'}
#                     )),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-map", className="ml-auto")
#                     ),
#                 ], id="modal-map", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Side Plots"),
#                     dbc.ModalBody(html.Div([
#                         dcc.Graph(id='longitude-altitude-plot-modal'),
#                         html.Br(),
#                         dcc.Graph(id='latitude-altitude-plot-modal')
#                     ])),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-sideplots", className="ml-auto")
#                     ),
#                 ], id="modal-sideplots", size="xl", is_open=False)
#             ]),
#             ddk.Card([
#                     html.B("3D Trajectory Plot"), html.Br(), html.Br(), "Select a flight and variable to view the drone's flight trajectory with concentration levels.", html.Br(),html.Br(), "See the built-in toolbar for options: Download png of plot, zoom in/out, multiple rotation options, and camera reset.",
#                     html.Br(),html.Br(),html.Br(),
#                     html.B("2D Companion Plots"), html.Br(),html.Br(), "These plots will be populated with the data from the flight selected. These show side views of the flight trajectory with the same color concentration levels.",
#                     html.Br(),html.Br(),html.Br(),
#                     html.B("Map Topview"), html.Br(),html.Br(), "This map shows the top view of the flight trajectory over a map for context. Zoom in and move around the map to see where the drone flew."
#                 ], style={'width': '20%'})
#         ])
#     ])

# # Define callbacks to handle the modals
# @callback(
#     Output("modal-trajectory", "is_open"),
#     Output("trajectory-graph-modal", "figure"),
#     Input("open-modal-trajectory", "n_clicks"),
#     Input("close-modal-trajectory", "n_clicks"),
#     State("modal-trajectory", "is_open"),
#     State("trajectory-graph-2", "figure")
# )
# def toggle_modal_trajectory(n1, n2, is_open, figure):
#     if n1 or n2:
#         return not is_open, figure
#     return is_open, figure

# @callback(
#     Output("modal-map", "is_open"),
#     Output("flight-path-layer-modal", "children"),
#     Input("open-modal-map", "n_clicks"),
#     Input("close-modal-map", "n_clicks"),
#     State("modal-map", "is_open"),
#     State("flight-path-layer", "children")
# )
# def toggle_modal_map(n1, n2, is_open, flight_path):
#     if n1 or n2:
#         return not is_open, flight_path
#     return is_open, flight_path

# @callback(
#     Output("modal-sideplots", "is_open"),
#     Output("longitude-altitude-plot-modal", "figure"),
#     Output("latitude-altitude-plot-modal", "figure"),
#     Input("open-modal-sideplots", "n_clicks"),
#     Input("close-modal-sideplots", "n_clicks"),
#     State("modal-sideplots", "is_open"),
#     State("longitude-altitude-plot-2", "figure"),
#     State("latitude-altitude-plot-2", "figure")
# )
# def toggle_modal_sideplots(n1, n2, is_open, long_fig, lat_fig):
#     if n1 or n2:
#         return not is_open, long_fig, lat_fig
#     return is_open, long_fig, lat_fig

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Extract the last two digits of the selected flight
#     flight_suffix = str(selected_flight)[-2:]

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'3D Trajectory for Flight {flight_suffix}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'Sideview: Longitude Flight {flight_suffix}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'Sideview: Latitude Flight {flight_suffix}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]

# #############################################################################################
# ################     End of 3D, Two companions stacked, top view map        #################
# #############################################################################################























## 2.5 -------------- best so far
#############################################################################################
#####      3D, Two companions stacked, top view map, pop up full, text RIGHT low        #####
#############################################################################################

import dash
from dash import html, dcc, callback, Output, Input, State, get_relative_path
import dash_design_kit as ddk
import requests
import xarray as xr
import io
import numpy as np
import plotly.graph_objects as go
import dash_leaflet as dl  # Import dash_leaflet
import dash_bootstrap_components as dbc

# Register the page with Dash
dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
df = load_data(data_url)

# Get unique flight IDs
if df is not None:
    unique_flights = np.unique(df['trajectory_id'].values)
else:
    unique_flights = []

# Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
if df is not None:
    columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
else:
    columns = []

# Define the layout using Dash Design Kit
def layout(project="unknown", **kwargs):
    return ddk.Block([
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False),
            ddk.Block([
                # ddk.Card(f"3D Trajectory of 1D Data ({project})"),
                ddk.Row([
                    ddk.Card(children=[
                        dcc.Dropdown(
                            id='flight-dropdown-2',
                            options=[{'label': flight, 'value': flight} for flight in unique_flights],
                            placeholder='Select a flight',
                            clearable=False,
                            style={'width': '100%', 'margin-bottom': '10px'}
                        )
                    ], style={'width': 30}),
                    ddk.Card(children=[
                        dcc.Dropdown(
                            id='color-dropdown-2',
                            options=[{'label': col, 'value': col} for col in columns],
                            value='cdp_intN',
                            clearable=False,
                            style={'width': '100%', 'margin-bottom': '10px'}
                        )
                    ], style={'width': 30})
                ]),
                ddk.Row([
                    ddk.Block([
                        ddk.Card([
                            dcc.Loading(dcc.Graph(id='trajectory-graph-2')),
                            dbc.Button("Expand", id="open-modal-trajectory", n_clicks=0, color="primary", className="mt-2")
                        ], style={'margin-bottom': 0}),
                        ddk.Card([
                            dcc.Loading(dl.Map(
                                center=[45.4470, -123.8428],  # Default center (Tillamook, OR)
                                zoom=12,
                                children=[
                                    dl.TileLayer(
                                        url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
                                        attribution="© CartoDB"
                                    ),
                                    dl.LayerGroup(id="flight-path-layer"),
                                ],
                                style={'width': '100%', 'height': '400px'}
                            )),
                            dbc.Button("Expand", id="open-modal-map", n_clicks=0, color="primary", className="mt-2")
                        ])
                    ]),
                    ddk.Block([
                        ddk.Card([
                            dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')),
                            html.Br(),
                            dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2')),
                            dbc.Button("Expand", id="open-modal-sideplots", n_clicks=0, color="primary", className="mt-2")
                        ], style={'height': 998})
                    ]),
                    ddk.Card([
                        html.B("3D Trajectory Plot"), html.Br(), html.Br(), "Select a flight and variable to view the drone's flight trajectory with concentration levels.", html.Br(),html.Br(), "See the built-in toolbar for options: Download png of plot, zoom in/out, multiple rotation options, and camera reset.",
                        html.Br(),html.Br(),html.Br(),
                        html.B("2D Companion Plots"), html.Br(),html.Br(), "These plots will be populated with the data from the flight selected. These show side views of the flight trajectory with the same color concentration levels.",
                        html.Br(),html.Br(),html.Br(),
                        html.B("Map Topview"), html.Br(),html.Br(), "This map shows the top view of the flight trajectory over a map for context. Zoom in and move around the map to see where the drone flew.",
                        html.Br(),html.Br(), "Click 'Expand' on any of the plots to make full-screen."
                    ], style={'width': '40%'})
                ]),
                # Define modals
                dbc.Modal([
                    dbc.ModalHeader("Expanded Trajectory Graph"),
                    dbc.ModalBody(
                        dcc.Graph(id='trajectory-graph-modal', style={'height': '100%', 'width': '100%'}),
                        style={'height': '80vh'}  # Keep this to control the modal height
                    ),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal-trajectory", className="ml-auto")
                    ),
                ], id="modal-trajectory", size="xl", is_open=False),

                dbc.Modal([
                    dbc.ModalHeader("Expanded Map"),
                    dbc.ModalBody(dl.Map(
                        center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
                        zoom=12,
                        children=[
                            dl.TileLayer(
                                url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
                                attribution="© CartoDB"
                            ),
                            dl.LayerGroup(id="flight-path-layer-modal"),
                        ],
                        style={'width': '100%', 'height': '80vh'}
                    )),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal-map", className="ml-auto")
                    ),
                ], id="modal-map", size="xl", is_open=False),
                
                dbc.Modal([
                    dbc.ModalHeader("Expanded Side Plots"),
                    dbc.ModalBody(html.Div([
                        dcc.Graph(id='longitude-altitude-plot-modal'),
                        html.Br(),
                        dcc.Graph(id='latitude-altitude-plot-modal')
                    ])),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close-modal-sideplots", className="ml-auto")
                    ),
                ], id="modal-sideplots", size="xl", is_open=False)
            ]),
        ])
    ])

# Define callbacks to handle the modals
@callback(
    Output("modal-trajectory", "is_open"),
    Output("trajectory-graph-modal", "figure"),
    Input("open-modal-trajectory", "n_clicks"),
    Input("close-modal-trajectory", "n_clicks"),
    State("modal-trajectory", "is_open"),
    State("trajectory-graph-2", "figure")
)
def toggle_modal_trajectory(n1, n2, is_open, figure):
    if n1 or n2:
        return not is_open, figure
    return is_open, figure

@callback(
    Output("modal-map", "is_open"),
    Output("flight-path-layer-modal", "children"),
    Input("open-modal-map", "n_clicks"),
    Input("close-modal-map", "n_clicks"),
    State("modal-map", "is_open"),
    State("flight-path-layer", "children")
)
def toggle_modal_map(n1, n2, is_open, flight_path):
    if n1 or n2:
        return not is_open, flight_path
    return is_open, flight_path

@callback(
    Output("modal-sideplots", "is_open"),
    Output("longitude-altitude-plot-modal", "figure"),
    Output("latitude-altitude-plot-modal", "figure"),
    Input("open-modal-sideplots", "n_clicks"),
    Input("close-modal-sideplots", "n_clicks"),
    State("modal-sideplots", "is_open"),
    State("longitude-altitude-plot-2", "figure"),
    State("latitude-altitude-plot-2", "figure")
)
def toggle_modal_sideplots(n1, n2, is_open, long_fig, lat_fig):
    if n1 or n2:
        return not is_open, long_fig, lat_fig
    return is_open, long_fig, lat_fig

# Define callback to update trajectory information based on flight and color variable selection
@callback(
    Output('trajectory-graph-2', 'figure'),
    Output('longitude-altitude-plot-2', 'figure'),
    Output('latitude-altitude-plot-2', 'figure'),
    Output('flight-path-layer', 'children'),  # Add output for the map layer
    Input('flight-dropdown-2', 'value'),
    Input('color-dropdown-2', 'value')
)
def update_trajectory_info_2(selected_flight, color_var):
    if selected_flight is None or color_var is None:
        return go.Figure(), go.Figure(), go.Figure(), []

    if df is None:
        return dash.no_update, dash.no_update, dash.no_update, dash.no_update

    selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

    x = selected_data['longitude'].values
    y = selected_data['latitude'].values
    z = selected_data['altitude'].values
    color = selected_data[color_var].values

    # Extract the last two digits of the selected flight
    flight_suffix = str(selected_flight)[-2:]

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
    fig_3d.update_layout(
        title=f'3D Trajectory for Flight {flight_suffix}',
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
            color=color,
            colorscale='Viridis',
            opacity=0.8
        )
    )])
    fig_long_alt.update_layout(
        title=f'Sideview: Longitude and Altitude Flight {flight_suffix}',
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
            color=color,
            colorscale='Viridis',
            opacity=0.8
        )
    )])
    fig_lat_alt.update_layout(
        title=f'Sideview: Latitude and Altitude Flight {flight_suffix}',
        xaxis_title='Latitude',
        yaxis_title='Altitude',
        margin=dict(l=50, r=50, t=80, b=50)
    )

    # Update the map with the flight path
    flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

    return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]

#############################################################################################
################     End of 3D, Two companions stacked, top view map        #################
#############################################################################################


























## 4
# #############################################################################################
# ######   3D, Two companions stacked, top view map, pop up full, text in, map below    #######
# #############################################################################################

# import dash
# from dash import html, dcc, callback, Output, Input, State, get_relative_path
# import dash_design_kit as ddk
# import requests
# import xarray as xr
# import io
# import numpy as np
# import plotly.graph_objects as go
# import dash_leaflet as dl  # Import dash_leaflet
# import dash_bootstrap_components as dbc

# # Register the page with Dash
# dash.register_page(__name__, path_template="/<project>/trajectory_3d")

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
#             dcc.Link('POPS', href=get_relative_path('/pops'))
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

# # Function to load data from URL and convert to xarray Dataset
# def load_data(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         dataset = xr.open_dataset(io.BytesIO(response.content))
#         return dataset
#     except Exception as e:
#         print(f"Error loading data from {url}: {e}")
#         return None

# # Load the data for CDP
# data_url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/acg_tillamook2022_fvr-55_cloudysky_1s.nc"
# df = load_data(data_url)

# # Get unique flight IDs
# if df is not None:
#     unique_flights = np.unique(df['trajectory_id'].values)
# else:
#     unique_flights = []

# # Get the column names for the dataset to use in the dropdown, excluding 'trajectory_id'
# if df is not None:
#     columns = [col for col in df.data_vars.keys() if col != 'trajectory_id']
# else:
#     columns = []

# # Define the layout using Dash Design Kit
# def layout(project="unknown", **kwargs):
#     return ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False),
#             ddk.Block([
#                 # ddk.Card(f"3D Trajectory of 1D Data ({project})"),
#                 ddk.Row([
#                     ddk.Card(width=1, children=[
#                         dcc.Dropdown(
#                             id='flight-dropdown-2',
#                             options=[{'label': flight, 'value': flight} for flight in unique_flights],
#                             placeholder='Select a flight',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ]),
#                     ddk.Card(width=30, children=[
#                         dcc.Dropdown(
#                             id='color-dropdown-2',
#                             options=[{'label': col, 'value': col} for col in columns],
#                             value='cdp_intN',
#                             clearable=False,
#                             style={'width': '100%', 'margin-bottom': '10px'}
#                         )
#                     ])
#                 ]),
#                 ddk.Row([
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='trajectory-graph-2')),
#                             dbc.Button("Expand", id="open-modal-trajectory", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'margin-bottom': 0}),
#                         ddk.Card([
#                             html.B("3D Trajectory Plot"), html.Br(), html.Br(), "Select a flight and variable to view the drone's flight trajectory with concentration levels.", html.Br(),html.Br(), "See the built-in toolbar for options: Download png of plot, zoom in/out, multiple rotation options, and camera reset.",
#                             html.Br(),html.Br(),html.Br(),
#                             html.B("2D Companion Plots"), html.Br(),html.Br(), "These plots will be populated with the data from the flight selected. These show side views of the flight trajectory with the same color concentration levels.",
#                             html.Br(),html.Br(),html.Br(),
#                             html.B("Map Topview"), html.Br(),html.Br(), "This map shows the top view of the flight trajectory over a map for context. Zoom in and move around the map to see where the drone flew."
#                         ], style={'width': '96%'}),
#                     ]),
#                     ddk.Block([
#                         ddk.Card([
#                             dcc.Loading(dcc.Graph(id='longitude-altitude-plot-2')),
#                             html.Br(),
#                             dcc.Loading(dcc.Graph(id='latitude-altitude-plot-2')),
#                             dbc.Button("Expand", id="open-modal-sideplots", n_clicks=0, color="primary", className="mt-2")
#                         ], style={'height': 998})
#                     ])
#                 ]),
#                 # Define modals
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Trajectory Graph"),
#                     dbc.ModalBody(dcc.Graph(id='trajectory-graph-modal')),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-trajectory", className="ml-auto")
#                     ),
#                 ], id="modal-trajectory", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Map"),
#                     dbc.ModalBody(dl.Map(
#                         center=[45.4551, -123.8428],  # Default center (Tillamook, OR)
#                         zoom=12,
#                         children=[
#                             dl.TileLayer(
#                                 url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                 attribution="© CartoDB"
#                             ),
#                             dl.LayerGroup(id="flight-path-layer-modal"),
#                         ],
#                         style={'width': '100%', 'height': '80vh'}
#                     )),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-map", className="ml-auto")
#                     ),
#                 ], id="modal-map", size="xl", is_open=False),
                
#                 dbc.Modal([
#                     dbc.ModalHeader("Expanded Side Plots"),
#                     dbc.ModalBody(html.Div([
#                         dcc.Graph(id='longitude-altitude-plot-modal'),
#                         html.Br(),
#                         dcc.Graph(id='latitude-altitude-plot-modal')
#                     ])),
#                     dbc.ModalFooter(
#                         dbc.Button("Close", id="close-modal-sideplots", className="ml-auto")
#                     ),
#                 ], id="modal-sideplots", size="xl", is_open=False),
#                 ddk.Card([
#                     dcc.Loading(dl.Map(
#                         center=[45.4470, -123.8428],  # Default center (Tillamook, OR)
#                         zoom=12,
#                         children=[
#                             dl.TileLayer(
#                                 url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                 attribution="© CartoDB"
#                             ),
#                             dl.LayerGroup(id="flight-path-layer"),
#                         ], style={'width': '100%', 'height': '400px'}
#                     )),
#                     dbc.Button("Expand", id="open-modal-map", n_clicks=0, color="primary", className="mt-2")
#                 ])
#             ])
#         ]),
#         # ddk.Card([
#         #         dcc.Loading(dl.Map(
#         #             center=[45.4470, -123.8428],  # Default center (Tillamook, OR)
#         #             zoom=12,
#         #             children=[
#         #                 dl.TileLayer(
#         #                     url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#         #                     attribution="© CartoDB"
#         #                 ),
#         #                 dl.LayerGroup(id="flight-path-layer"),
#         #             ], style={'width': '100%', 'height': '400px'}
#         #         )),
#         #         dbc.Button("Expand", id="open-modal-map", n_clicks=0, color="primary", className="mt-2")
#         #     ])
#     ])

# # Define callbacks to handle the modals
# @callback(
#     Output("modal-trajectory", "is_open"),
#     Output("trajectory-graph-modal", "figure"),
#     Input("open-modal-trajectory", "n_clicks"),
#     Input("close-modal-trajectory", "n_clicks"),
#     State("modal-trajectory", "is_open"),
#     State("trajectory-graph-2", "figure")
# )
# def toggle_modal_trajectory(n1, n2, is_open, figure):
#     if n1 or n2:
#         return not is_open, figure
#     return is_open, figure

# @callback(
#     Output("modal-map", "is_open"),
#     Output("flight-path-layer-modal", "children"),
#     Input("open-modal-map", "n_clicks"),
#     Input("close-modal-map", "n_clicks"),
#     State("modal-map", "is_open"),
#     State("flight-path-layer", "children")
# )
# def toggle_modal_map(n1, n2, is_open, flight_path):
#     if n1 or n2:
#         return not is_open, flight_path
#     return is_open, flight_path

# @callback(
#     Output("modal-sideplots", "is_open"),
#     Output("longitude-altitude-plot-modal", "figure"),
#     Output("latitude-altitude-plot-modal", "figure"),
#     Input("open-modal-sideplots", "n_clicks"),
#     Input("close-modal-sideplots", "n_clicks"),
#     State("modal-sideplots", "is_open"),
#     State("longitude-altitude-plot-2", "figure"),
#     State("latitude-altitude-plot-2", "figure")
# )
# def toggle_modal_sideplots(n1, n2, is_open, long_fig, lat_fig):
#     if n1 or n2:
#         return not is_open, long_fig, lat_fig
#     return is_open, long_fig, lat_fig

# # Define callback to update trajectory information based on flight and color variable selection
# @callback(
#     Output('trajectory-graph-2', 'figure'),
#     Output('longitude-altitude-plot-2', 'figure'),
#     Output('latitude-altitude-plot-2', 'figure'),
#     Output('flight-path-layer', 'children'),  # Add output for the map layer
#     Input('flight-dropdown-2', 'value'),
#     Input('color-dropdown-2', 'value')
# )
# def update_trajectory_info_2(selected_flight, color_var):
#     if selected_flight is None or color_var is None:
#         return go.Figure(), go.Figure(), go.Figure(), []

#     if df is None:
#         return dash.no_update, dash.no_update, dash.no_update, dash.no_update

#     selected_data = df.where(df.trajectory_id == selected_flight, drop=True)

#     x = selected_data['longitude'].values
#     y = selected_data['latitude'].values
#     z = selected_data['altitude'].values
#     color = selected_data[color_var].values

#     # Extract the last two digits of the selected flight
#     flight_suffix = str(selected_flight)[-2:]

#     # Create 3D scatter plot
#     fig_3d = go.Figure(data=[go.Scatter3d(
#         x=x,
#         y=y,
#         z=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,  # set color to selected variable values
#             colorscale='Viridis',  # choose a colorscale
#             opacity=0.8,
#             colorbar=dict(
#                 title=color_var
#             )
#         )
#     )])
#     fig_3d.update_layout(
#         title=f'3D Trajectory for Flight {flight_suffix}',
#         scene=dict(
#             xaxis_title='Longitude',
#             yaxis_title='Latitude',
#             zaxis_title='Altitude'
#         ),
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Longitude vs Altitude
#     fig_long_alt = go.Figure(data=[go.Scatter(
#         x=x,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_long_alt.update_layout(
#         title=f'Sideview: Longitude Flight {flight_suffix}',
#         xaxis_title='Longitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Create 2D scatter plot: Latitude vs Altitude
#     fig_lat_alt = go.Figure(data=[go.Scatter(
#         x=y,
#         y=z,
#         mode='markers',
#         marker=dict(
#             size=4,
#             color=color,
#             colorscale='Viridis',
#             opacity=0.8
#         )
#     )])
#     fig_lat_alt.update_layout(
#         title=f'Sideview: Latitude Flight {flight_suffix}',
#         xaxis_title='Latitude',
#         yaxis_title='Altitude',
#         margin=dict(l=50, r=50, t=80, b=50)
#     )

#     # Update the map with the flight path
#     flight_path = dl.Polyline(positions=list(zip(y, x)), color="darkblue", weight=2)

#     return fig_3d, fig_long_alt, fig_lat_alt, [flight_path]

# #############################################################################################
# ###   End of 3D, Two companions stacked, top view map, pop up full, text in, map below    ###
# #############################################################################################