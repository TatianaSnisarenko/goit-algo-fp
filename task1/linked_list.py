class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.data == other.data and self.next == other.next
        return False


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __eq__(self, other):
        if isinstance(other, LinkedList):
            if self.size != other.size:
                return False
            node1 = self.head
            node2 = other.head
            while node1 is not None and node2 is not None:
                if node1 != node2:
                    return False
                node1 = node1.next
                node2 = node2.next
            return node1 is None and node2 is None

    def insert_all(self, data):
        for value in data:
            self.insert_at_end(value)

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            self.size -= 1
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None
        self.size -= 1

    def is_empty(self):
        return self.head is None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def reverse(self):
        if self.head is None:
            return
        prev = None
        cur = self.head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        sorted_list = LinkedList()
        current = self.head

        while current:
            next = current.next

            if sorted_list.is_empty() or sorted_list.head.data >= current.data:
                sorted_list.insert_at_beginning(current.data)
            else:
                cur_sorted = sorted_list.head
                while cur_sorted.next and cur_sorted.next.data < current.data:
                    cur_sorted = cur_sorted.next
                sorted_list.insert_after(cur_sorted, current.data)
            current = next
        self.head = sorted_list.head

    def get_middle(self):
        if self.head is None:
            return None
        slow = self.head
        fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head
        self.head = self.merge_sorted().head

    def merge_sorted(self):
        if self.head is None or self.head.next is None:
            return self
        middle = self.get_middle()
        next_to_middle = middle.next
        middle.next = None
        left = LinkedList()
        right = LinkedList()
        left.head = self.head
        right.head = next_to_middle
        return self.merge(left.merge_sorted(), right.merge_sorted())

    def merge(self, list1, list2):
        if list1.head is None:
            return list2
        if list2.head is None:
            return list1

        result = LinkedList()
        cur1 = list1.head
        cur2 = list2.head
        while cur1 and cur2:
            if cur1.data <= cur2.data:
                result.insert_at_end(cur1.data)
                cur1 = cur1.next
            else:
                result.insert_at_end(cur2.data)
                cur2 = cur2.next
        while cur1:
            result.insert_at_end(cur1.data)
            cur1 = cur1.next
        while cur2:
            result.insert_at_end(cur2.data)
            cur2 = cur2.next
        return result


if __name__ == '__main__':

    list1 = LinkedList()

    data = [20, 25, 5, 10, 15]
    for value in data:
        list1.insert_at_end(value)

    print("Початковий зв'язний список:")
    list1.print_list()
    list1.reverse()
    print("\nЗв'язний список після реверсу:")
    list1.print_list()
    list1.insertion_sort()
    print("\nЗв'язний список після сортування вставками:")
    list1.print_list()

    list2 = LinkedList()

    data = [20, 25, 5, 10, 15]
    for value in data:
        list2.insert_at_end(value)
    print("\nДругий початковий зв'язний список:")
    list2.print_list()
    list2.merge_sort()
    print("\nДругий зв'язний список після сортування злиттям:")
    list2.print_list()

    two_sorted_lists = list1.merge(list1, list2)
    print("\nЗлиття двох відсортованих списків:")
    two_sorted_lists.print_list()
