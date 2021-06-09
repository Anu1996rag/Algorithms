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

    def partition(self, given_node):
        smaller_head = smaller_tail = None
        equal_head = equal_tail = None
        greater_head = greater_tail = None

        temp = self.head
        while temp is not None:
            # if the current node is equal to the given node,
            # append it to the equally valued list
            if temp.data == given_node:
                if equal_head is None:
                    equal_head = equal_tail = temp
                else:
                    equal_tail.next = temp
                    equal_tail = temp

            # if the node is less than the given node
            elif temp.data < given_node:
                if smaller_head is None:
                    smaller_head = smaller_tail = temp
                else:
                    smaller_tail.next = temp
                    smaller_tail = temp

            # if the current node is greater than the given node
            else:
                if greater_head is None:
                    greater_head = greater_tail = temp
                else:
                    greater_tail.next = temp
                    greater_tail = temp

            # iterate through the list
            temp = temp.next

        # append None to the end of the greater list
        if greater_tail.next is not None:
            greater_tail.next = None

        # concatenation of all the lists
        # if the smaller and equal list is empty
        if smaller_head is None:
            if equal_head is None:
                return greater_head
            equal_tail.next = greater_head  # if only the smaller list is empty
            return equal_head

        # if only the equal list is empty
        if equal_head is None:
            smaller_tail.next = greater_head
            return smaller_head

        # if all the lists are non empty
        smaller_tail.next = equal_head
        equal_tail.next = greater_head
        return smaller_head


linked_list = LinkedList()
linked_list.insert_values(list_of_values=[1, 5, 0, 1, 5, 3, 4, 0, 9, 0, 11])
print(linked_list.print_list())
linked_list.partition(5)
print(linked_list.print_list())
