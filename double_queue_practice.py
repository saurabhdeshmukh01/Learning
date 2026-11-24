class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def append_front(self, data):
        """Insert an element at the front of the deque. O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        self._size += 1

    def append_rear(self, data):
        """Insert an element at the rear of the deque. O(1)"""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1

    def pop_front(self):
        """Remove and return the front element. O(1)"""
        if self.is_empty():
            raise IndexError("pop_front from an empty deque")
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        else:
            self.front.prev = None
        self._size -= 1
        return data

    def pop_rear(self):
        """Remove and return the rear element. O(1)"""
        if self.is_empty():
            raise IndexError("pop_rear from an empty deque")
        data = self.rear.data
        self.rear = self.rear.prev
        if self.rear is None:
            self.front = None
        else:
            self.rear.next = None
        self._size -= 1
        return data

    def peek_front(self):
        """Return the front element without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek_front from an empty deque")
        return self.front.data

    def peek_rear(self):
        """Return the rear element without removing it. O(1)"""
        if self.is_empty():
            raise IndexError("peek_rear from an empty deque")
        return self.rear.data

    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "Front <-> " + " <-> ".join(items) + " <-> Rear"


# Example usage
if __name__ == "__main__":
    dq = Deque()
    dq.append_rear(10)
    dq.append_rear(20)
    dq.append_front(5)
    print(dq)  # Front <-> 5 <-> 10 <-> 20 <-> Rear

    print("Popped front:", dq.pop_front())  # 5
    print("Popped rear:", dq.pop_rear())    # 20
    print("Front now:", dq.peek_front())    # 10
    print("Size:", len(dq))                 # 1