"""
Reversing the linked list
"""


class Node:
    def __init__(self, data, ref=None):
        self.data = data
        self.next = ref


class LinkedList:

    # to initialize linked list object
    def __init__(self):
        self.head = None

    # add node at the end of the list
    def insert_at_end(self, new_data):
        new_node = Node(new_data)

        # check if the head exists, if not make the new node as the head
        if self.head is None:
            self.head = new_node
            return

        # else traverse till the end of the list
        last = self.head
        while last.next:
            last = last.next

        # change the next of the last node
        last.next = new_node

    # inserting the list of values
    def insert_values(self, list_of_values):
        for value in list_of_values:
            self.insert_at_end(value)

    # printing out list of nodes
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


def reverse_linked_list(l1):
    # initialising variables
    previous = None
    current = l1.head
    following = current.next

    while current:
        current.next = previous # link is reversed
        previous, current = current, following
        if following:
            following = following.next

    l1.head = previous


l1 = LinkedList()

# insert values
l1.insert_values([1, 2, 3])

reverse_linked_list(l1)
l1.print_list()
