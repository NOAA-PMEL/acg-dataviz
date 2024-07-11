import dash
from dash import html, register_page, dcc, get_relative_path
import dash_design_kit as ddk


register_page(
    __name__,
    name='Tillamook Project',
    top_nav=True,
    path='/Tillamook'
)

menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='1D Data Visualization!',
        default_open=False,
        children=[
            dcc.Link('1D Data Plots', href=get_relative_path('/1d_data_plots')),
            # dcc.Link('Property/Property Plots', href=app.get_relative_path('/propPropPlot')),
        ]
    ),
    # ddk.CollapsibleMenu(
    #     title='2D Data Visualization',
    #     default_open=False,
    #     children=[
    #         dcc.Link('CDP', href=app.get_relative_path('/cdp')),
    #         dcc.Link('MSEMS', href=app.get_relative_path('/msems')),
    #         dcc.Link('POPS - not done', href=app.get_relative_path('/pops'))
    #     ]
    # ),
    # ddk.CollapsibleMenu(
    #     title='3D Data Visualization',
    #     default_open=False,
    #     children=[
    #         dcc.Link('Trajectory Plot', href=app.get_relative_path('/trajectory')),
    #     ]
    # ),
])

# def layout():
#     return html.Div([
#         html.H1("Tillamook Data Here.")
#     ])
    
    
# Define the layout using Dash Design Kit
layout = ddk.App([
    ddk.Card("Tillamook Data Here."),
    ddk.Row([
        ddk.Sidebar([
            menu
        ], foldable=False, style={'background-color': '#add8e6'}),
        # ddk.Card([
        #     dash.page_container
        # ], width=100)  # Set the width to 100 to take the remaining space next to the sidebar
    ]),
])