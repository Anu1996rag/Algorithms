"""Implementing circular queue"""


class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.head = self.tail = -1

    def enqueue(self, item):
        if (self.tail + 1) % self.capacity == self.head:
            print("Circular queue is full.")

        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item

        else:
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = item

    def deque(self):
        temp = None
        if self.head == -1:
            print("Circular queue is full")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = self.tail = -1
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.capacity
        return temp

    def print_circular_queue(self):
        if self.head == -1:
            print("No element in the circular queue")

        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Your MyCircularQueue object will be instantiated and called as such:
obj = CircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.print_circular_queue()

obj.deque()
print("After removing an element from the queue")
obj.print_circular_queue()
