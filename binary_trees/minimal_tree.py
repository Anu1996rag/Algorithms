class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def convert_array_to_bst(array: list) -> [Node, None]:
    if not array:
        return None

    # get the middle element of the array
    mid = len(array) // 2

    # make it as a root
    root = Node(array[mid])

    root.left = convert_array_to_bst(array[:mid])
    root.right = convert_array_to_bst(array[mid + 1:])

    return root


def pre_order(node):
    if not node:
        return None
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)


arr = [1, 2, 3, 4, 5, 6]
bst = convert_array_to_bst(array=arr)
pre_order(bst)
