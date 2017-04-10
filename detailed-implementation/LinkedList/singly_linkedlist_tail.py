""" head and tail pointer for this implementation
PushFront(key) add to the front ||| O(1)
Key TopFront() return front item ||| O(1)
PopFront() remove the front item ||| O(1)
PushBack(key) add the back item ||| O(1)
PopBack() remove the back item ||| O(n)
Boolean Find(key) is key in list?
Erase(key) remove key from list
Boolean Empty() empty list?
AddBefore(Node,Key) adds key before node
AddAfter(Node,Key) adds key after node
"""

class Node:
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next

class SinglyLinkedList:
    def __init__(self,head=None,tail=None):
        self.head = head
        self.tail = tail
        self.length = 0

    def __str__(self):
        s = "["
        p = self.head
        if p != None:
            while p.next != None:
                s += p.key +", "
                p = p.next
            s += p.key +"]"
            return s

    def pushFront(self,key):
        new_node = Node(key)
        if self.head != None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def topFront(self):
        return self.head

    def popFront(self):
        if self.head != None:
            if self.length > 1:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            self.length -= 1
        else:
            return "Error"

    def pushBack(self,key):
        new_node = Node(key)
        if self.head != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def popBack(self):
        if self.head != None:
            if self.length > 1:
                curr_node = self.head
                while curr_node.next != self.tail:
                    curr_node = curr_node.next
                curr_node.next = None
                self.tail = curr_node
            else:
                self.head = None
                self.tail = None
            self.length -= 1
        else:
            return "Error"

    def findKey(self,key):
        if self.head != None:
            curr_node = self.head
            while curr_node != None:
                if (curr_node.key == key):
                    return True
                else:
                    curr_node = curr_node.next
            return False
        else:
            return False

    def eraseKey(self, key):
        if (self.head != None):
            if (self.length > 1):
                curr_node = self.head
                if (curr_node.key != key):
                    while (curr_node != self.tail and curr_node.next.key != key):
                        curr_node = curr_node.next
                    if (curr_node == self.tail):
                        return "Not here!"
                    if (curr_node.next == self.tail):
                        curr_node.next = None
                        self.tail = curr_node
                        self.length -= 1
                    else:
                        curr_node.next = curr_node.next.next
                        self.length -= 1
                else:
                    self.head = self.head.next
                    self.length -= 1
            else:
                if (self.head.key == key):
                    self.head = None
                    self.tail = None
                    self.length -= 1

    def empty(self):
        if self.length == 0:
            return True
        else:
            False

    def addBefore(self,key,newKey):
        new_node = Node(newKey)
        if self.head != None:
            curr_node = self.head
            if curr_node.key != key:
                while curr_node.next.key != key:
                    curr_node = curr_node.next
                if curr_node != self.tail:
                    new_node.next = curr_node.next
                    curr_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node

    def addAfter(self,key,newKey):
        new_node = Node(newKey)
        if self.head != None:
            curr_node  = self.head
            while curr_node.key != key:
                curr_node = curr_node.next
            if (curr_node == self.tail):
                if (curr_node.key == key):
                    curr_node.next = new_node
                    self.tail = new_node
                    self.length += 1
            else:
                new_node.next = curr_node.next
                curr_node.next = new_node
                self.length += 1



link = SinglyLinkedList()
link.pushBack("FirstPanda")
link.pushBack("SecondPanda")
link.pushBack("ThirdPanda")
link.pushBack("FourthPanda")
print(link.__str__())

link.addAfter("SecondPanda", "FifthPanda")
print(link.__str__())
