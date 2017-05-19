class Node:
    """
    Simple implementation of a node class.
    """
    def __init__(self,key=None):
        self.key = key
        self.next = None

class Stack(object):
    """
    Implementation of a stack that follows LIFO
    (Last In Last Out).
    """
    def __init__(self,head=None,tail=None):
        self.head = head

    def push(self,key):
        """
        Push a key to the stack.
        Running time: O(1)
        """
        new_node = Node(key)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            self.head = new_node
            new_node.next = temp

    def pop(self):
        """
        Removes the last element of the stack and returns it.
        Running time: O(1)
        """
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
