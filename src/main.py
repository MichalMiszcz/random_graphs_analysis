import networkx as nx
import matplotlib.pyplot as plt

import pandas as pd

import os

from analyze import analyze_graph
from analyze_resistance import analyze_graph_resistance

number = 100

def generate_graph(graph_type):
    if graph_type == "random":
        return nx.erdos_renyi_graph(n=number, p=0.1)
    elif graph_type == "scale_free":
        return nx.barabasi_albert_graph(n=number, m=2)
    elif graph_type == "small_world":
        return nx.watts_strogatz_graph(n=number, k=4, p=0.1)
    elif graph_type == "binomial_tree":
        return nx.binomial_tree(n=6)
    elif graph_type == "mycielski":
        return nx.mycielski_graph(n=6)
    elif graph_type == "sudoku":
        return nx.sudoku_graph(n=2)


def main():
    graphs_list = ["random", "scale_free", "small_world", "binomial_tree", "mycielski", "sudoku"]

    data_about_graphs = []
    data_about_graphs_resistence = []

    for graph_type in graphs_list:
        folder_path = os.path.join(".", graph_type)
        os.makedirs(folder_path, exist_ok=True)

        g = generate_graph(graph_type)

        plt.title(graph_type)
        nx.draw(g, with_labels=True)
        plt.savefig(os.path.join(folder_path, "graph.png"))
        plt.show()
        plt.close()

        graph_metrics = analyze_graph(g, folder_path, graph_type)
        graph_metrics_r = analyze_graph_resistance(g, folder_path, graph_type)

        metrics = {"Typ grafu": graph_type}
        metrics.update(graph_metrics)
        data_about_graphs.append(metrics)

        metrics_r = {"Typ grafu": graph_type}
        metrics_r.update(graph_metrics_r)
        data_about_graphs_resistence.append(metrics_r)

    columns = ["Typ grafu", "Liczba wierzchołków", "Liczba krawędzi", "Średnia najkrótsza ścieżka",
               "Średnica", "Średnia centralność stopnia", "Średni współczynnik gronowania"]
    df = pd.DataFrame(data_about_graphs, columns=columns)
    df_resistence = pd.DataFrame(data_about_graphs_resistence, columns=columns)

    print("\nDataFrame z miarami grafów:")
    print(df)

    print("\nDataFrame z zmienionymi miarami grafów po usunięciu niektórych wierzchołków:")
    print(df_resistence)

    df.to_csv("graph_analysis.csv", index=False)
    print("\nZapisano dane do pliku 'graph_analysis.csv'")

    df_resistence.to_csv("graph_resistence_analysis.csv", index=False)
    print("\nZapisano dane do pliku 'graph_resistence_analysis.csv'")


if __name__ == "__main__":
    main()