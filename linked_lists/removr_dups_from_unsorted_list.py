class Node:
    def __init__(self, data, ref=None):
        self.data = data
        self.next = ref


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def insert_at_end(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return

        # traverse till the end of the list
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_values(self, list_of_values):
        for value in list_of_values:
            self.insert_at_end(value)

    def remove_duplicates(self):
        current = self.head
        visited = set()

        visited.add(self.head.data)
        while current.next is not None:
            if current.next.data in visited:
                current.next = current.next.next
            else:
                visited.add(current.next.data)
                current = current.next

        print(visited)


linked_list = LinkedList()
linked_list.insert_values(list_of_values=[1, 2, 3, 1, 2, 3])
print(linked_list.print_list())
linked_list.remove_duplicates()
print(linked_list.print_list())
