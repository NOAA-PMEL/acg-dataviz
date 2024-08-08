# import dash
# from dash import html, register_page, dcc, get_relative_path
# import dash_design_kit as ddk

# register_page(
#     __name__,
#     name='PMEL Barrow Atmospheric Baseline Observatory Data',
#     top_nav=True,
#     path='/barrow'
# )

# # Uncomment the menu if you want to add it to the sidebar
# # menu = ddk.Menu([
# #     ddk.CollapsibleMenu(
# #         title='1D Data Visualization',
# #         default_open=False,
# #         children=[
# #             dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
# #             dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
# #         ]
# #     ),
# #     ddk.CollapsibleMenu(
# #         title='2D Data Visualization',
# #         default_open=False,
# #         children=[
# #             dcc.Link('CDP', href=get_relative_path('/cdp')),
# #             dcc.Link('MSEMS', href=get_relative_path('/msems')),
# #             dcc.Link('POPS', href=get_relative_path('/pops'))
# #         ]
# #     ),
# #     ddk.CollapsibleMenu(
# #         title='3D Data Visualization',
# #         default_open=False,
# #         children=[
# #             dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/trajectory_3d')),
# #         ]
# #     ),
# # ])

# def layout(project="unknown", **kwargs): 
#     layout = ddk.Block([
#         ddk.Card("Barrow Data Here."),
#         ddk.Row([
#             ddk.Sidebar([
#                 # menu
#             ], foldable=False, className='sidebar-hidden'),
#             ddk.Block([
#                 ddk.Row([
#                     html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '100%', 'height': 'auto'}),
#                 ]),
#                 ddk.Row([
#                     ddk.Card([
#                         "Information about project. Information about project. Information about project."
#                     ])
#                 ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'})
#             ]),
#         ]),
#     ])
#     return layout




























# import dash
# from dash import html, register_page, dcc, get_relative_path
# import dash_design_kit as ddk

# register_page(
#     __name__,
#     name='PMEL Barrow Atmospheric Baseline Observatory Data',
#     top_nav=True,
#     path='/Barrow'
# )

# def layout(project="unknown", **kwargs): 
#     layout = ddk.Block([
#         ddk.Card("Barrow Data Here."),
#         ddk.Row([
#             ddk.Sidebar([
#                 # menu
#             ], foldable=False, className='sidebar-hidden'),
#             ddk.Block([
#                 ddk.Row([
#                     html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '100%', 'height': 'auto'}),
#                 ]),
#                 ddk.Row([
#                     ddk.Card([
#                         "Information about project. Information about project. Information about project."
#                     ])
#                 ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'})
#             ]),
#         ]),
#     ])
#     return layout















# import dash
# from dash import html, register_page, dcc, get_relative_path, dash_table
# import dash_design_kit as ddk
# import xarray as xr
# import pandas as pd
# import requests
# import io

# from UAS_Functions import say_hello

# register_page(
#     __name__,
#     name='PMEL Barrow Atmospheric Baseline Observatory Data',
#     top_nav=True,
#     path='/Barrow'
# )

# # Load the dataset from the URL
# def load_dataset():
#     url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/station_barrow_submicron_chemistry.nc"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         ds = xr.open_dataset(io.BytesIO(response.content))
#         df = ds.to_dataframe().reset_index()  # Convert xarray dataset to pandas DataFrame
#         return df
#     except Exception as e:
#         print(f"Error loading data: {e}")
#         return pd.DataFrame()

# # Load the data and select specific columns
# columns_to_include = [
#     'volume',
#     'mass_sub1_conc',
#     'IC_Na_sub1_conc',
#     'IC_NH4_sub1_conc',
#     'IC_K_sub1_conc',
#     'IC_Mg_sub1_conc',
#     'IC_Ca_sub1_conc',
#     'IC_MSA_sub1_conc',
#     'IC_Cl_sub1_conc',
#     'IC_Br_sub1_conc',
#     'IC_NO3_sub1_conc',
#     'IC_total_SO4_sub1_conc',
#     'IC_Oxalate_sub1_conc'
# ]

# data_df = load_dataset()[columns_to_include]

# def layout(project="unknown", **kwargs): 
#     layout = ddk.Block([
#         ddk.Card(f"Barrow Data Here. {say_hello()}"),
#         ddk.Row([
#             ddk.Sidebar([
#                 # menu
#             ], foldable=False, className='sidebar-hidden'),
#             ddk.Block([
#                 ddk.Row([
#                     html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '100%', 'height': 'auto'}),
#                 ]),
#                 ddk.Row([
#                     ddk.Card([
#                         "Information about project. Information about project. Information about project."
#                     ]),
#                 ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'}),
#                 ddk.Row([
#                     ddk.Card([
#                         dash_table.DataTable(
#                             data=data_df.to_dict('records'),
#                             columns=[{"name": i, "id": i} for i in data_df.columns],
#                             page_size=10,  # Adjust the number of rows displayed
#                         )
#                     ])
#                 ])
#             ]),
#         ]),
#     ])
#     return layout


























