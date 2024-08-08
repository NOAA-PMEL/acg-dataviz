# import dash
# from dash import Dash, html, dcc, callback, Output, Input
# # import numpy
# import pandas as pd
# import plotly.express as px
# import dash_design_kit as ddk

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')
# dash.register_page(__name__, path="/")
# # app = Dash(__name__, use_pages=True)
# # server = app.server  # expose server variable for Procfile

# # app.layout = [
# layout = ddk.App(show_editor=True, children=[
#     # html.H1(children='ACG DataViz!', style={'textAlign':'center'}),
#     ddk.Header(ddk.Title('ACG DataViz!')),
#     ddk.ControlCard([
#     ddk.ControlItem(dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection')),
#     ddk.Graph(id='graph-content')
#     ])
# ])






# from dash import html, register_page  #, callback # If you need callbacks, import it here.
# import dash_design_kit as ddk

# register_page(
#     __name__,
#     name='home',
#     top_nav=True,
#     path='/home'
# )

# # def layout():
# #     return html.Div([
# #         html.H1("home Data Here.")
# #     ])
    

# layout = ddk.App([
#     ddk.Card("Welcome to ACG-DataViz!"),
#     # ddk.Row([
#     #     # ddk.Sidebar([
#     #     #     menu
#     #     # ], foldable=False, style={'background-color': '#add8e6'}),
#     #     # ddk.Card([
#     #     #     dash.page_container
#     #     # ], width=100)  # Set the width to 100 to take the remaining space next to the sidebar
#     # ]),
# ])




# from dash import html, register_page
# import dash_design_kit as ddk
# from PIL import Image
# from IPython.display import display

# register_page(
#     __name__,
#     name='home',
#     top_nav=True,
#     path='/'
# )

# img = Image.open('assets/drone.jpg')

# layout = ddk.Block([
#     ddk.Card("Welcome to ACG-DataViz!"),
#     ddk.Block(
#         display(img)
#         # html.Img(src='/assets/stupidgrapefruit.jpg.', style={'width': '100%', 'height': 'auto'})
#         # html.Img(src=get_asset_url('/assets/drone.jpg'))
#     )
# ])







# from dash import html, register_page
# import dash_design_kit as ddk
# from dash import dcc
# import dash


# register_page(
#     __name__,
#     name='home',
#     top_nav=True,
#     path='/'
# )


# layout = ddk.Block([
#     ddk.Card("Welcome to ACG-DataViz!"),
#     ddk.Block([
#         # html.Img(src=dash.get_asset_url('drone.jpg'), style={'width': '50%', 'height': 'auto'}),
#         # html.Img(src=dash.get_asset_url('hothDrone.jpg'), style={'width': '50%', 'height': 'auto'}),
#         # html.Img(src=dash.get_asset_url('littleBoat.jpg'), style={'width': '50%', 'height': 'auto'}),
#         html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '50%', 'height': 'auto'})
#     ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'padding': '30px'}),
# ])





























# #nice map

# from dash import Dash, html, dcc, register_page
# import dash_design_kit as ddk
# import dash_leaflet as dl
# import dash


# # Register the pages
# register_page(
#     __name__,
#     name='home',
#     top_nav=True,
#     path='/'
# )


# # Define the layout with the map and links
# layout = ddk.Block([
#     ddk.Card("Welcome to ACG-DataViz!"),
#     # ddk.Block([
#     #     html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '50%', 'height': 'auto'})
#     # ], style={'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'padding': '30px'}),
#     ddk.Block([
#         dl.Map(center=[47.6906, -122.2837], zoom=3, children=[          
#         dl.TileLayer(
#             url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#             attribution="© CartoDB"
#         ),

#             dl.Marker(position=[47.6906, -122.2837], children=[
#                     dl.Tooltip("Sandpoint, Seattle, WA"),
#                     dl.Popup([
#                         dcc.Link('Go to Sandpoint', href='/sandpoint')
#                     ])
#                 ]),
#                 dl.Marker(position=[35.2741, -120.6814], children=[
#                     dl.Tooltip("2328 Banderola Ct, San Luis Obispo, CA"),
#                     dl.Popup([
#                         dcc.Link('Go to San Luis Obispo', href='/san_luis_obispo')
#                     ])
#                 ]),
#                 dl.Marker(position=[45.4551, -123.8428], children=[
#                     dl.Tooltip("Tillamook, OR"),
#                     dl.Popup([
#                         dcc.Link('Go to Tillamook', href=dash.get_relative_path('/Tillamook2022'))
#                     ])
#                 ])
#         ], style={'width': '100%', 'height': '400px'})
#     ])
# ])


















from dash import Dash, html, dcc, register_page, get_relative_path
import dash_design_kit as ddk
import dash_leaflet as dl
import dash

# Register the pages
register_page(
    __name__,
    name='home',
    top_nav=True,
    path='/'
)

menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='Tillamook 2022',
        default_open=False,
        children=[
            dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
            dcc.Link('Property/Property Plots', href=get_relative_path('/propPropPlot')),
            # dcc.Link('test page', href=get_relative_path('/test')),
        ]
    ),
    ddk.CollapsibleMenu(
        title='Vandenberg 2023',
        default_open=False,
        children=[
            dcc.Link('CDP', href=get_relative_path('/cdp')),
            dcc.Link('MSEMS', href=get_relative_path('/msems')),
            dcc.Link('POPS', href=get_relative_path('/pops'))
        ]
    ),
    ddk.CollapsibleMenu(
        title='ATOMIC',
        default_open=False,
        children=[
            dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/trajectory_3d')),
            # dcc.Link('Trajectory Plot', href=get_relative_path('/Tillamook2023/option2'))
        ]
    ),
])









