class Node:

  def __init__(self, data):
    self.data = data
    self.next = None


class stack:

  def __init__(self):
    self.top = None

  def isempty(self):
    return self.top is None

  def push(self, new_node):
    new_node.next = self.top
    self.top = new_node

  def pop(self):
    if self.isempty():
      print("Stack is empty")
      return None
    else:
      temp = self.top
      print("Poped element: ", temp.data)
      val = temp.data
      self.top = self.top.next
      temp = None
      return val

  def print(self):
    temp = self.top
    while temp is not None:
      print(temp.data, end=" -> ")
      temp = temp.next
    print("None")


class LQueue:

  def __init__(self):
    self.front = None
    self.rear = None

  def isempty(self):
    return self.front is None

  def enqueue(self, new_node):
    if self.rear is None:
      self.front = self.rear = new_node
    else:
      self.rear.next = new_node
      self.rear = new_node

  def dequeue(self):
    if self.isempty():
      print("Queue is empty")
      return None
    else:
      temp = self.front
      val = temp.data
      self.front = self.front.next
      if self.front is None:
        self.rear = None
      temp = None
      return val

  def print(self):
    temp = self.front
    while temp is not None:
      print(temp.data, end=" -> ")
      temp = temp.next
    print("None")


def reverse_stack(s1):
  q1 = LQueue()
  while not s1.isempty():  # pop from stack and enqueue to queue
    q1.enqueue(Node(s1.pop()))
    while not q1.isempty():  # dequeue from queue and push back to stack
        s1.push(Node(q1.dequeue()))
    s1.print()


def reverse_queue(q):
  s = stack()
  while not q.isempty():  # dequeue from queue and push to stack
    s.push(Node(q.dequeue()))
  while not s.isempty():  # pop from stack and enqueue back to queue
    q.enqueue(Node(s.pop()))
  q.print()



print("--- Reversing a Stack using Queue ---")
stk = stack()
stk.push(Node(10))
stk.push(Node(20))
stk.push(Node(30))
print("Original Stack:")
stk.print()
print("Reversed Stack (in Queue):")
reverse_stack(stk)

print("\n--- Reversing a Queue using Stack ---")
que = LQueue()
que.enqueue(Node(23))
que.enqueue(Node(63))
que.enqueue(Node(78))
que.enqueue(Node(90))
print("Original Queue:")
que.print()
print("Reversed Queue:")
reverse_queue(que)