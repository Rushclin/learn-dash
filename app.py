from dash import dash, html, Input, Output
import dash_bootstrap_components as dbc
from layouts.layout import Layout
import datetime as datetime
import pandas as pd


class App:
    def __init__(self):
        self.title = 'Petit Chrnometre'
        self.layout = Layout().render()

    def load_data(self):
        return

    def run_app(self):
        print(self.load_data())
        app = dash.Dash(
            __name__,
            external_stylesheets=[
                dbc.themes.LUX,
            ],
        )

        app.layout = self.layout

        # CALLBACKS

        @app.callback(
            Output('timer', 'children'),
            Input('interval-component', 'n_intervals')
        )
        def update_times(n):
            time = datetime.datetime.now()

            return [
                html.H1('Heure locale : '+str(time))
            ]

        # RUN THE APP SERVER
        app.run_server(debug=True, port=8089)


# RUN THE APP
if __name__ == "__main__":
    print("============= RUN APP ")
    App().run_app()
