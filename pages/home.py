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




from dash import html, register_page
import dash_design_kit as ddk


register_page(
    __name__,
    name='home',
    top_nav=True,
    path='/'
)


layout = ddk.Block([
    ddk.Card("Welcome to ACG-DataViz!"),
    ddk.Block(
        html.Img(src='/assets/drone.jpg', style={'width': '100%', 'height': 'auto'})
    )
])
