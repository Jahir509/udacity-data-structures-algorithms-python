"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""

class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        if type(head) == type(1):
            self.head = Element(1)
        else:
            self.head = head
    def insert_start(self, new_value):
        new_element = Element(new_value)
        new_element.next = self.head
        self.head = new_element
    def insert_end(self, new_value):
        new_element = Element(new_value)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
    def delete_start(self):
        if self.head:
            temp = self.head.value
            self.head = self.head.next
            return temp
    def delete_end(self):
        if self.head.next:
            current = self.head
            while current.next.next:
                current = current.next
            current.next = None
        elif self.head:
            self.head = None

class Queue:
    def __init__(self, head=None):
        self.storage = LinkedList(head)

    def enqueue(self, new_value):
        self.storage.insert_end(new_value)

    def peek(self):
        return self.storage.head.value

    def dequeue(self):
        return self.storage.delete_start()

# Setup
q = Queue(1)
q.enqueue(2)
q.enqueue(3)

# Test peek
# Should be 1
print(q.peek())

# Test dequeue
# Should be 1
print(q.dequeue())

# Test enqueue
q.enqueue(4)
# Should be 2
print(q.dequeue())
# Should be 3
print(q.dequeue())
# Should be 4
print(q.dequeue())
q.enqueue(5)
# Should be 5
print(q.peek())
