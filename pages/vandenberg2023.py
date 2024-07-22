import dash
from dash import html, register_page, dcc, get_relative_path
import dash_design_kit as ddk


register_page(
    __name__,
    name='Tillamook2022 UAS Project',
    top_nav=True,
    path='/Vandenberg2023'
)


def layout(project="unknown", **kwargs): 
    layout = ddk.Block([
    ddk.Card("Vandenberg")
    ])
    return layout