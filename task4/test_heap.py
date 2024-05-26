import unittest
from heap import build_heap


class TestBuildHeap(unittest.TestCase):

    def is_min_heap(self, node):
        if node is None:
            return True
        if node.left and node.left.val < node.val:
            return False
        if node.right and node.right.val < node.val:
            return False
        return self.is_min_heap(node.left) and self.is_min_heap(node.right)

    def test_empty_data(self):
        data = []
        result = build_heap(data)
        self.assertIsNone(result)

    def test_single_element(self):
        data = [10]
        result = build_heap(data)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 10)
        self.assertIsNone(result.left)
        self.assertIsNone(result.right)

    def test_multiple_elements(self):
        data = [4, 10, 3, 5, 1]
        result = build_heap(data)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, min(data))
        self.assertTrue(self.is_min_heap(result))

    def test_heap_property(self):
        data = [20, 15, 30, 5, 10, 25]
        result = build_heap(data)
        self.assertIsNotNone(result)
        self.assertEqual(result.val, min(data))

        # Ensure all elements are in the tree
        def traverse(node):
            return [node.val] + traverse(node.left) + traverse(node.right) if node else []

        result_elements = traverse(result)
        self.assertCountEqual(result_elements, data)


if __name__ == '__main__':
    unittest.main()
