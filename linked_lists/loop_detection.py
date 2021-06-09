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

    def is_looping(self):
        temp = self.head
        visited = set()

        while temp:
            if temp.data in visited:
                return True
            visited.add(temp.data)
            temp = temp.next

        return False

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next


first = LinkedList()
first.head = Node(10)
first.insert_at_end(20)
first.insert_at_end(30)
first.insert_at_end(10)
print(first.print_list())
print(first.is_looping())
