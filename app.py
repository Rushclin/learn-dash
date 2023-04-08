import os
import pathlib

from dash import dash, html, Output, Input, State, dcc
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
import dash_daq as daq

import pandas as pd

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.SOLAR],
)
app.title = "Dashboard"


# Composants
def render_header():
    title = html.H4(
        "DASHBOARD",
        style={
            "marginTop": 5,
            "marginLeft": "10px",
        },
        className="text-white",
    )
    sub_title = html.H5(
        "Une petite description.",
        style={"marginLeft": "10px"},
        className="text-white",
    )
    logo_image = html.Img(
        src=app.get_asset_url("dash-logo.png"),
        style={
            "float": "right",
            "height": 50,
            "padding": 10,
        },
        className="mt-3",
    )
    link = html.A(
        logo_image,
        href="https://plotly.com/dash/",
    )

    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row([title]),
                    dbc.Row([sub_title]),
                ]
            ),
            dbc.Col(link),
        ],
        className="my-1",
    )


def render_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custum-tabs",
                children=[
                    dcc.Tab(
                        id="setting_tab",
                        label="PARAMETRAGES DU DASHBOARD",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="control_tab",
                        label="GRAPHES DE CONTRôLE",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            ),
        ],
    )


def rendre_side_bar_graph():
    return html.Div(
        id="",
        children=[
            html.Div(
                [
                    html.P("ID"),
                    daq.LEDDisplay(
                        id="",
                        value="1704",
                        color="#92e0d3",
                        backgroundColor="#1e2130",
                        size=50,
                    ),
                ],
                className="custum_card mb-5",
            ),
            html.Div(
                [
                    html.P("FREQUENCE"),
                    daq.Gauge(
                        id="",
                        max=2,
                        min=0,
                        showCurrentValue=True,
                    ),
                ],
                className="custum_card mb-5",
            ),
            html.Div(
                [
                    daq.StopButton(
                        id="",
                        size=100,
                        n_clicks=0,
                    )
                ],
                id="",
            ),
        ],
        className="bg-dark p-3",
    )


app.layout = dbc.Container(
    fluid=True,
    children=[
        render_header(),
        html.Hr(),
        render_tabs(),
        html.Div(
            id="app-content",
        ),
    ],
    id="app-container",
)


@app.callback(
    [Output("app-content", "children")],
    [Input("app-tabs", "value")],
)
def render_tab_content(tab_switch):
    if tab_switch == "tab1":
        return [
            html.Div(
                [
                    html.H1("Element de la Tabs 1"),
                ],
            )
        ]
    return [
        dbc.Row(
            [
                dbc.Col(
                    [
                        rendre_side_bar_graph(),
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        html.Div(
                            id="graph_container",
                            children=[
                                html.P("Les autres elements ici"),
                            ],
                        ),
                    ],
                    md=9,
                ),
            ],
            id="",
            className="mt-3",
        )
    ]


app.run_server(debug=True, port=8050)
