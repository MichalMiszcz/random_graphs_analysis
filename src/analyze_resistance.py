import networkx as nx

from src.graph_operations import graph_operations


def analyze_graph_resistance(graph: nx.Graph, folder_path, name=""):
    graph_copy = graph.copy()
    hubs = sorted(graph_copy.degree, key=lambda x: x[1], reverse=True)[:5]
    graph_copy.remove_nodes_from([node for node, degree in hubs])

    print(f"--< {name} - with some nodes deleted >------------------------------------------------")
    return graph_operations(graph_copy, folder_path, name, "_r")