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

    def find_kth(self, n):
        length = self.get_length()
        temp = self.head
        for each_node in range(0, length - n):
            temp = temp.next
        print(temp.data)


linked_list = LinkedList()
linked_list.insert_values(list_of_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
linked_list.find_kth(5)