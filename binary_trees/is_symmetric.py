class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isMirror(node_1, node_2):
    # if both the nodes are None
    if node_1 is None and node_2 is None:
        return True

    """ For two trees to be mirror images,
            the following three conditions must be true
            1 - Their root node's key must be same
            2 - left subtree of left tree and right subtree
              of the right tree have to be mirror images
            3 - right subtree of left tree and left subtree
               of right tree have to be mirror images
    """
    if node_1 is not None and node_2 is not None:
        if node_1.data == node_2.data:
            return isMirror(node_1.right, node_2.left) and isMirror(node_1.left, node_2.right)

    # if none of the above conditions are satisfied,
    return False


def is_symmetric(node):
    return isMirror(node_1=node, node_2=node)


# driver code
root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(7)
root.right.right = Node(3)
print("Symmetric" if is_symmetric(root) == True else "Not symmetric")
