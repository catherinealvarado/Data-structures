#Simple implementation of a queue
#FIFO
class Queue:
    class Node:
        def __init__(self,key=None,next=None):
            self.key = key
            self.next = next

    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail

    def enqueue(self,key):
        #add element to qeueu - it goes to the back
        node = self.None(key)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        #remove and return first in (FIFO)
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
