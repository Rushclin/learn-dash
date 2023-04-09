from dash import html, dcc
import dash_bootstrap_components as dbc

from layouts.header import Header
from layouts.navbar import Navbar


class Layout:
    def __init__(self):
        print("============= INIT LAYOUT")
        self.header = Header().get_header()
        self.navbar = Navbar().get_navbar()

        self.layout = dbc.Container(
            fluid=True,
            children=[
                self.header,
                html.Hr(),
                self.navbar,
                html.Div(
                    id="app-content",
                    className="mx-5",
                ),
            ],
            id="app-container",
        )

    def get_layout(self):
        return self.layout
