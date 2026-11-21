# Part C - Q8: Circular Array Queue


class EmptyQueueError(Exception):
    pass


class CircularQueue:
    def __init__(self, capacity=5):
        self._capacity = capacity
        self._data = [None] * capacity
        self._front = 0
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self._capacity

    def enqueue(self, val):
        if self.is_full():
            raise OverflowError("Queue reached maximum capacity")
        next_idx = (self._front + self._size) % self._capacity
        self._data[next_idx] = val
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty, cannot dequeue")
        out = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return out

    def front(self):
        if self.is_empty():
            raise EmptyQueueError("Queue is empty")
        return self._data[self._front]


if __name__ == "__main__":
    q = CircularQueue(5)
    for num in [1, 2, 3, 4]:
        q.enqueue(num)
        print(f"Enqueued: {num}")

    print("Front item:", q.front())
    print("Dequeued item:", q.dequeue())
    q.enqueue(5)
    q.enqueue(6)
    print("Front item after adds:", q.front())
