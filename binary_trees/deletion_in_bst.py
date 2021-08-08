class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, current_node, value):
        if current_node is None:
            current_node = Node(value)
        elif value < current_node.value:
            current_node.left = self.insert(current_node.left, value)
        else:
            current_node.right = self.insert(current_node.right, value)
        return current_node

    # To find the inorder successor which is the smallest node in the subtree
    def findsuccessor(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete(self, current_node, value):
        if current_node is None:
            return current_node
        if value == current_node.value:

            if current_node.left is None:
                current_node = current_node.right
            elif current_node.right == None:
                current_node = current_node.left
            else:
                # deletion of nodes with 2 children
                # find the inorder successor and replace the current node
                current_node = self.findsuccessor(current_node)
                current_node.right = self.delete(current_node.right, current_node.value)
        elif value < current_node.value:
            current_node.left = self.delete(current_node.left, value)
        else:
            current_node.right = self.delete(current_node.right, value)

        return self


arr = list(map(int, input().split(',')))
print(arr)
# Choose a root node
root = Node(arr[0])
for value in arr[1:]:
    root.insert(root, value)

delete_val = int(input("Enter the value to be deleted : "))
root = root.delete(root, delete_val)
print("The value of the root is", root)

