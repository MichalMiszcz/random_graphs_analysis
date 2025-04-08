import networkx as nx
import matplotlib.pyplot as plt
import os

def graph_operations(graph: nx.Graph, folder_path, name="", file_name_addition=""):
    nodes_count = graph.number_of_nodes()
    print("Nodes number: ", nodes_count)
    edges_count = graph.number_of_edges()
    print("Edges number: ", edges_count)

    # Degree distribution
    degrees = [degree for node, degree in graph.degree()]
    plt.hist(degrees, bins=10, edgecolor="black", linewidth=0.75)
    plt.xlabel("Degree")
    plt.ylabel("Number")
    plt.title("Degree distribution")
    plt.savefig(os.path.join(folder_path, f"degree_distribution{file_name_addition}.png"))
    plt.show()
    plt.close()

    # Degree centrality
    degree_centrality = nx.degree_centrality(graph)
    nodes = list(degree_centrality.keys())
    centrality_values = list(degree_centrality.values())
    avg_degree_centrality = sum(centrality_values) / len(nodes)

    plt.figure(figsize=(8, 6))
    plt.scatter(nodes, centrality_values, color='blue', alpha=0.7)
    plt.xlabel('Nodes')
    plt.ylabel('Degree centrality')
    plt.title(f'Degree centrality in graph {name}')
    plt.savefig(os.path.join(folder_path, f"degree_centrality{file_name_addition}.png"))
    plt.show()
    plt.close()

    # Clustering distribution
    clustering = nx.clustering(graph)
    clustering_values = list(clustering.values())
    avg_clustering = sum(clustering_values) / len(nodes)

    plt.figure(figsize=(8, 6))
    plt.hist(clustering_values, bins=20, color='green', alpha=0.7)
    plt.xlabel('Clustering')
    plt.ylabel('Nodes number')
    plt.title(f'Clustering distribution in graph {name}')
    plt.savefig(os.path.join(folder_path, f"clustering_distribution{file_name_addition}.png"))
    plt.show()
    plt.close()


    if nx.is_connected(graph):
        avg_path_length = nx.average_shortest_path_length(graph)
        print(f"Average shortest path: {avg_path_length}")

        diameter = nx.diameter(graph)
        print(f"Graph's diameter: {diameter}")

        return {
            "Nodes number": nodes_count,
            "Edges number": edges_count,
            "Average shortest path": avg_path_length,
            "Diameter": diameter,
            "Average degree centrality": avg_degree_centrality,
            "Average clustering": avg_clustering
        }

    return {
        "Nodes number": nodes_count,
        "Edges number": edges_count,
        "Average shortest path": None,
        "Diameter": None,
        "Average degree centrality": avg_degree_centrality,
        "Average clustering": avg_clustering
    }