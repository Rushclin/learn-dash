from dash import html
import dash_daq as daq
import dash_bootstrap_components as dbc


class BuildStat:
    def build_quick_stats_panel(self):
        return dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            id="card-1",
                            children=[
                                html.P(
                                    "Identification",
                                    className="fw-bold",
                                ),
                                daq.LEDDisplay(
                                    id="operator-led",
                                    value="1704",
                                    color="#92e0d3",
                                    backgroundColor="#1e2130",
                                    size=50,
                                ),
                            ],
                        ),
                    ],
                    md=12,
                    className="my-5",
                ),
                dbc.Col(
                    [
                        html.Div(
                            id="card-2",
                            children=[
                                html.P(
                                    "Heure de completion",
                                    className="fw-bold",
                                ),
                                daq.Gauge(
                                    id="progress-gauge",
                                    max=10 * 2,
                                    min=0,
                                    showCurrentValue=True,  # default size 200 pixel
                                ),
                            ],
                        ),
                    ],
                    md=12,
                    className="my-5",
                ),
                dbc.Col(
                    [
                        html.Div(
                            id="utility-card",
                            children=[
                                daq.StopButton(
                                    id="stop-button",
                                    size=160,
                                    n_clicks=0,
                                )
                            ],
                            className="center",
                        ),
                    ],
                    md=12,
                ),
            ],
            className="bg-dark p-3",
        )
