from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='CDP Tillamook',
    top_nav=True,
    path='/cdp'
)

def layout():
    return html.Div([
        html.H1("CDP Data Here.")
    ])
    