import dash
from dash import Dash, dcc, html
import dash_design_kit as ddk

app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True,
    meta_tags=[{'name': 'viewport',
        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'
    }]
)
server = app.server  # expose server variable for Procfile
menu = ddk.Menu(
    children=[ddk.CollapsibleMenu(
        title='Projects',
        children=[
            # dcc.Link('joe', href=app.get_relative_path('/joe')),
            # dcc.Link('Tillamook', href='tillamook/trajectory'),
            dcc.Link('Tillamook2022', href='Tillamook2022'),
            dcc.Link('Vandenberg2023', href='Vandenberg2023'),
            dcc.Link('ATOMIC', href='ATOMIC'),
            dcc.Link('Barrow', href='Barrow')
            # dcc.Link('Investment', href='/'),
        ])
    ]
)

app.layout = ddk.App(children=[    #show_editor=True, 
    ddk.Header([
        # ddk.Logo(src=app.get_asset_url('DataViz_logo_stacked_compass_rose.png')),
        # ddk.Logo(src=app.get_asset_url('ACG_orbit.png')),
        # ddk.Logo(src=app.get_asset_url('original_compass_orbit.png')),
        # ddk.Logo(src=app.get_asset_url('compass_rose_horizontal.png')),
        dcc.Link(
            ddk.Logo(src=app.get_asset_url('chosen.png')), #compass_rose_horizontal
            href=app.get_relative_path('/')
        ),
        # dcc.Link(html.Button('Home', style={'margin-left': '20px'}), href=app.get_relative_path('/')),
        # dcc.Link(
        #     ddk.Logo(src=app.get_asset_url('original_compass_orbit.png')),
        #     href=app.get_relative_path('/')
        # ),
        menu,
    ]), # style={'background-color': '#add8e6'}
    
    # ddk.Block([
    #     html.Img(src=app.get_asset_url('drone.jpg'), style={'width': '50%', 'height': 'auto'})
    # ]),


    dash.page_container, # Add page container
    ddk.PageFooter(children=[
        html.Hr(),
        ddk.Block(children=[
            ddk.Block(width=0.2, children=[
                html.Img(src=app.get_asset_url('PMEL_logo.png'), style={'height': '90px', 'margin-left': '20px'})
            ]),
            ddk.Block(width=0.8, children=[
                html.Div(style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'flex-start', 'margin-left': '10px'}, children=[
                    dcc.Link('National Oceanic and Atmospheric Administration',
                             href='https://www.noaa.gov/', style={'font-size': '1em', 'margin-bottom': '5px', 'margin-left': '-250px'}),
                    dcc.Link('Pacific Marine Environmental Laboratory',
                             href='https://www.pmel.noaa.gov/', style={'font-size': '1em', 'margin-bottom': '5px', 'margin-left': '-250px'}),
                    dcc.Link('oar.pmel.webmaster@noaa.gov', href='mailto:oar.pmel.webmaster@noaa.gov', style={'font-size': '1em', 'margin-bottom': '5px', 'margin-left': '-250px'}),
                    html.Div(children=[
                        dcc.Link('DOC |', href='https://www.commerce.gov/', style={'font-size': '1em'}),
                        dcc.Link(' NOAA |', href='https://www.noaa.gov/', style={'font-size': '1em'}),
                        dcc.Link(' OAR |', href='https://www.research.noaa.gov/', style={'font-size': '1em'}),
                        dcc.Link(' PMEL |', href='https://www.pmel.noaa.gov/', style={'font-size': '1em'}),
                        dcc.Link(' Privacy Policy |', href='https://www.noaa.gov/disclaimer', style={'font-size': '1em'}),
                        dcc.Link(' Disclaimer |', href='https://www.noaa.gov/disclaimer', style={'font-size': '1em'}),
                        dcc.Link(' Accessibility', href='https://www.pmel.noaa.gov/accessibility', style={'font-size': '1em'})
                    ], style={'margin-left': '-250px'})
                ])
            ])
        ])
    ], style={'padding': '10px'})
])

# dash.page_registry.values

if __name__ == '__main__':
    app.run(debug=True)
