import pickle
from datetime import datetime

import dash_bootstrap_components as dbc
import dash_daq as daq
import pandas as pd
import plotly.graph_objects as go
from dash import Input, Output, dash, dcc, html, State, dash_table

app = dash.Dash(
    title="Dashboard",
)


suffix_row = "_row"
suffix_button_id = "_button"
suffix_sparkline_graph = "_sparkline_graph"
suffix_count = "_count"
suffix_ooc_n = "_OOC_number"
suffix_ooc_g = "_OOC_graph"
suffix_indicator = "_indicator"

# Definition des composants


def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H5("Manufacturation."),
                    html.H6("Processus de control."),
                ],
            ),
            html.Div(
                id="banner-logo",
                children=[
                    html.A(
                        html.Button("PLOTLY"),
                        href="https://plotly.com/get-demo/",
                    ),
                    html.A(
                        html.Img(id="logo", src=app.get_asset_url("dash-logo.png")),
                        href="https://plotly.com/dash/",
                    ),
                ],
            ),
        ],
    )


def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="Specification Settings",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Control Charts Dashboard",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )


size_auto = "auto"
sidebar_size = 12
graph_size = 10

app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        dcc.Interval(
            id="interval-component",
            interval=2 * 1000,
            n_intervals=50,
            disabled=True,
        ),
        html.Div(
            id="app-container",
            children=[
                build_tabs(),
                html.Div(
                    id="app-content",
                ),
            ],
        ),
        dcc.Store(id="value-setter", data={}),
        dcc.Store(
            id="n-interval",
            data=50,
        ),
    ],
)


app.run_server(debug=True, port=8051)
