import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()

    def test_init(self):
        self.assertEqual(self.graph.adjacency_list, {})

    def test_add_vertex(self):
        self.assertTrue(self.graph.add_vertex('A'))
        self.assertIn('A', self.graph.adjacency_list)
        self.assertFalse(self.graph.add_vertex('A'))

    def test_add_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.assertTrue(self.graph.add_edge('A', 'B', 1))
        self.assertIn('B', self.graph.adjacency_list['A'])
        self.assertIn('A', self.graph.adjacency_list['B'])
        self.assertEqual(self.graph.adjacency_list['A']['B'], 1)
        self.assertEqual(self.graph.adjacency_list['B']['A'], 1)

    def test_remove_edge(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 1)
        self.assertTrue(self.graph.remove_edge('A', 'B'))
        self.assertNotIn('B', self.graph.adjacency_list['A'])
        self.assertNotIn('A', self.graph.adjacency_list['B'])
        self.graph.remove_vertex('A')
        self.graph.remove_vertex('B')
        self.assertFalse(self.graph.remove_edge('A', 'B'))

    def test_remove_vertex(self):
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        self.graph.add_edge('A', 'B', 1)
        self.assertTrue(self.graph.remove_vertex('A'))
        self.assertNotIn('A', self.graph.adjacency_list)
        self.assertFalse(self.graph.remove_vertex('A'))


if __name__ == '__main__':
    unittest.main()
