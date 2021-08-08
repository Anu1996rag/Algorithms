""" Implementing stack operations using list
    Time Complexity O(n)
"""


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, data):
        return self.stack.append(data)

    def pop(self):
        try:
            return self.stack.pop()
        except IndexError:
            return "Stack is empty"

    def print_stack(self):
        return [data for data in self.stack]


if __name__ == "__main__":

    stack = Stack()
    list_of_values = [1, 2, 3, 4, 5]
    for value in list_of_values:
        stack.push(value)

    print(stack.print_stack())
    stack.pop()
    print(stack.print_stack())
