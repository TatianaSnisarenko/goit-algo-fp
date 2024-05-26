import heapq
from graph import Graph
import networkx as nx


def dijkstra(graph, start_vertex):
    n = len(graph.adjacency_list)
    distances = {vertex: float('inf') for vertex in graph.adjacency_list}
    distances[start_vertex] = 0
    heap = [(0, start_vertex)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph.adjacency_list[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


if __name__ == "__main__":
    graph_data = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    g = Graph(graph_data)
    g.print_graph()

    start_vertex = 'A'
    shortest_paths = dijkstra(g, start_vertex)

    print("\nНайкоротші шляхи від вершини", start_vertex)
    print(shortest_paths)

    G = nx.Graph()

    for vertex in graph_data:
        for neighbor, weight in graph_data[vertex].items():
            G.add_edge(vertex, neighbor, weight=weight)

    nx_shortest_paths = nx.single_source_dijkstra_path_length(G, start_vertex)

    print("\nПеревірка результатів з використанням networkx")
    print(nx_shortest_paths)

    comparison = shortest_paths == nx_shortest_paths
    print("\nЧи збігаються результати? ", comparison)
