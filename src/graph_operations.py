import networkx as nx
import matplotlib.pyplot as plt
import os

def graph_operations(graph: nx.Graph, folder_path, name="", file_name_addition=""):
    nodes_count = graph.number_of_nodes()
    print("Liczba wierzchołków: ", nodes_count)
    edges_count = graph.number_of_edges()
    print("Liczba krawędzi: ", edges_count)

    # Rozkład stopni wierzchołków
    degrees = [degree for node, degree in graph.degree()]
    plt.hist(degrees, bins=10, edgecolor="black", linewidth=0.75)
    plt.xlabel("Stopień")
    plt.ylabel("Liczba")
    plt.title("Dystrbucja stopni")
    plt.savefig(os.path.join(folder_path, f"dystrybucja_stopni{file_name_addition}.png"))
    plt.show()
    plt.close()

    # Wykres centralności stopnia
    degree_centrality = nx.degree_centrality(graph)
    nodes = list(degree_centrality.keys())
    centrality_values = list(degree_centrality.values())
    avg_degree_centrality = sum(centrality_values) / len(nodes)

    plt.figure(figsize=(8, 6))
    plt.scatter(nodes, centrality_values, color='blue', alpha=0.7)
    plt.xlabel('Wierzchołki')
    plt.ylabel('Centralność stopnia')
    plt.title(f'Centralność stopnia w grafie {name}')
    plt.savefig(os.path.join(folder_path, f"centralnosc_stopnia{file_name_addition}.png"))
    plt.show()
    plt.close()
    # Oś X: Numer wierzchołka (od 0 do 99 w naszym przypadku).
    # Oś Y: Wartość centralności stopnia (miara od 0 do 1, proporcjonalna do liczby sąsiadów wierzchołka).

    # Współczynnik gronowania
    clustering = nx.clustering(graph)
    clustering_values = list(clustering.values())
    avg_clustering = sum(clustering_values) / len(nodes)

    plt.figure(figsize=(8, 6))
    plt.hist(clustering_values, bins=20, color='green', alpha=0.7)
    plt.xlabel('Współczynnik gronowania')
    plt.ylabel('Liczba wierzchołków')
    plt.title(f'Rozkład współczynnika gronowania w grafie {name}')
    plt.savefig(os.path.join(folder_path, f"rozklad_gronowania{file_name_addition}.png"))
    plt.show()
    plt.close()
    # Oś X: Wartości współczynnika gronowania (od 0 do 1).
    # Oś Y: Liczba wierzchołków, które mają daną wartość gronowania.
    # W grafie Small World większość wierzchołków ma wysoki współczynnik gronowania (bliżej 1),
    # co oznacza, że tworzą one gęste klastry. To charakterystyczne dla sieci typu "mały świat",
    # np. sieci społecznych.

    if nx.is_connected(graph):
        avg_path_length = nx.average_shortest_path_length(graph)
        print(f"Średnia najkrótsza ścieżka: {avg_path_length}")

        diameter = nx.diameter(graph)
        print(f"Średnica grafu: {diameter}")

        return {
            "Liczba wierzchołków": nodes_count,
            "Liczba krawędzi": edges_count,
            "Średnia najkrótsza ścieżka": avg_path_length,
            "Średnica": diameter,
            "Średnia centralność stopnia": avg_degree_centrality,
            "Średni współczynnik gronowania": avg_clustering
        }

    return {
        "Liczba wierzchołków": nodes_count,
        "Liczba krawędzi": edges_count,
        "Średnia najkrótsza ścieżka": None,
        "Średnica": None,
        "Średnia centralność stopnia": avg_degree_centrality,
        "Średni współczynnik gronowania": avg_clustering
    }