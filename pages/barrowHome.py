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




























import dash
from dash import html, register_page, dcc, get_relative_path
import dash_design_kit as ddk

register_page(
    __name__,
    name='PMEL Barrow Atmospheric Baseline Observatory Data',
    top_nav=True,
    path='/Barrow'
)

def layout(project="unknown", **kwargs): 
    layout = ddk.Block([
        ddk.Card("Barrow Data Here."),
        ddk.Row([
            ddk.Sidebar([
                # menu
            ], foldable=False, className='sidebar-hidden'),
            ddk.Block([
                ddk.Row([
                    html.Img(src=dash.get_asset_url('tatooineSunset.jpg'), style={'width': '100%', 'height': 'auto'}),
                ]),
                ddk.Row([
                    ddk.Card([
                        "Information about project. Information about project. Information about project."
                    ])
                ], style={'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'})
            ]),
        ]),
    ])
    return layout
