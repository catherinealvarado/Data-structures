
class Node:
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next

    def __str__(self):
        return str(self.key)

class SinglyLinkedList:
    def __init__(self,head=None):
        self.length = 0
        self.head = head

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
            self.head = new_node
        else:
            self.head = new_node

    #returns the front item
    def topFront(self):
        return self.head

    #removes the front item
    def popFront(self):
        if self.head != None:
            self.length -= 1
            self.head = self.head.next

    #add to the back of linked list
    def pushBack(self,key):
        self.length += 1
        new_node = Node(key)
        if self.head != None:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            curr_node.next = new_node
        else:
            self.head = new_node

    #return back item
    def topBack(self):
        if self.head != None:
            curr_node = self.head
            while curr_node.next != None:
                curr_node = curr_node.next
            return curr_node
        else:
            return "Error"

    #remove back item
    def popBack(self):
        if self.head != None:
            self.length -= 1
            f_node = self.head
            s_node = f_node.next
            while s_node.next != None:
                f_node = s_node
                s_node = f_node.next
            f_node.next = None
        else:
            return "Error"

    #find key in linkedlist
    def find(self,key):
        if self.head != None:
            curr_node = self.head
            while curr_node != None:
                if curr_node.key == key:
                    return True
                else:
                    curr_node = curr_node.next
            return False
        else:
            return False

    #remove a key from list
    def erase(self,key):
        if self.head != None:
            curr_node = self.head
            if curr_node.key == key:
                self.length -= 1
                self.head = curr_node.next
            else:
                while curr_node != None:
                    next_node = curr_node.next
                    if next_node.key == key:
                        self.length -= 1
                        curr_node.next = next_node.next
                        break
                    else:
                        curr_node = next_node

    def empty(self):
        if self.length == 0:
            return True
        else:
            return False

    #add node before key
    def addBefore(self,beforekey,key):
        new_node = Node(key)
        if self.head != None:
            if self.head.key == beforekey:
                self.length +=  1
                new_node.next = self.head
                self.head = new_node
            else:
                curr_node = self.head
                while curr_node != None:
                    if curr_node.next.key == beforekey:
                        self.length +=  1
                        new_node.next = curr_node.next
                        curr_node.next = new_node
                        break
                    else:
                        curr_node = curr_node.next

    #add node after key
    def addAfter(self,afterkey,key):
        new_node = Node(key)
        if self.head != None:
            curr_node = self.head
            while curr_node != None:
                if curr_node.key == afterkey:
                    self.length += 1
                    new_node.next = curr_node.next
                    curr_node.next = new_node
                    break
                else:
                    curr_node = curr_node.next


link = SinglyLinkedList()
link.pushBack("FirstPanda")
link.pushBack("SecondPanda")
link.pushBack("ThirdPanda")
link.pushBack("FourthPanda")
print(link.__str__())


link.addAfter("FourthPanda","FifthPanda")
link.addBefore("FifthPanda","FourthPanda")
print(link.__str__())
