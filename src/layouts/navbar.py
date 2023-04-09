# NAVBAR COMPONENT

from dash import html, dcc


class Navbar:
    def __init__(self):
        self.tabs = html.Div(
            id="tabs",
            className="tabs",
            children=[
                dcc.Tabs(
                    id="app-tabs",
                    value="tab2",
                    className="custum-tabs mx-5 mb-2",
                    children=[
                        dcc.Tab(
                            id="setting_tab",
                            label="PARAMETRAGES DU DASHBOARD",
                            value="settings",
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                        dcc.Tab(
                            id="control_tab",
                            label="GRAPHES DE CONTRôLE",
                            value="graphes",
                            className="custom-tab text-uppercase",
                            selected_className="custom-tab--selected",
                        ),
                    ],
                )
            ],
        )

    def get_navbar(self):
        return self.tabs
