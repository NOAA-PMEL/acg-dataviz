# import dash
# from dash import html, register_page, dcc, get_relative_path
# import dash_design_kit as ddk


# register_page(
#     __name__,
#     name='Tillamook2022 UAS Project',
#     top_nav=True,
#     path='/Tillamook2022'
# )

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

# # def layout():
# #     return html.Div([
# #         html.H1("Tillamook Data Here.")
# #     ])
    
    
# # Define the layout using Dash Design Kit
# layout = ddk.Block([
#     ddk.Card("Tillamook Data Here."),
#     ddk.Row([
#         ddk.Sidebar([
#             menu
#         ], foldable=False), # style={'background-color': '#add8e6'}
#         # ddk.Card([
#         #     dash.page_container
#         # ], width=100)  # Set the width to 100 to take the remaining space next to the sidebar
#         ddk.Block([
#             ddk.Row([
#                 html.Img(src=dash.get_asset_url('tillamook_landing_img.jpg'), style={'width': '65%', 'height': 'auto'}),
#                 ddk.Card([
#                     "Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context."
#                 ])
#             ]),
#             # html.Img(src=dash.get_asset_url('derek_3.jpg'), style={'width': 'auto', 'height': '15%', 'padding': '10px'}),
#             ddk.Row([
#                 html.Img(src=dash.get_asset_url('derek_3.jpg'), style={'width': 'auto', 'height': '15%', 'padding': '10px'}),
#                 html.Img(src=dash.get_asset_url('workshop_drone2.jpg'), style={'width': 'auto', 'height': '15%', 'padding': '10px'})
#             ]),
#         ]),
#     ]),
#     # ddk.Block([
#     #         html.Img(src=dash.get_asset_url('Tillamook_drone.jpg'), style={'width': '100%', 'height': 'auto'})
#     # ], style={'width': '20%', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center', 'padding': '30px'})
# ])





















import dash
from dash import html, register_page, dcc, get_relative_path
import dash_design_kit as ddk


register_page(
    __name__,
    name='Tillamook2022 UAS Project',
    top_nav=True,
    path='/Tillamook2022'
)


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
            dcc.Link('POPS - not done', href=get_relative_path('/pops'))
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


layout = ddk.Block([
    ddk.Card("Tillamook Data Here."),
    ddk.Row([
        ddk.Sidebar([
            menu
        ], foldable=False),
        ddk.Block([
            ddk.Row([
                html.Img(src=dash.get_asset_url('tillamook_landing_img.jpg'), style={'width': '65%', 'height': 'auto'}),
                ddk.Card([
                    "Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context.",
                    # "Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context.",
                    # "Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context."
                ])
            ]),
            ddk.Row([
                html.Img(src=dash.get_asset_url('Tillamook_drone.jpg'), style={'width': 'auto', 'height': '256px', 'margin': '10px 0px'}),
                html.Img(src=dash.get_asset_url('derek_3.jpg'), style={'width': 'auto', 'height': '256px', 'margin': '10px 0px'}),
                html.Img(src=dash.get_asset_url('workshop_drone2.jpg'), style={'width': 'auto', 'height': '256px', 'margin': '10px 0px'}),
                ddk.Card([
                    "Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context. Summary of project, some information, cool facts, things like that. Context."
                ])
            ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'})
        ]),
    ]),
])




