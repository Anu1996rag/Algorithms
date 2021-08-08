""" Implementing stack using deque
    Time Complexity O(1)
"""
from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, data):
        return self.stack.append(data)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return "Pop operation on empty stack"

    def print_stack(self):
        return [data for data in self.stack]

    def is_empty(self):
        return len(self.stack) == 0


if __name__ == "__main__":
    stack = Stack()
    print(stack.is_empty())
    list_of_values = [1,5,2,5,4]
    for value in list_of_values:
        stack.push(value)
    print(stack.print_stack())
