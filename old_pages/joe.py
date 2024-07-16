from dash import html, dcc, callback, Output, Input, no_update
import dash

dash.register_page(__name__)

layout = [html.Div(id='joe',children='joe'), dcc.Dropdown(id='dd', options=[{'label':'bill', 'value':'bill'}, {'label':'jim', 'value':'jim'}])]

@callback(
    Output('joe', 'children'),
    Input('dd', 'value')
)
def rename(in_name):
    if in_name is not None and len(in_name) > 0:
        return [in_name]
    else:
        return no_update