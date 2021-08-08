"""Sorting of stack using a temp stack"""


class Stack:
    def __init__(self) -> None:
        self._stack = []

    def is_empty(self) -> bool:
        return len(self._stack) == 0

    def push(self, item):
        self._stack.append(item)

    def top(self) -> int:
        return self._stack[-1]

    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self._stack.pop()

    def sort_stack(self):
        # creating a temporary stack
        temp_stack = Stack()
        # wihle the input stack is not empty
        while not self.is_empty():
            # pop one element from the input stack
            temp = self._stack.pop()

            # while the temporary stack is not empty, check if top of temporary stack is
            # greater than the temp
            while not temp_stack.is_empty() and int(temp_stack.top()) > int(temp):
                # pop the element from the temporary stack and push it to input stack
                self.push(temp_stack.top())
                temp_stack.pop()

            temp_stack.push(temp)

        # sorted elements will be in the temporary stack
        return temp_stack

    def print_stack(self, stack):
        while not stack.is_empty():
            print(stack.pop(), end=" ")


stack = Stack()
for i in [1, 2, 0, 4, 2, 90, 12, 34 ,132]:
    stack.push(i)
sorted_stack = stack.sort_stack()
stack.print_stack(sorted_stack)
