import os

import networkx as nx
from matplotlib import pyplot as plt

from src.graph_operations import graph_operations


def analyze_graph_resistance(graph: nx.Graph, folder_path, name=""):
    graph_copy = graph.copy()
    hubs = sorted(graph_copy.degree, key=lambda x: x[1], reverse=True)[:5]
    graph_copy.remove_nodes_from([node for node, degree in hubs])

    plt.title(name)
    nx.draw(graph_copy, with_labels=True)
    plt.savefig(os.path.join(folder_path, "graph_r.png"))
    plt.show()
    plt.close()

    print(f"--< {name} - with some nodes deleted >------------------------------------------------")
    return graph_operations(graph_copy, folder_path, name, "_r")