class Graph:
    def __init__(self, adjacency_list=None):
        if adjacency_list is None:
            self.adjacency_list = {}
        else:
            self.adjacency_list = adjacency_list

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = {}
            return True
        return False

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2, weight):
        if vertex1 not in self.adjacency_list:
            self.add_vertex(vertex1)
        if vertex2 not in self.adjacency_list:
            self.add_vertex(vertex2)

        self.adjacency_list[vertex1][vertex2] = weight
        self.adjacency_list[vertex2][vertex1] = weight
        return True

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.adjacency_list and vertex2 in self.adjacency_list:
            if vertex2 in self.adjacency_list[vertex1]:
                del self.adjacency_list[vertex1][vertex2]
            if vertex1 in self.adjacency_list[vertex2]:
                del self.adjacency_list[vertex2][vertex1]
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for other_vertex in list(self.adjacency_list[vertex]):
                self.remove_edge(vertex, other_vertex)
            del self.adjacency_list[vertex]
            return True
        return False


if __name__ == "__main__":
    graph_data = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    g = Graph(graph_data)
    g.print_graph()
    print("\nДодавання нових ребер і вершин:")
    g.add_edge('A', 'E', 3)
    g.add_edge('F', 'G', 7)
    g.print_graph()

    print("\nВидалення ребра між A і B:")
    g.remove_edge('A', 'B')
    g.print_graph()

    print("\nВидалення вершини C:")
    g.remove_vertex('C')
    g.print_graph()
