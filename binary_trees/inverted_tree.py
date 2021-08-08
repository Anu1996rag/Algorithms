class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def _add_nodes(self, data: int):
        if self.data == data:
            return

        if data < self.data:
            if self.left:
                self.left._add_nodes(data)
            else:
                self.left = Tree(data)
        else:
            if self.right:
                self.right._add_nodes(data)
            else:
                self.right = Tree(data)

    def in_order_traversal(self) -> list:
        elements = []

        # visit the left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # visit the base node
        elements.append(self.data)

        # visit the right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements


def convert_array_to_bst(array: list) -> [Tree, None]:
    if not array:
        return None

    # get the middle element of the array
    mid = len(array) // 2

    # make it as a root
    root = Tree(array[mid])

    root.left = convert_array_to_bst(array[:mid])
    root.right = convert_array_to_bst(array[mid + 1:])

    return root


def inverted_tree(root):
    left = root.left
    root.left = root.right
    root.right = left


if __name__ == "__main__":
    nums = [1, 3, 2, 4, 3, 0]
    nums = list(set(sorted(nums)))
    num_tree = convert_array_to_bst(nums)
    inverted_tree(num_tree)
    print(f'After inverting the tree : {num_tree.in_order_traversal()}')