import dash
from dash import html, register_page, dcc, get_relative_path, dash_table
import dash_design_kit as ddk
import xarray as xr
import pandas as pd
import requests
import io
import plotly.express as px
from dash.dependencies import Input, Output

from UAS_Functions import say_hello

register_page(
    __name__,
    name='PMEL Barrow Atmospheric Baseline Observatory Data',
    top_nav=True,
    path='/Barrow'
)

# Load the dataset from the URL
def load_dataset():
    url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/station_barrow_submicron_chemistry.nc"
    try:
        response = requests.get(url)
        response.raise_for_status()
        ds = xr.open_dataset(io.BytesIO(response.content))
        df = ds.to_dataframe().reset_index()  # Convert xarray dataset to pandas DataFrame
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

# Load the data and select specific columns
columns_to_include = [
    'time',    
    'volume',
    'mass_sub1_conc',
    'IC_Na_sub1_conc',
    'IC_NH4_sub1_conc',
    'IC_K_sub1_conc',
    'IC_Mg_sub1_conc',
    'IC_Ca_sub1_conc',
    'IC_MSA_sub1_conc',
    'IC_Cl_sub1_conc',
    'IC_Br_sub1_conc',
    'IC_NO3_sub1_conc',
    'IC_total_SO4_sub1_conc',
    'IC_Oxalate_sub1_conc'
]

data_df = load_dataset()[columns_to_include]

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

def layout(project="unknown", **kwargs): 
    layout = ddk.Block([
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False, className='sidebar-hidden'),

            ddk.Block([
                ddk.Card(f"Barrow Data Here. {say_hello()}"),
                
                ddk.Row([
                    ddk.Card([
                        dcc.Dropdown(
                            id='y-axis-dropdown',
                            options=[{'label': col, 'value': col} for col in data_df.columns if col != 'time'],
                            value='mass_sub1_conc',  # Default value
                            clearable=False,
                            style={'width': '100%'}
                        ),
                    ]),
                    ddk.Card([
                        dcc.Dropdown(
                            id='color-axis-dropdown',
                            options=[{'label': col, 'value': col} for col in data_df.columns if col != 'time'],
                            value='volume',  # Default color variable
                            clearable=False,
                            style={'width': '100%'} 
                        ),
                    ])
                ]),
                ddk.Card([
                    dcc.Graph(id='scatter-plot', style={'height': '400px'})
                ]),
                ddk.Card([
                    dcc.RangeSlider(
                        id='color-range-slider',
                        min=data_df['volume'].min(),
                        max=data_df['volume'].max(),
                        value=[data_df['volume'].min(), data_df['volume'].max()],
                        marks={str(i): str(i) for i in range(int(data_df['volume'].min()), int(data_df['volume'].max()) + 1, 10)},
                        step=0.1
                    )
                ]),
            ]),
        ]),
    ])
    return layout

# Callback to update the scatter plot based on the selected y-axis variable
@dash.callback(
    Output('scatter-plot', 'figure'),
    Input('y-axis-dropdown', 'value'),
    Input('color-axis-dropdown', 'value'),
    Input('color-range-slider', 'value')
)
def update_scatter_plot(y_axis, color_axis, color_range):
    fig = px.scatter(
        data_df,
        x='time',
        y=y_axis,
        color=color_axis,
        color_continuous_scale='viridis',
        range_color=color_range,  # Set the color range based on the slider
        labels={'time': 'Time', y_axis: y_axis, color_axis: color_axis}
    )
    fig.update_layout(transition_duration=500)
    return fig











####################################################################################
######################         attempt at error bars         #######################
####################################################################################


## not working yet. I was not able to get any error bars to show up and I am not
## sure why




# import dash
# from dash import html, register_page, dcc, get_relative_path, dash_table
# import dash_design_kit as ddk
# import xarray as xr
# import pandas as pd
# import requests
# import io
# import plotly.express as px
# from dash.dependencies import Input, Output

# from UAS_Functions import say_hello

# register_page(
#     __name__,
#     name='PMEL Barrow Atmospheric Baseline Observatory Data',
#     top_nav=True,
#     path='/Barrow'
# )

# # Load the dataset from the URL
# def load_dataset():
#     url = "https://data.pmel.noaa.gov/pmel/erddap/tabledap/station_barrow_submicron_chemistry.nc"
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         ds = xr.open_dataset(io.BytesIO(response.content))
#         df = ds.to_dataframe().reset_index()  # Convert xarray dataset to pandas DataFrame
#         return df
#     except Exception as e:
#         print(f"Error loading data: {e}")
#         return pd.DataFrame()

