import dash_bootstrap_components as dbc
from dash import html, dcc


class Layout():
    def __init__(self):
        self.layout = dbc.Container(
            fluid=True,
            children=[
                html.H1(
                    'Un petit chronometre avec des composants de type class', className='fw-light fs-4 text-center my-5',),
                html.Hr(),
                html.Div(
                    id="app-content",
                    className="mx-auto",
                    children=[
                        html.Div(id='timer', className='text-center mt-3',)
                    ]
                ),
                dcc.Interval(
                    id='interval-component',
                    interval=1*1000,
                    n_intervals=0
                )
            ]
        )

    def render(self):
        return self.layout
