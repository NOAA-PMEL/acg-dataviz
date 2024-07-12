from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='MSEMS Tillamook',
    top_nav=True,
    path='/msems'
)

def layout():
    return html.Div([
        html.H1("MSEMS Data Here.")
    ])
    