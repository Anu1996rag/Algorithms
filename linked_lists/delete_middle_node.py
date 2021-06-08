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

    def get_length(self):
        length = 0
        itr = self.head

        while itr:
            length += 1
            itr = itr.next

        return length

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next

    def delete_middle_node(self):
        temp = self.head
        current = None
        length = self.get_length()

        mid_count = length // 2 if length % 2 == 0 else (length // 2) + 1
        # count to the middle of the list
        for i in range(0, mid_count - 1):
            current = temp
            temp = temp.next
        # delete the element in the middle
        if current is not None:
            current.next = temp.next
            temp = None


linked_list = LinkedList()
linked_list.insert_values(list_of_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11])
print(linked_list.print_list())
linked_list.delete_middle_node()
print(linked_list.print_list())
