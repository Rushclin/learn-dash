from components.build_value_setter_line import BuildLine
from components.build_quick_stats_panel import BuildStat
from components.graph import Graph


class Component:
    def __init__(self):
        self.line = BuildLine()
        self.stat = BuildStat()
        self.graph = Graph()
