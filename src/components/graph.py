from dash import html
import dash_bootstrap_components as dbc
from components.build_value_setter_line import BuildLine


class Graph:
    def __init__(self):
        self.line = BuildLine()

    def build_top_panel(self):
        return dbc.Row(
            [
                dbc.Col(
                    children=[
                        self.line.generate_section_banner(
                            "Processus de control",
                        ),
                        dbc.Row(
                            id="metric-div",
                            children=[
                                self.line.generate_metric_list_header(),
                                html.Div(
                                    [],
                                    id="metric-rows",
                                ),
                            ],
                        ),
                    ],
                    id="metric-summary-session",
                    md=8,
                ),
                dbc.Col(
                    [],
                    md=4,
                ),
            ],
            id="top-section-container",
        )
