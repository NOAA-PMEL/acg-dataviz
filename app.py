# import dash
# from dash import Dash, html, dcc, callback, Output, Input
# # import numpy
# import pandas as pd
# import plotly.express as px
# import dash_design_kit as ddk

# df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

# app = Dash(__name__, use_pages=True)
# server = app.server  # expose server variable for Procfile

# # test

# # app.layout = [
# #     html.H1(children='ACG DataViz!', style={'textAlign':'center'}),
# #     dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection'),
# #     dcc.Graph(id='graph-content')
# # ]

# # app.layout = html.Div([dcc.Location(id="url"), dash.page_container])
# app.layout = ddk.App(show_editor=True, children=[html.Div([
#     # html.H1('Multi-page app with Dash Pages'),
#     ddk.Header([
#         # ddk.Logo(src=app.get_asset_url('dash-sample-enterprise-logo.png')),
#         ddk.Title('Multi-page app with Dash Pages'),
#     ]),
#     html.Div([
#         html.Div(
#             dcc.Link(f"{page['name']} - {page['path']}", href=page["relative_path"])
#         ) for page in dash.page_registry.values()
#     ]),
#     dash.page_container
# ])])

# @callback(
#     Output('graph-content', 'figure'),
#     Input('dropdown-selection', 'value')
# )
# def update_graph(value):
#     dff = df[df.country==value]
#     return px.line(dff, x='year', y='pop')

# if __name__ == '__main__':
#     # app.run(debug=True)
#     app.run_server(debug=True)





import dash
from dash import Dash, dcc, html
import dash_design_kit as ddk
import plotly.express as px


app = Dash(__name__, title="NewLayoutTry", use_pages=True, pages_folder="pages")
server = app.server  # expose server variable for Procfile


menu = ddk.Menu([
    ddk.CollapsibleMenu(
        title='Choose Project',
        default_open=False,
        children=[
            dcc.Link('Tillamook', href=app.get_relative_path('/Tillamook')),
            dcc.Link('ATOMIC', href=app.get_relative_path('/ATOMIC'))
        ]
    ),
])


app.layout = ddk.App([
    dcc.Location(id='_pages_location'),  # Add Location component
    ddk.Header([
        ddk.Logo(src=app.get_asset_url('PMEL_logo.png')),
        ddk.Title('DataViz'),
        dcc.Link(html.Button('Home', style={'margin-left': '20px'}), href=app.get_relative_path('/home')),
        menu
    ], style={'background-color': '#add8e6'}),
    dcc.Store(id='_pages_store'),  # Add Store component for internal state management
    ddk.Block(id='_pages_content', children=dash.page_container)  # Add page container
])

if __name__ == '__main__':
    app.run(debug=True)
