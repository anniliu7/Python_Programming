- First-In First-Out: first inserted item is the first to be removed
- Head and tail: the beginning and the end of the queue
- Enqueue: as in stacks, the item can only be inserted at the end of the queue
- Dequeue: unlike stacks, the item can only removed from the head of the queue
- Other types of queues: doubly ended queues; circular queues; priority queues
- Applications: 1) printing task; 2) applications where the order of requests matters (e.g., concert ticket; taxi service)

```
class Node:
  def __init_(self, data):
    self.data = data
    self.next = None

class Queue:
  def __init__(self):
    self.head = None
    self.tail = None

def enqueue(self, data):
  new_node = Node(data)
  if self.head == None:
    self.head = new_node
    self.tail = new_node
  else:
    self.tail.next = new_node # The tail's next pointer points to the new_node
    self.tail = new_node
```