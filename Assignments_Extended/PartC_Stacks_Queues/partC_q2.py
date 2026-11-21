# Part C - Q2: Stack ADT using Python list


class EmptyStackError(Exception):
    pass


class ArrayStack:
    def __init__(self):
        self._items = []

    def push(self, elem):
        self._items.append(elem)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty, cannot pop")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty, cannot peek")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)


if __name__ == "__main__":
    st = ArrayStack()
    st.push(100)
    st.push(200)
    st.push(300)

    print("Stack length:", len(st))
    print("Top element:", st.peek())
    print("Popped:", st.pop())
    print("New top:", st.peek())
