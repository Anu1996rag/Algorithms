"""This file implements binary seaaarch tree"""


class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data: int):
        # if duplicate key found , ignore
        if self.data == data:
            return

        # visit from left sub tree if the data is less than current data
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

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

    def search(self, value: int) -> bool:
        if self.data == value:
            return True

        # if the value is less than current node data,
        # then search for the left subtree
        if value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False

        # if the value is greater than current node data,
        # then search for the right subtree
        if value > self.data:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def find_min(self):
        # iterate through the left sub tree all the time till the leaf node
        if self.left is None:
            return self.data
        return self.left.find_min()

    def find_max(self):
        # iterate through the right sub tree all the time till the leaf node
        if self.right is None:
            return self.data
        return self.right.find_max()

    def delete_node(self,node):
        if node < self.data:
            if self.left:
                self.left = self.left.delete(node)
        elif node > self.data:
            if self.right:
                self.right = self.right.delete(node)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            # choosing the minimum value from the right subtree
            min_value = self.right.find_min()
            # assigning the minimum value to the current node
            self.data = min_value
            # deleting it from the tree
            self.right = self.right.delete(min_value)
        return self


def build_tree(elements: list):
    # take the first element as the root of the tree
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == "__main__":
    nums = [1, 3, 2, 4, 3,0]
    num_tree = build_tree(nums)
    # print(num_tree.in_order_traversal())
    # print(num_tree.search(7))
    # print(num_tree.find_min())
    # print(num_tree.find_max())
    num_tree.delete_node(0)
    print(f'After deleting the node : {num_tree.in_order_traversal()}')
