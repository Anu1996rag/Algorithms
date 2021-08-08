class EmptyStackError(Exception):
    pass


class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = None

    def top(self):
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def print_stack(self):
        for element in self.stack:
            print(element)

    def isempty(self):
        return len(self.stack) == 0

    def push(self, value):
        if self.isempty():
            self.stack.append(value)
            self.minimum = value
        elif value < self.minimum:
            new_value = 2 * value - self.minimum
            self.stack.append(new_value)
            self.minimum = value
        else:
            self.stack.append(value)

    def pop(self):
        if self.isempty():
            raise EmptyStackError("Empty Stack : Cannot perform pop operation")
        popped_element = self.stack.pop()

        if popped_element < self.minimum:
            self.minimum = 2 * self.minimum - popped_element
            return self.minimum
        else:
            return popped_element

    def get_min(self):
        if self.isempty():
            raise EmptyStackError("Empty Stack")
        return self.minimum


# driver code
if __name__ == "__main__":
    stack = MinStack()
    list_of_values = [1, 2, 4, 0]
    for i in list_of_values:
        stack.push(i)
    print(stack.get_min())
    stack.pop()
    stack.pop()
    stack.print_stack()
    print(stack.top())
    print(stack.get_min())
