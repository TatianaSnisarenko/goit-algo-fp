import unittest
from linked_list import LinkedList, Node


class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.list = LinkedList()

    def test_insert_at_beginning(self):
        self.list.insert_at_beginning(5)
        self.assertEqual(self.list.head.data, 5)
        self.assertEqual(self.list.size, 1)

    def test_insert_at_end(self):
        self.list.insert_at_end(5)
        self.list.insert_at_end(10)
        self.assertEqual(self.list.head.data, 5)
        self.assertEqual(self.list.head.next.data, 10)
        self.assertEqual(self.list.size, 2)

    def test_insert_after(self):
        self.list.insert_at_end(5)
        self.list.insert_after(self.list.head, 10)
        self.assertEqual(self.list.head.next.data, 10)
        self.assertEqual(self.list.size, 2)

    def test_delete_node(self):
        self.list.insert_at_end(5)
        self.list.insert_at_end(10)
        self.list.delete_node(5)
        self.assertEqual(self.list.head.data, 10)
        self.assertEqual(self.list.size, 1)

    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.insert_at_end(5)
        self.assertFalse(self.list.is_empty())

    def test_search_element(self):
        self.list.insert_all([25, 35, 5, 20, 10])
        self.assertEqual(self.list.search_element(10).data, 10)
        self.assertIsNone(self.list.search_element(15))

    def test_reverse(self):
        self.list.insert_all([25, 15, 5, 20, 10])
        self.list.reverse()
        expected_list = LinkedList()
        expected_list.insert_all([10, 20, 5, 15, 25])
        self.assertEqual(self.list, expected_list)

    def test_insertion_sort(self):
        data = [25, 15, 5, 20, 10, 5]
        for value in data:
            self.list.insert_at_end(value)
        self.list.insertion_sort()
        expected_list = LinkedList()
        expected_list.insert_all([5, 5, 10, 15, 20, 25])
        self.assertEqual(self.list, expected_list)

    def test_get_middle_odd(self):
        data = [25, 15, 5, 20, 10]
        for value in data:
            self.list.insert_at_end(value)
        self.assertEqual(self.list.get_middle().data, 5)

    def test_get_middle_even(self):
        data = [25, 15, 5, 20]
        for value in data:
            self.list.insert_at_end(value)
        self.assertEqual(self.list.get_middle().data, 15)

    def test_merge_sort_odd(self):
        data = [25, 15, 5, 20, 10]
        for value in data:
            self.list.insert_at_end(value)
        self.list.merge_sort()
        expected_list = LinkedList()
        expected_list.insert_all([5, 10, 15, 20, 25])
        self.assertEqual(self.list, expected_list)

    def test_merge_sort_even(self):
        data = [20, 10, 5, 15]
        for value in data:
            self.list.insert_at_end(value)
        self.list.merge_sort()
        expected_list = LinkedList()
        expected_list.insert_all([5, 10, 15, 20])
        self.assertEqual(self.list, expected_list)

    def test_merge(self):
        list1 = LinkedList()
        data = [5, 10, 15]
        for value in data:
            list1.insert_at_end(value)
        data = [6, 11, 16]
        list2 = LinkedList()
        for value in data:
            list2.insert_at_end(value)
        merged_list = list1.merge(list1, list2)
        expected_list = LinkedList()
        expected_list.insert_all([5, 6, 10, 11, 15, 16])
        self.assertEqual(merged_list, expected_list)

    def test_eq(self):
        # Test when both lists are empty
        list1 = LinkedList()
        list2 = LinkedList()
        self.assertEqual(list1, list2)

        # Add elements to the lists
        list1.insert_all([5, 10, 15])
        list2.insert_all([5, 10, 15])
        self.assertEqual(list1, list2)

        # Test when lists have different sizes
        list1.insert_at_end(20)
        self.assertNotEqual(list1, list2)

        # Test when lists have same sizes but different elements
        list2.insert_at_beginning(20)
        self.assertNotEqual(list1, list2)


if __name__ == '__main__':
    unittest.main()
