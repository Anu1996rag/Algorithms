""" Implementing stack using singly linked list """


class EmptyStackError(Exception):
    pass


class Node:
    def __init__(self, data):
        self.data = data
        self._next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            node = Node(data)
            node._next = self.head
            self.head = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is Empty. Cannot perform pop operation")
        popped_node = self.head.data
        self.head = self.head._next
        self.size -= 1
        return popped_node

    # to get the top value of the stack
    def top(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.head.data

    # print elements of the stack
    def __str__(self):
        curr = self.head
        out = ""
        while curr:
            out += str(curr.data) + "->"
            curr = curr._next
        return out[:-3]


# Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    print(len(stack))
    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    print(len(stack))