def layout(project="unknown", **kwargs):
    layout = ddk.Block([
        ddk.Row([
            ddk.Sidebar([
                menu
            ], foldable=False), 
            ddk.Block([
                ddk.Card("Welcome to ACG-DataViz!"),
                ddk.Row([
                    ddk.Block([
                        dl.Map(
                            center=[52.5, -115.6298],
                            zoom=3,
                            children=[
                                dl.TileLayer(
                                    url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
                                    attribution="© CartoDB"
                                ),
                                dl.Marker(position=[47.6906, -122.2837], children=[
                                    dl.Tooltip("Sandpoint, Seattle, WA"),
                                    dl.Popup([
                                        dcc.Link('Go to Sandpoint', href=dash.get_relative_path('/sandpoint'))
                                    ])
                                ]),
                                dl.Marker(position=[71.2906, -156.7886], children=[
                                    dl.Tooltip("Barrow, AK"),
                                    dl.Popup([
                                        dcc.Link('Go to Barrow', href=dash.get_relative_path('/Barrow'))
                                    ])
                                ]),
                                dl.Marker(position=[35.2741, -120.6814], children=[
                                    dl.Tooltip("2328 Banderola Ct, San Luis Obispo, CA"),
                                    dl.Popup([
                                        dcc.Link('Go to San Luis Obispo', href=dash.get_relative_path('/san_luis_obispo'))
                                    ])
                                ]),
                                dl.Marker(position=[45.4551, -123.8428], children=[
                                    dl.Tooltip("Tillamook, OR"),
                                    dl.Popup([
                                        dcc.Link('Go to Tillamook', href=dash.get_relative_path('/Tillamook2022'))
                                    ])
                                ]),
                                dl.Marker(position=[34.7324, -120.5724], children=[
                                    dl.Tooltip("Vandenberg, Lompoc, CA"),
                                    dl.Popup([
                                        dcc.Link('Go to Vandenberg', href=dash.get_relative_path('/Vandenberg2023'))
                                    ])
                                ])
                            ],
                            style={'width': '100%', 'height': '600px'}
                        )


                    ], style={'width': '50%', 'height': '580px', 'border': '1px solid #ccc', 'border-radius': '10px'}),
                    ddk.Block([
                        html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), className='responsive-image', style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
                        html.Img(src=dash.get_asset_url('hothDrone.jpg'), className='responsive-image', style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
                        html.Img(src=dash.get_asset_url('littleBoat.jpg'), className='responsive-image', style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
                    ], style={'width': '20%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'padding': '7px'})
                ], style={'display': 'flex'})
            ])
        ])
    ])
    return layout








# Define the layout with the map and image
# def layout(project="unknown", **kwargs):
#     layout = ddk.Block([
#         ddk.Row([
#             ddk.Sidebar([
#                 menu
#             ], foldable=False), # style={'background-color': '#add8e6'}
#             ddk.Block([
#                 ddk.Card("Welcome to ACG-DataViz!"),
#                 ddk.Row([
#                     ddk.Block([
#                         dl.Map(
#                             center=[41.8781, -96.6298],
#                             zoom=4,
#                             children=[          
#                                 dl.TileLayer(
#                                     url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png",
#                                     attribution="© CartoDB"
#                                 ),
#                                 dl.Marker(position=[47.6906, -122.2837], children=[
#                                     dl.Tooltip("Sandpoint, Seattle, WA"),
#                                     dl.Popup([
#                                         dcc.Link('Go to Sandpoint', href='/sandpoint')
#                                     ])
#                                 ]),
#                                 dl.Marker(position=[35.2741, -120.6814], children=[
#                                     dl.Tooltip("2328 Banderola Ct, San Luis Obispo, CA"),
#                                     dl.Popup([
#                                         dcc.Link('Go to San Luis Obispo', href='/san_luis_obispo')
#                                     ])
#                                 ]),
#                                 dl.Marker(position=[45.4551, -123.8428], children=[
#                                     dl.Tooltip("Tillamook, OR"),
#                                     dl.Popup([
#                                         dcc.Link('Go to Tillamook', href=dash.get_relative_path('/Tillamook2022'))
#                                     ])
#                                 ]),
#                                 dl.Marker(position=[34.7324, -120.5724], children=[
#                                     dl.Tooltip("Vandenberg, Lompoc, CA"),
#                                     dl.Popup([
#                                         dcc.Link('Go to Vandenberg', href=dash.get_relative_path('/Vandenberg2023'))
#                                     ])
#                                 ])
#                             ],
#                             style={'width': '100%', 'height': '600px'}
#                         )
#                     ], style={'width': '50%', 'height': '580px', 'border': '1px solid #ccc', 'border-radius': '10px'}),
#                     ddk.Block([
#                         html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
#                         html.Img(src=dash.get_asset_url('hothDrone.jpg'), style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
#                         html.Img(src=dash.get_asset_url('littleBoat.jpg'), style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
#                         # html.Img(src=dash.get_asset_url('drone.jpg'), style={'width': '75%', 'height': 'auto', 'margin-bottom': '7px'}),
#                     ], style={'width': '20%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'padding': '7px'})
#                 ], style={'display': 'flex'})
#             ])
#         ])
#     ])
#     return layout




























