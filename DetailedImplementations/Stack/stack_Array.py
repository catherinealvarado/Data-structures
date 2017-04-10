#implementing a stack using array
class StackArray():
    def __init__(self,items=[]):
        self.items = items
        self.length = 0

    def __str__(self):
        return self.items

    #add element to stack
    def push(self,item):
        self.length += 1
        self.items.append(item)

    #returns most recently added key
    def top(self):
        if self.length > 0:
            return self.items[-1]
        else:
            return "ERROR: Stack is empty"

    #return and remove recently added element
    def pop(self):
        if self.length > 0:
            self.length -= 1
            last = self.items[-1]
            self.items = self.items[:-1]
            return last
        else:
            return "ERROR: Stack is empty"

    #is the stack empty?
    def empty(self):
        if self.items == 0:
            return True
        else:
            return False



stack = StackArray()
stack.push("Jeffrey")
stack.push("Catherine")
stack.push("Jennifer")
stack.push("Jason")
print(stack.__str__())
# print(stack.top())

stack.pop()
print(stack.__str__())
stack.pop()
print(stack.__str__())
stack.pop()
print(stack.__str__())
stack.pop()
print(stack.__str__())
stack.pop()
print(stack.__str__())
