#Basic implementation of a singly linked list
class SinglyLinkedList:
    #implementing a node class
    class Node:
        def __init__(self,key=None,next=None):
            self.key = key
            self.next = None

    def __str__(self):
        #prints out the linked list as a list
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

    def push_front(self,key):
        #add node to the front
        node = self.Node(key)
        if not self.head:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def push_back(self,key):
        #add node to the back
        node = self.Node(key)
        if not self.head:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def pop_front(self):
        #remove and return the first node
        if self.head:
            temp = self.head
            self.head.next = temp.next
            return temp

    def pop_back(self):
        #remove and return the last node
        if self.head:
            curr = self.head
            while curr.next and curr.next.next:
                curr = curr.next
            temp = curr.next
            curr.next = None
            return temp
