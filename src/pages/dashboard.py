# DASHBOARD PAGE

from dash import html
from components.index import Component
import dash_bootstrap_components as dbc


class Dashboard:
    def __init__(self, params, state_dic):
        print("============= INIT DASHBOARD PAGE ")
        self.build_quick_stats_panel = Component().stat.build_quick_stats_panel()
        self.build_top_panel = Component().graph.build_top_panel()

        self.content = dbc.Row(
            [
                dbc.Col(
                    [
                        self.build_quick_stats_panel,
                    ],
                    md=3,
                ),
                dbc.Col(
                    [
                        Component().graph.build_top_panel(),
                    ],
                    id="graphs-container",
                    md=9,
                    className="p-3"
                    # children=[build_top_panel(stopped_interval), build_chart_panel()],
                ),
            ],
            id="status-container",
            className="px-3",
        )

    def get_page(self):
        return self.content
