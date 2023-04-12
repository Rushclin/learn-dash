import os
import pathlib

from dash import dash, html, Input, Output, State, dash_table
import pandas as pd
import dash_bootstrap_components as dbc
from layouts.layout import Layout
from pages.dashboard import Dashboard
from pages.settings import Settings
from components.index import Component
import dash_daq as daq


# Classe principale de l'application.
class App:
    def __init__(self):
        self.APP_PATH = str(pathlib.Path(__file__).parent.resolve())
        self.df = pd.read_csv(
            os.path.join(self.APP_PATH, os.path.join("data", "spc_data.csv"))
        )
        self.params = list(self.df)
        self.max_length = len(self.df)
        self.init_df = Layout(self.df).init_df()
        self.state_dict = self.init_df

        self.layout = Layout(self.df).get_layout()
        self.dashboard = Dashboard(self.params, self.state_dict).get_page()
        self.settings = Settings(list(self.params)).get_page()
        self.component = Component()

        self.ud_usl_input = daq.NumericInput(
            id="ud_usl_input", className="setting-input", size=200, max=9999999
        )
        self.ud_lsl_input = daq.NumericInput(
            id="ud_lsl_input", className="setting-input", size=200, max=9999999
        )
        self.ud_ucl_input = daq.NumericInput(
            id="ud_ucl_input", className="setting-input", size=200, max=9999999
        )
        self.ud_lcl_input = daq.NumericInput(
            id="ud_lcl_input", className="setting-input", size=200, max=9999999
        )

    def run_app(self):
        app = dash.Dash(
            __name__,
            external_stylesheets=[
                dbc.themes.SOLAR,
            ],
        )

        app.layout = self.layout

        # Definition de toutes les methodes de callback

        @app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def render_page(tab_switch):
            if tab_switch == "settings":
                return self.settings
            return self.dashboard

        @app.callback(
            output=Output("value-setter-view-output", "children"),
            inputs=[
                Input("value-setter-view-btn", "n_clicks"),
                Input("metric-select-dropdown", "value"),
                Input("value-setter-store", "data"),
            ],
        )
        def show_current_specs(n_clicks, dd_select, store_data):
            if n_clicks > 0:
                curr_col_data = store_data[dd_select]
                new_df_dict = {
                    "Specs": [
                        "Upper Specification Limit",
                        "Lower Specification Limit",
                        "Upper Control Limit",
                        "Lower Control Limit",
                    ],
                    "Current Setup": [
                        curr_col_data["usl"],
                        curr_col_data["lsl"],
                        curr_col_data["ucl"],
                        curr_col_data["lcl"],
                    ],
                }
                new_df = pd.DataFrame.from_dict(new_df_dict)
                return dash_table.DataTable(
                    style_header={"fontWeight": "bold", "color": "inherit"},
                    style_as_list_view=True,
                    fill_width=True,
                    style_cell_conditional=[
                        {"if": {"column_id": "Specs"}, "textAlign": "left"}
                    ],
                    style_cell={
                        "backgroundColor": "#1e2130",
                        "fontFamily": "Open Sans",
                        "padding": "0 2rem",
                        "color": "darkgray",
                        "border": "none",
                    },
                    css=[
                        {
                            "selector": "tr:hover td",
                            "rule": "color: #91dfd2 !important;",
                        },
                        {"selector": "td", "rule": "border: none !important;"},
                        {
                            "selector": ".dash-cell.focused",
                            "rule": "background-color: #1e2130 !important;",
                        },
                        {"selector": "table", "rule": "--accent: #1e2130;"},
                        {"selector": "tr", "rule": "background-color: transparent"},
                    ],
                    data=new_df.to_dict("rows"),
                    columns=[{"id": c, "name": c} for c in ["Specs", "Current Setup"]],
                )

            @app.callback(
                output=[
                    Output("value-setter-panel", "children"),
                    Output("ud_usl_input", "value"),
                    Output("ud_lsl_input", "value"),
                    Output("ud_ucl_input", "value"),
                    Output("ud_lcl_input", "value"),
                ],
                inputs=[Input("metric-select-dropdown", "value")],
                state=[State("value-setter-store", "data")],
            )
            def build_value_setter_panel(dd_select, state_value):
                return (
                    [
                        self.component.line.build_value_setter_line(
                            "value-setter-panel-header",
                            "Specs",
                            "Historical Value",
                            "Set new value",
                        ),
                        self.component.line.build_value_setter_line(
                            "value-setter-panel-usl",
                            "Upper Specification limit",
                            self.state_dict[dd_select]["usl"],
                            self.ud_usl_input,
                        ),
                        self.component.line.build_value_setter_line(
                            "value-setter-panel-lsl",
                            "Lower Specification limit",
                            self.state_dict[dd_select]["lsl"],
                            self.ud_lsl_input,
                        ),
                        self.component.line.build_value_setter_line(
                            "value-setter-panel-ucl",
                            "Upper Control limit",
                            self.state_dict[dd_select]["ucl"],
                            self.ud_ucl_input,
                        ),
                        self.component.line.build_value_setter_line(
                            "value-setter-panel-lcl",
                            "Lower Control limit",
                            self.state_dict[dd_select]["lcl"],
                            self.ud_lcl_input,
                        ),
                    ],
                    state_value[dd_select]["usl"],
                    state_value[dd_select]["lsl"],
                    state_value[dd_select]["ucl"],
                    state_value[dd_select]["lcl"],
                )

            @app.callback(
                output=Output("value-setter-store", "data"),
                inputs=[Input("value-setter-set-btn", "n_clicks")],
                state=[
                    State("metric-select-dropdown", "value"),
                    State("value-setter-store", "data"),
                    State("ud_usl_input", "value"),
                    State("ud_lsl_input", "value"),
                    State("ud_ucl_input", "value"),
                    State("ud_lcl_input", "value"),
                ],
            )
            def set_value_setter_store(set_btn, param, data, usl, lsl, ucl, lcl):
                if set_btn is None:
                    return data
                else:
                    data[param]["usl"] = usl
                    data[param]["lsl"] = lsl
                    data[param]["ucl"] = ucl
                    data[param]["lcl"] = lcl

                    # Recalculate ooc in case of param updates
                    data[param]["ooc"] = Layout(self.df).populate_ooc(
                        self.df[param], ucl, lcl
                    )
                    return data

        app.run_server(debug=True, port=5001)


# RUN THE APP
if __name__ == "__main__":
    print("============= RUN APP ")
    App().run_app()
