class Node:
    def __init__(self,key=None):
        self.key = key
        self.next = None

class LinkedList(object):
    """
    Basic implementation of singly linked list.
    """

    def __str__(self):
        """Prints out the linked list as a list."""
        s = "["
        p = self.head
        if p:
            while p.next:
                s += str(p.key) +", "
                p = p.next
            s += str(p.key) +"]"
            return s

    def __init__(self,head=None):
        self.head = head

    def insert(self,key):
        """Adds node to the back of linked list."""
        node = Node(key)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def push_front(self,key):
        """Adds node to the front of linked list."""
        node = Node(key)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop_front(self):
        """Removes and returns the first node in linked list."""
        if self.head:
            temp = self.head
            self.head.next = temp.next
            return temp

    def pop_back(self):
        """Removes and returns the last node."""
        if self.head:
            curr = self.head
            while curr.next and curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
            return temp
