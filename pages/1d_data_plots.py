from dash import html, register_page  #, callback # If you need callbacks, import it here.

register_page(
    __name__,
    name='1D Data Tillamook',
    top_nav=True,
    path='/1d_data_plots'
)

def layout():
    return html.Div([
        html.H1("1D Data Here.")
    ])
    