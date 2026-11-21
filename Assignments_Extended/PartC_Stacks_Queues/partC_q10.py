# Part C - Q10: Circular Array Deque


class EmptyDequeError(Exception):
    pass


class CircularDeque:
    def __init__(self, capacity=5):
        self._cap = capacity
        self._data = [None] * capacity
        self._front = 0
        self._count = 0

    def is_empty(self):
        return self._count == 0

    def is_full(self):
        return self._count == self._cap

    def add_first(self, val):
        if self.is_full():
            raise OverflowError("Deque is full")
        self._front = (self._front - 1) % self._cap
        self._data[self._front] = val
        self._count += 1

    def add_last(self, val):
        if self.is_full():
            raise OverflowError("Deque is full")
        pos = (self._front + self._count) % self._cap
        self._data[pos] = val
        self._count += 1

    def delete_first(self):
        if self.is_empty():
            raise EmptyDequeError("Deque is empty")
        val = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self._cap
        self._count -= 1
        return val

    def delete_last(self):
        if self.is_empty():
            raise EmptyDequeError("Deque is empty")
        back_idx = (self._front + self._count - 1) % self._cap
        val = self._data[back_idx]
        self._data[back_idx] = None
        self._count -= 1
        return val


if __name__ == "__main__":
    dq = CircularDeque(5)
    dq.add_last(15)
    dq.add_last(25)
    dq.add_first(5)
    print("Deleted front:", dq.delete_first())
    print("Deleted back:", dq.delete_last())
