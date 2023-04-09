# DASHBOARD PAGE

from dash import html


class Settings:
    def __init__(self):
        self.content = html.Div(
            [
                html.H1(
                    "Takam Rushclin setting",
                ),
            ],
        )

    def get_page(self):
        return self.content
