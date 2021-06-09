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

    def sum_of_lists(self, first, second):
        prev = None
        temp = None
        carry = 0

        # traversing through both the lists
        while first is not None or second is not None:
          
            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data

            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0
            # update the sum if it is greater than 10
            sum = sum if sum < 10 else sum % 10

            # creating node
            temp = Node(sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next
            if second is not None:
                second = second.next

        # for leftover carry
        if carry > 0:
            temp.next = Node(carry)


first = LinkedList()
first.insert_values(list_of_values=[3, 1, 7])
second = LinkedList()
second.insert_values(list_of_values=[8, 0, 3])

result = LinkedList()
result.sum_of_lists(first.head, second.head)
print(result.print_list())
