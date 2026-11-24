class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


class CircularDeque:
    def __init__(self):
        # Dummy sentinel node simplifies all insertion and deletion logic
        self.sentinel = Node()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def _insert_between(self, data, predecessor, successor):
        """Helper to insert a new node between two existing nodes. O(1)"""
        new_node = Node(data)
        new_node.prev = predecessor
        new_node.next = successor
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Helper to unlink a node and return its data. O(1)"""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        data = node.data
        node.prev = node.next = node.data = None  # Help garbage collection
        return data

    def append_front(self, data):
        """Insert an element at the front (right after sentinel). O(1)"""
        self._insert_between(data, self.sentinel, self.sentinel.next)

    def append_rear(self, data):
        """Insert an element at the rear (right before sentinel). O(1)"""
        self._insert_between(data, self.sentinel.prev, self.sentinel)

    def pop_front(self):
        """Remove and return the front element. O(1)"""
        if self.is_empty():
            raise IndexError("pop_front from an empty circular deque")
        return self._delete_node(self.sentinel.next)

    def pop_rear(self):
        """Remove and return the rear element. O(1)"""
        if self.is_empty():
            raise IndexError("pop_rear from an empty circular deque")
        return self._delete_node(self.sentinel.prev)

    def peek_front(self):
        """Return the front element without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek_front from an empty circular deque")
        return self.sentinel.next.data

    def peek_rear(self):
        """Return the rear element without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek_rear from an empty circular deque")
        return self.sentinel.prev.data

    def rotate(self, steps=1):
        """Rotate the deque right by `steps` (or left if negative). O(k)"""
        if self._size <= 1:
            return
        steps %= self._size
        for _ in range(steps):
            # Move rear item to front
            self.append_front(self.pop_rear())

    def __str__(self):
        items = []
        current = self.sentinel.next
        while current is not self.sentinel:
            items.append(str(current.data))
            current = current.next
        return "↻ [ " + " <-> ".join(items) + " ] ↺"


# Example usage
if __name__ == "__main__":
    cdq = CircularDeque()
    cdq.append_rear(10)
    cdq.append_rear(20)
    cdq.append_rear(30)
    cdq.append_front(5)
    print("Initial: ", cdq)  # ↻ [ 5 <-> 10 <-> 20 <-> 30 ] ↺

    cdq.rotate(1)
    print("Rotated: ", cdq)  # ↻ [ 30 <-> 5 <-> 10 <-> 20 ] ↺

    print("Pop front:", cdq.pop_front())  # 30
    print("Pop rear: ", cdq.pop_rear())   # 20
    print("Final:   ", cdq)               # ↻ [ 5 <-> 10 ] ↺