# DASHBOARD PAGE

from dash import html


class Dashboard:
    def __init__(self):
        self.content = html.Div(
            [
                html.H1(
                    "Takam Rushclin",
                ),
            ],
        )

    def get_page(self):
        return self.content
