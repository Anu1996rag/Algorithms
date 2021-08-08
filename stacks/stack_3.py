""" Implementing stack using LIFOQueue """
from queue import LifoQueue


class Stack:
    def __init__(self):
        self.stack = LifoQueue()

    def push(self, data):
        self.stack.put(data)

    def pop(self):
        return self.stack.get()

    def is_empty(self):
        return self.stack.empty()

    def is_full(self):
        return self.stack.full()

    def stack_size(self):
        return self.stack.qsize()

    def print_stack(self):
        return [data for data in list(self.stack.queue)]


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    list_of_values = [1, 5, 2, 5, 4]
    for value in list_of_values:
        stack.push(value)
    print(stack.print_stack())
    print(stack.is_full())
    print(stack.stack_size())