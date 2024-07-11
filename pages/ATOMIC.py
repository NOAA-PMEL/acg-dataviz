from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='ATOMIC Project',
    top_nav=True,
    path='/ATOMIC'
)

def layout():
    return html.Div([
        html.H1("ATOMIC Data Here.")
    ])
    