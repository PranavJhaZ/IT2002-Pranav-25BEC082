# Part D - Q3: Singly Linked List


class ListNode:
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._len = 0

    def is_empty(self):
        return self._len == 0

    def insert_first(self, val):
        new_node = ListNode(val, self.head)
        self.head = new_node
        if self._len == 0:
            self.tail = new_node
        self._len += 1

    def insert_last(self, val):
        new_node = ListNode(val)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self._len += 1

    def delete_first(self):
        if self.is_empty():
            raise IndexError("Cannot delete from an empty list")
        removed_val = self.head.value
        self.head = self.head.next
        self._len -= 1
        if self.is_empty():
            self.tail = None
        return removed_val

    def to_list(self):
        res = []
        curr = self.head
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_first(2)
    ll.insert_first(1)
    ll.insert_last(3)
    ll.insert_last(4)
    print("Elements:", ll.to_list())
    print("Deleted first:", ll.delete_first())
    print("Remaining:", ll.to_list())
