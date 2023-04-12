# DASHBOARD PAGE

from dash import html, dcc
import dash_bootstrap_components as dbc


class Settings:
    def __init__(self, params):
        print("============= INIT SETTINGS PAGE 1 ")

        self.params = params
        self.content = html.Div(
            [
                html.Div(
                    [
                        html.P(
                            "Utilisez les limites de contrôle historiques pour établir une référence ou définir de nouvelles valeurs.",
                        )
                    ],
                    className="my-5 fw-bold",
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.Div(
                                    [
                                        html.Label(
                                            "Selectionnez la metrique",
                                            id="",
                                            className="mb-3",
                                        ),
                                        html.Br(),
                                        dcc.Dropdown(
                                            id="metric-select-dropdown",
                                            options=list(
                                                {"label": param, "value": param}
                                                for param in self.params[1:]
                                            ),
                                            value=self.params[1],
                                        ),
                                    ],
                                    id="",
                                ),
                            ],
                            md=4,
                        ),
                        dbc.Col(
                            [
                                html.Div(id="value-setter-panel"),
                                html.Br(),
                                html.Div(
                                    id="value-setter-view-output",
                                    className="output-datatable",
                                ),
                                html.Div(
                                    [
                                        dbc.Row(
                                            [
                                                dbc.Col(
                                                    [
                                                        html.Button(
                                                            "Mettre à jour",
                                                            id="value-setter-set-btn",
                                                            className="btn btn-outline-primary",
                                                        ),
                                                    ],
                                                    md=6,
                                                ),
                                                dbc.Col(
                                                    [
                                                        html.Button(
                                                            "Etat courant",
                                                            id="value-setter-view-btn",
                                                            n_clicks=0,
                                                            className="btn btn-outline-primary mr-5",
                                                        ),
                                                    ],
                                                    md=6,
                                                    className="align-right",
                                                ),
                                            ]
                                        )
                                    ],
                                    className="mt-5",
                                ),
                            ],
                            md=8,
                        ),
                    ]
                ),
            ],
        )

    def get_page(self):
        return self.content
