from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='POPS Tillamook',
    top_nav=True,
    path='/pops'
)

def layout():
    return html.Div([
        html.H1("POPS Data Here.")
    ])
    