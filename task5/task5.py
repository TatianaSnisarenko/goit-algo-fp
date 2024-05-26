
from tree import Node, draw_tree_bfs, draw_tree_preorder, draw_tree_inorder, draw_tree_postorder, compute_size, build_tree


if __name__ == "__main__":

    root = build_tree([0, 4, 1, 5, 10, 3, 14, 6, 7, 8, 9, 2, 31, 98, 77])
    total_steps = compute_size(root)

    while True:
        order = input(
            "Введіть порядок обходу (bfs, pre, in, post), або exit: ")
        if order == "bfs":
            draw_tree_bfs(root, total_steps)
        elif order == "pre":
            draw_tree_preorder(root, total_steps)
        elif order == "in":
            draw_tree_inorder(root, total_steps)
        elif order == "post":
            draw_tree_postorder(root, total_steps)
        elif order == "exit":
            break
        else:
            print("Невірний ввід! Будь ласка, спробуте ще раз.")
