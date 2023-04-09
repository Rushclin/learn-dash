from dash import dash, html, Input, Output, State
import dash_bootstrap_components as dbc
from layouts.layout import Layout
from pages.dashboard import Dashboard
from pages.settings import Settings


class App:
    def __init__(self):
        self.layout = Layout().get_layout()
        self.dashboard = Dashboard().get_page()
        self.settings = Settings().get_page()

    def run_app(self):
        app = dash.Dash(
            __name__,
            external_stylesheets=[
                dbc.themes.SOLAR,
            ],
        )

        app.layout = self.layout

        @app.callback(
            Output("app-content", "children"),
            Input("app-tabs", "value"),
        )
        def render_page(tab_switch):
            if tab_switch == "settings":
                return self.settings
            return self.dashboard

        app.run_server(debug=True, port=5001)


# RUN THE APP
if __name__ == "__main__":
    print("============= RUN APP =============")
    App().run_app()
