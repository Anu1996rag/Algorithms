class Node:
    def __init__(self, data, ref=None):
        self.data = data
        self.next = ref


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def insert_values(self, list_of_values):
        for value in list_of_values:
            self.insert_at_end(value)

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def do_intersect(self, first, second):
        visited = set()

        # storing all the elements from the first list
        temp = first.head
        while temp:
            visited.add(temp.data)
            temp = temp.next

        # traversing through the second list
        node = second.head
        while node:
            if node.data in visited:
                return True
            node = node.next
        return False

first = LinkedList()
first.insert_values(list_of_values=[1, 2, 3, 2, 1])

second = LinkedList()
second.insert_values(list_of_values=[5, 6, 0, 0, 0])

result = LinkedList()
print(result.do_intersect(first,second))



