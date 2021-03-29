""" Implementation of linked list in Python """


# for Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next  # Initializing next as null


class LinkedList:
    # to initialize linked list object
    def __init__(self):
        self.head = None

    # to add new node in the beginning
    def insert_at_head(self, new_data):
        new_node = Node(new_data)

        # make head of current list to be pointed to new node
        new_node.next = self.head

        # make the new node as the head
        self.head = new_node

    def get_length(self):

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    # to insert at the given node
    def insert_at_given_index(self, index, data):

        if index < 0 or index > self.get_length():
            return "Invalid index"

        if index == 0:
            self.insert_at_head(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                break
            itr = itr.next
            count += 1

    def insert_after_given_node(self, given_node, new_data):
        # checks if the previous or given node exists
        if given_node is None:
            print("Given node is not in linked list.")
            return

        # make the pointer of the given node as the pointer of the new node
        node = self.head
        while node.next:
            if node.data == given_node:
                new_node = Node(new_data, node.next)
                node.next = new_node
                break
            node = node.next

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

    # removing element at the index
    def remove_at(self,index_value):

        if index_value < 0 or index_value > self.get_length():
            raise Exception("Invalid index")

        if index_value == 0:
            self.head = self.head.next

        # to insert and remove elements from the list
        # we need to keep the count
        count = 0
        itr = self.head
        while itr:
            if itr == index_value - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    # printing out list of nodes
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


# to start execution
if __name__ == "__main__":
    l1 = LinkedList()

    # initializing head
    l1.head = Node(1)
    # adding 2 other nodes
    second = Node(2)
    third = Node(5)

    # linking first node with the second
    l1.head.next = second

    # linking second node to the third
    second.next = third

    # inserting at the beginning of the list
    l1.insert_at_head(0)

    # inserting at the end of the list
    l1.insert_at_end(10)

    # inserting after given node of the list
    l1.insert_after_given_node(2, 59)

    # insert at given index
    l1.insert_at_given_index(2, 7)

    # inserting list of values
    l1.insert_values([11,12,14])

    # remove at given index
    l1.remove_at(0)

    # printing out list
    l1.print_list()

    # get length of the list
    print(l1.get_length())
