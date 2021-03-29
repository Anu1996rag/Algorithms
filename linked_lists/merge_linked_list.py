""" Merging two sorted linked lists
l1 = 1->2->3
l2 = 1->3->5
output = 1->1->2->3->3->5

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

    @staticmethod
    def merge_sorted_linked_lists(l1, l2):
        dummy_head = tail = Node(0)

        # checking for the edge cases
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        while l1 and l2:
            if l1.data < l2.data:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next

            tail = tail.next

        # append the remaining elements
        tail.next = l1 or l2

        return dummy_head.next


l1 = LinkedList()
l2 = LinkedList()
l3 = LinkedList()

# insert values
l1.insert_values([1,2,3])
l2.insert_values([1,3,5])

l3.head = LinkedList.merge_sorted_linked_lists(l1.head,l2.head)
l3.print_list()


