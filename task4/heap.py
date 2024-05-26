import heapq
from tree import Node, draw_tree


class HeapNode(Node):
    def __init__(self, key, color="skyblue"):
        super().__init__(key, color)


def insert_heap(root, key):
    if not root:
        return HeapNode(key)
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left = HeapNode(key)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = HeapNode(key)
            break
        else:
            queue.append(temp.right)
    return root


def build_heap(data):
    heapq.heapify(data)
    if not data:
        return None
    root = HeapNode(data[0])
    for key in data[1:]:
        root = insert_heap(root, key)
    return root


def draw_heap(data):
    heap_root = build_heap(data)
    draw_tree(heap_root)
