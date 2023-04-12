from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd

from layouts.header import Header
from layouts.navbar import Navbar


class Layout:
    def __init__(self, DF):
        print("============= INIT LAYOUT")
        self.header = Header().get_header()
        self.navbar = Navbar().get_navbar()
        self.DF = DF

        self.layout = dbc.Container(
            fluid=True,
            children=[
                self.header,
                html.Hr(),
                self.navbar,
                html.Div(
                    id="app-content",
                    className="mx-5",
                ),
                dcc.Store(
                    id="value-setter-store",
                    data=self.init_value_setter_store(),
                ),
                dcc.Store(
                    id="n-interval-stage",
                    data=50,
                ),
            ],
            id="app-container",
        )

    def init_df(self):
        ret = {}
        for col in list(self.DF[1:]):
            data = self.DF[col]
            stats = data.describe()

            std = stats["std"].tolist()
            ucl = (stats["mean"] + 3 * stats["std"]).tolist()
            lcl = (stats["mean"] - 3 * stats["std"]).tolist()
            usl = (stats["mean"] + stats["std"]).tolist()
            lsl = (stats["mean"] - stats["std"]).tolist()

            ret.update(
                {
                    col: {
                        "count": stats["count"].tolist(),
                        "data": data,
                        "mean": stats["mean"].tolist(),
                        "std": std,
                        "ucl": round(ucl, 3),
                        "lcl": round(lcl, 3),
                        "usl": round(usl, 3),
                        "lsl": round(lsl, 3),
                        "min": stats["min"].tolist(),
                        "max": stats["max"].tolist(),
                        "ooc": self.populate_ooc(data, ucl, lcl),
                    }
                }
            )

        return ret

    def populate_ooc(self, data, ucl, lcl):
        ooc_count = 0
        ret = []
        for i in range(len(data)):
            if data[i] >= ucl or data[i] <= lcl:
                ooc_count += 1
                ret.append(ooc_count / (i + 1))
            else:
                ret.append(ooc_count / (i + 1))
        return ret

    def init_value_setter_store(self):
        # state_dict = self.init_df()
        return self.init_df()

    def get_layout(self):
        return self.layout
