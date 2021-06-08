"""
Removes duplicates from an unsorted list
"""


class Node:
    def __init__(self, data, ref=None):
        self.data = data
        self.next = ref


class LinkedList:

    # to initialize linked list object
    def __init__(self):
        self.head = None

    # printing out list of nodes
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
            
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

    def remove_duplicates(self):
        current = second = self.head

        while current is not None:
            while second.next is not None:
                if second.next.data == current.data:
                    second.next = second.next.next
                else:
                    second = second.next
            current = second = current.next


l1 = LinkedList()

# insert values
l1.insert_values([1, 2, 3,3,2,3])
l1.remove_duplicates()
l1.print_list()