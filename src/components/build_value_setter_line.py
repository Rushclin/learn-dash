from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objs as go
import dash_daq as daq


class BuildLine:
    def __init__(self):
        self.suffix_row = "_row"
        self.suffix_button_id = "_button"
        self.suffix_sparkline_graph = "_sparkline_graph"
        self.suffix_count = "_count"
        self.suffix_ooc_n = "_OOC_number"
        self.suffix_ooc_g = "_OOC_graph"
        self.suffix_indicator = "_indicator"

    def build_value_setter_line(self, line_num, label, value, col3):
        return html.Div(
            id=line_num,
            children=[
                html.Label(label, className="four columns"),
                html.Label(value, className="four columns"),
                html.Div(col3, className="four columns"),
            ],
            className="row",
        )

    def generate_section_banner(self, title):
        return html.Div(
            className="fw-bold px-2",
            children=title,
        )

    def generate_metric_row(self, id, style, col1, col2, col3, col4, col5, col6):
        if style is None:
            style = {"height": "8rem", "width": "100%"}

        return dbc.Row(
            id=id,
            className="row metric-row",
            style=style,
            children=[
                dbc.Col(
                    id=col1["id"],
                    className="one column",
                    style={"margin-right": "2.5rem", "minWidth": "50px"},
                    children=col1["children"],
                ),
                dbc.Col(
                    id=col2["id"],
                    style={"textAlign": "center"},
                    className="one column",
                    children=col2["children"],
                ),
                dbc.Col(
                    id=col3["id"],
                    style={"height": "100%"},
                    className="four columns",
                    children=col3["children"],
                ),
                dbc.Col(
                    id=col4["id"],
                    style={},
                    className="one column",
                    children=col4["children"],
                ),
                dbc.Col(
                    id=col5["id"],
                    style={"height": "100%", "margin-top": "0"},
                    className="three columns",
                    children=col5["children"],
                ),
                dbc.Col(
                    id=col6["id"],
                    style={"display": "flex", "justifyContent": "center"},
                    className="one column",
                    children=col6["children"],
                ),
            ],
        )

    def generate_metric_list_header(self):
        return self.generate_metric_row(
            "metric_header",
            {"height": "3rem", "margin": "1rem 0", "textAlign": "center"},
            {"id": "m_header_1", "children": html.Div("Parameter")},
            {"id": "m_header_2", "children": html.Div("Count")},
            {"id": "m_header_3", "children": html.Div("Sparkline")},
            {"id": "m_header_4", "children": html.Div("OOC%")},
            {"id": "m_header_5", "children": html.Div("%OOC")},
            {"id": "m_header_6", "children": html.Div("Pass/Fail")},
        )


def generate_metric_row_helper(self, params, stopped_interval, index, state_dict):
    item = params[index]

    div_id = item + self.suffix_row
    button_id = item + self.suffix_button_id
    sparkline_graph_id = item + self.suffix_sparkline_graph
    count_id = item + self.suffix_count
    ooc_percentage_id = item + self.suffix_ooc_n
    ooc_graph_id = item + self.suffix_ooc_g
    indicator_id = item + self.suffix_indicator

    return self.generate_metric_row(
        div_id,
        None,
        {
            "id": item,
            "className": "metric-row-button-text",
            "children": html.Button(
                id=button_id,
                className="metric-row-button",
                children=item,
                title="Click to visualize live SPC chart",
                n_clicks=0,
            ),
        },
        {"id": count_id, "children": "0"},
        {
            "id": item + "_sparkline",
            "children": dcc.Graph(
                id=sparkline_graph_id,
                style={"width": "100%", "height": "95%"},
                config={
                    "staticPlot": False,
                    "editable": False,
                    "displayModeBar": False,
                },
                figure=go.Figure(
                    {
                        "data": [
                            {
                                "x": state_dict["Batch"]["data"].tolist()[
                                    :stopped_interval
                                ],
                                "y": state_dict[item]["data"][:stopped_interval],
                                "mode": "lines+markers",
                                "name": item,
                                "line": {"color": "#f4d44d"},
                            }
                        ],
                        "layout": {
                            "uirevision": True,
                            "margin": dict(l=0, r=0, t=4, b=4, pad=0),
                            "xaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "yaxis": dict(
                                showline=False,
                                showgrid=False,
                                zeroline=False,
                                showticklabels=False,
                            ),
                            "paper_bgcolor": "rgba(0,0,0,0)",
                            "plot_bgcolor": "rgba(0,0,0,0)",
                        },
                    }
                ),
            ),
        },
        {"id": ooc_percentage_id, "children": "0.00%"},
        {
            "id": ooc_graph_id + "_container",
            "children": daq.GraduatedBar(
                id=ooc_graph_id,
                color={
                    "ranges": {
                        "#92e0d3": [0, 3],
                        "#f4d44d ": [3, 7],
                        "#f45060": [7, 15],
                    }
                },
                showCurrentValue=False,
                max=15,
                value=0,
            ),
        },
        {
            "id": item + "_pf",
            "children": daq.Indicator(
                id=indicator_id, value=True, color="#91dfd2", size=12
            ),
        },
    )
