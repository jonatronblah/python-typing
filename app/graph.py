# import networkx as nx
# from networkx.classes.graph import Graph
from pydantic import BaseModel

from node import BaseNode


class BaseGraph(BaseModel):
    # G: Graph = nx.Graph()
    nodes: list[BaseNode]

    class Config:
        arbitrary_types_allowed = True
