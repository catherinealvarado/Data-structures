class Node:
    """Simple node implementation."""
    def __init__(self,key=None):
        self.key = key
        self.next = None

class Queue(object):
    """
    Implementation of a queue.
    Queue will follow FIFO (First In First Out).
    """

    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def __str__(self):
        """Prints out the queue as a list."""
        s = "["
        p = self.head
        if p:
            while p.next:
                s += str(p.key) +", "
                p = p.next
            s += str(p.key) +"]"
            return s

    def enqueue(self,key):
        """
        Add new node to queue. Adds it to the end of queue.
        Running time: O(1)
        """
        node = Node(key)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        """
        Remove and return the first node in queue.
        Running time: O(1)
        """
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
