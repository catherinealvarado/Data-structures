#when return the front or back item might want to return a key!!!!!!!!!!!!

class Node:
    def __init__(self,key=None,next=None,prev=None):
        self.key = key
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.key)

#how do i keep account of the tail???
class DoublyLinkedList:
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

    #adds to the front
    def pushFront(self,key):
        self.length += 1
        new_node = Node(key)
        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    #returns the front item
    def topFront(self):
        return self.head

    #removes the front item
    def popFront(self):
        if self.head != None:
            self.length -= 1
            if self.length != 1:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
        return "Error"

    #add to the back of linked list
    def pushBack(self,key):
        self.length += 1
        new_node = Node(key)
        if self.head != None:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    #return back item
    def topBack(self):
        return self.tail

    #remove back item
    def popBack(self):
        if self.head != None:
            self.length -= 1
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            return "ERROR"

    #find key in linkedlist
    def find(self,key):
        if self.head != None:
            curr = self.head
            while curr != None:
                if curr.key == key:
                    return True
                else:
                    curr = curr.next
            return False
        else:
            return False

    #remove a node from list
    def erase(self,key):
        curr = self.head
        if curr != None:
            if curr.key == key:
                self.length -= 1
                curr.next.prev = None
                self.head = curr.next
            elif self.tail.key == key:
                self.length -= 1
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                while curr != None:
                    if curr.key == key:
                        self.length -= 1
                        curr.prev.next = curr.next
                        curr.next.prev = curr.prev
                        break
                    else:
                        curr = curr.next

    def empty(self):
        if self.length == 0:
            return True
        else:
            return False

    #add node before key
    def addBefore(self,beforekey,key):
        new_node = Node(key)
        curr = self.head
        if curr != None:
            if curr.key == beforekey:
                self.length += 1
                self.head.prev = new_node
                new_node.next = self.head
                self.head = new_node
            else:
                curr = curr.next
                while curr != None:
                    if curr.key == beforekey:
                        self.length += 1
                        new_node.prev = curr.prev
                        curr.prev.next = new_node
                        curr.prev = new_node
                        new_node.next = curr
                        break
                    else:
                        curr = curr.next

    #add node after key
    def addAfter(self,afterkey,key):
        new_node = Node(key)
        curr = self.head
        if curr != None:
            print(self.tail)
            if self.tail.key == afterkey:
                self.length += 1
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
            else:
                while curr != None:
                    if curr.key == afterkey:
                        self.length += 1
                        new_node.prev = curr
                        new_node.next = curr.next
                        curr.next.prev = new_node
                        curr.next = new_node
                        break
                    else:
                        curr = curr.next





link = DoublyLinkedList()
link.pushBack("One")
link.pushBack("Two")
link.pushBack("Three")
print(link.__str__())
#
link.addAfter("One","Four")
print(link.__str__())
