#Stacks are also known as LIFO queues (Last In First Out)

#here implement a stack using LinkedList
#i am using a tail pointer to indicate oldest element added
class Node():
    def __init__(self,key=None,next=None):
        self.key = key
        self.next = next

class StackLinkedList():
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

    #add element to stack
    def push(self,key):
        self.length += 1
        new_node = Node(key)
        if self.head != None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

    #return recently added key
    def top(self):
        if self.head != None:
            return self.head.key
        else:
            return "ERROR: Stack is empty"

    #return and remove recently added element
    def pop(self):
        if self.head != None:
            self.length -= 1
            last = self.head.key
            self.head = self.head.next
            return last
        else:
            return "ERROR: Stack is empty"

    #is the stack empty?
    def empty(self):
        if self.length == 0:
            return True
        else:
            return False

# stack = StackLinkedList()
# stack.push("Jeffrey")
# stack.push("Catherine")
# stack.push("Jennifer")
# print(stack.__str__())
# print(stack.tail.key)

# print(stack.pop())
# print(stack.__str__())
# print(stack.empty())