# # Load the data and select specific columns
# columns_to_include = [
#     'time',    
#     'volume',
#     'mass_sub1_conc',
#     'mass_sub1_unc',
#     'IC_Na_sub1_conc',
#     'IC_Na_sub1_unc',
#     'IC_NH4_sub1_conc',
#     'IC_NH4_sub1_unc',
#     'IC_K_sub1_conc',
#     'IC_K_sub1_unc',
#     'IC_Mg_sub1_conc',
#     'IC_Mg_sub1_unc',
#     'IC_Ca_sub1_conc',
#     'IC_Ca_sub1_unc',
#     'IC_MSA_sub1_conc',
#     'IC_MSA_sub1_unc',
#     'IC_Cl_sub1_conc',
#     'IC_Cl_sub1_unc',
#     'IC_Br_sub1_conc',
#     'IC_Br_sub1_unc',
#     'IC_NO3_sub1_conc',
#     'IC_NO3_sub1_unc',
#     'IC_total_SO4_sub1_conc',
#     'IC_total_SO4_sub1_unc',
#     'IC_Oxalate_sub1_conc',
#     'IC_Oxalate_sub1_unc'
# ]

# data_df = load_dataset()[columns_to_include]

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

# def layout(project="unknown", **kwargs): 
#     layout = ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False, className='sidebar-hidden'),

#             ddk.Block([
#                 ddk.Card(f"Barrow Data Here. {say_hello()}"),
                
#                 ddk.Row([
#                     ddk.Card([
#                         dcc.Dropdown(
#                             id='y-axis-dropdown',
#                             options=[{'label': col, 'value': col} for col in data_df.columns if col.endswith('_conc')],
#                             value='mass_sub1_conc',  # Default value
#                             clearable=False,
#                             style={'width': '100%'}
#                         ),
#                     ]),
#                     ddk.Card([
#                         dcc.Dropdown(
#                             id='color-axis-dropdown',
#                             options=[{'label': col, 'value': col} for col in data_df.columns if col != 'time'],
#                             value='volume',  # Default color variable
#                             clearable=False,
#                             style={'width': '100%'} 
#                         ),
#                     ])
#                 ]),
#                 ddk.Card([
#                     dcc.Graph(id='scatter-plot', style={'height': '400px'})
#                 ]),
#                 ddk.Card([
#                     dcc.RangeSlider(
#                         id='color-range-slider',
#                         min=data_df['volume'].min(),
#                         max=data_df['volume'].max(),
#                         value=[data_df['volume'].min(), data_df['volume'].max()],
#                         marks={str(i): str(i) for i in range(int(data_df['volume'].min()), int(data_df['volume'].max()) + 1, 10)},
#                         step=0.1
#                     )
#                 ]),
#             ]),
#         ]),
#     ])
#     return layout

# # Callback to update the scatter plot based on the selected y-axis variable
# @dash.callback(
#     Output('scatter-plot', 'figure'),
#     Input('y-axis-dropdown', 'value'),
#     Input('color-axis-dropdown', 'value'),
#     Input('color-range-slider', 'value')
# )
# def update_scatter_plot(y_axis, color_axis, color_range):
#     # Create a mapping of the y-axis variables to their corresponding uncertainty variables
#     error_bars_mapping = {
#         'mass_sub1_conc': 'mass_sub1_unc',
#         'IC_Na_sub1_conc': 'IC_Na_sub1_unc',
#         'IC_NH4_sub1_conc': 'IC_NH4_sub1_unc',
#         'IC_K_sub1_conc': 'IC_K_sub1_unc',
#         'IC_Mg_sub1_conc': 'IC_Mg_sub1_unc',
#         'IC_Ca_sub1_conc': 'IC_Ca_sub1_unc',
#         'IC_MSA_sub1_conc': 'IC_MSA_sub1_unc',
#         'IC_Cl_sub1_conc': 'IC_Cl_sub1_unc',
#         'IC_Br_sub1_conc': 'IC_Br_sub1_unc',
#         'IC_NO3_sub1_conc': 'IC_NO3_sub1_unc',
#         'IC_total_SO4_sub1_conc': 'IC_total_SO4_sub1_unc',
#         'IC_Oxalate_sub1_conc': 'IC_Oxalate_sub1_unc'
#     }
    
#     # Get the corresponding error variable
#     error_y = error_bars_mapping.get(y_axis, None)

#     # Create the scatter plot with error bars
#     fig = px.scatter(
#         data_df,
#         x='time',
#         y=y_axis,
#         color=color_axis,
#         color_continuous_scale='viridis',
#         range_color=color_range,  # Set the color range based on the slider
#         error_y=error_y,  # Set the error bars for the selected y-axis variable
#         labels={'time': 'Time', y_axis: y_axis, color_axis: color_axis}
#     )
    
#     # Add error values for positive and negative directions
#     fig.update_traces(error_y=dict(type='data', array=data_df[error_y], visible=True), 
#                       error_y_minus=dict(type='data', array=data_df[error_y], visible=True))
    
#     fig.update_layout(transition_duration=500)
#     return fig
