import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def add_nodes(root, key):
    if root is None:
        return Node(key)

    if key < root.data:
        root.left = add_nodes(root.left, key)
    else:
        root.right = add_nodes(root.right, key)

    return root


# Function to determine whether a given binary tree is a BST
def checkForBST(root):
    if is_binary_search_tree(root, min_key=-sys.maxsize, max_key=sys.maxsize):
        print("The tree is a BST.")
    else:
        print("The tree is not a BST")


def is_binary_search_tree(node, min_key, max_key):
    if node is None:
        return True

    if node.data < min_key or node.data > max_key:
        return False

    return is_binary_search_tree(node.left, min_key=min_key, max_key=node.data) and \
           is_binary_search_tree(node=node.right, min_key=node.data, max_key=max_key)


# swapping the nodes
def swap(root):
    left = root.left
    root.left = root.right
    root.right = left


if __name__ == '__main__':

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = add_nodes(root, key)
    swap(root)
    checkForBST(root)
