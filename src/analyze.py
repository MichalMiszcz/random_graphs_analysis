import networkx as nx

from src.graph_operations import graph_operations


def analyze_graph(graph: nx.Graph, folder_path, name=""):
    print()
    print(f"--< {name} >------------------------------------------------")
    return graph_operations(graph, folder_path, name)
