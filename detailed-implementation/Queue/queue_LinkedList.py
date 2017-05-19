#this is the implementation of a queue with a Linked list
#FIFO - First-in First-out
class Node:
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next

class Queue:
    def __init__(self,head=None,tail=None):
        self.length = 0
        self.head = head
        self.tail = tail

    def __str__(self):
        s = "["
        p = self.head
        if p != None:
            while p.next != None:
                s += p.key +", "
                p = p.next
            s += p.key +"]"
            return s

    #adds key to collection
    def enqueue(self,key):
        self.length += 1
        new_node = Node(key)
        if self.head != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    #removes and returns least recently added key
    def dequeue(self):
        if self.length > 0:
            self.length -= 1
            first = self.head.key
            self.head = self.head.next
            return first
        else:
            return "ERROR: Empty linked list"

    #returns bool describing whether queue is empty 
    def empty(self):
        if self.head == None:
            return True
        else:
            return False
