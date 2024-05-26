import unittest
from graph import Graph
from dijkstra import dijkstra
import networkx as nx


class TestDijkstra(unittest.TestCase):
    def setUp(self):
        self.graph_data = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        self.g = Graph(self.graph_data)

    def test_dijkstra(self):
        G = nx.Graph()
        for vertex in self.graph_data:
            for neighbor, weight in self.graph_data[vertex].items():
                G.add_edge(vertex, neighbor, weight=weight)

        for start_vertex in self.graph_data:
            shortest_paths = dijkstra(self.g, start_vertex)
            nx_shortest_paths = nx.single_source_dijkstra_path_length(
                G, start_vertex)
            self.assertEqual(shortest_paths, nx_shortest_paths)


if __name__ == '__main__':
    unittest.main()
