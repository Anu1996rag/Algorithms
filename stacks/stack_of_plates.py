class CapacityError(Exception):
    pass


class StackOfPlates:
    def __init__(self, capacity):
        self.stacks = []
        if capacity < 1:
            raise CapacityError("Capacity cannot be less than 1")
        self.capacity = capacity

    def push(self, item):
        if not len(self.stacks):
            self.stacks.append([item])
        else:
            if len(self.stacks[-1]) >= self.capacity:
                self.stacks.append([item])
            else:
                self.stacks[-1].append(item)

    def pop(self):
        popped = self.stacks[-1].pop()
        if len(self.stacks[-1]) == 0:
            del self.stacks[-1]
        return popped

    def print_stack(self):
        print(self.stacks)


# Driver Code
if __name__ == "__main__":
    stack = StackOfPlates(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print_stack()
    stack.pop()
    stack.pop()
    stack.print_stack()
