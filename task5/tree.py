from collections import deque
import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())


def insert(root, key):
    if not root:
        return Node(key)
    queue = [root]
    while queue:
        temp = queue.pop(0)
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    return root


def build_tree(data):
    if not data:
        return None
    root = Node(data[0])
    for key in data[1:]:
        root = insert(root, key)
    return root


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r,
                          y=y - 1, layer=layer + 1)
    return graph


def compute_size(node):
    if node is None:
        return 0
    else:
        return 1 + compute_size(node.left) + compute_size(node.right)


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(
        data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors)
    plt.show()


def bfs(root, total_steps):
    if root is None:
        return
    color = generate_color(0, total_steps)
    queue = deque([root])
    visited = set()
    while queue:
        node = queue.popleft()
        if node not in visited:
            node.color = color
            color = generate_color(len(visited), total_steps)
            visited.add(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


def preorder(root, total_steps):
    if root is None:
        return
    color = generate_color(0, total_steps)
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        if node not in visited:
            node.color = color
            color = generate_color(len(visited), total_steps)
            visited.add(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


def inorder(root, total_steps):
    if root is None:
        return
    color = generate_color(0, total_steps)
    stack = []
    node = root
    visited = set()
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        if node not in visited:
            node.color = color
            color = generate_color(len(visited), total_steps)
            visited.add(node)
        node = node.right


def postorder(root, total_steps):
    if root is None:
        return
    color = generate_color(0, total_steps)
    stack = [(root, False)]
    visited = set()
    while stack:
        node, visited_left_and_right = stack[-1]
        if node is None:
            stack.pop()
            continue
        if visited_left_and_right:
            node.color = color
            color = generate_color(len(visited), total_steps)
            visited.add(node)
            stack.pop()
        else:
            stack[-1] = (node, True)
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))


def generate_color(step, total_steps):
    base_color = [18, 150, 240]
    lighten_factor = step / total_steps
    new_color = [int(c + (255 - c) * lighten_factor) for c in base_color]
    return f'#{new_color[0]:02X}{new_color[1]:02X}{new_color[2]:02X}'


def draw_tree_bfs(root, total_steps):
    bfs(root, total_steps)
    draw_tree(root)


def draw_tree_preorder(root, total_steps):
    preorder(root, total_steps)
    draw_tree(root)


def draw_tree_inorder(root, total_steps):
    inorder(root, total_steps)
    draw_tree(root)


def draw_tree_postorder(root, total_steps):
    postorder(root, total_steps)
    draw_tree(root)


if __name__ == "__main__":

    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)

    print(compute_size(root))
    print(generate_color(2, 6))
