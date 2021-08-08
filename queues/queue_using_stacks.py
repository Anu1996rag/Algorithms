"""Implementing queue using stacks """


class Queue:
    def __init__(self):
        self._enque = []
        self._deque = []

    def enqueue(self, data):
        self._enque.append(data)

    def deque(self) -> object:
        if not self._deque:
            while self._enque:
                self._deque.append(self._enque.pop())

        if not self._deque:
            raise IndexError("Empty Queue")

        return self._deque.pop()

    def print_queue(self):
        for i in self._deque:
            print(i)


que = Queue()
for d in [1, 2, 3, 3]:
    que.enqueue(1)
que.deque()
que.deque()
