
#this is an implementation of a queue
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

    #are there any elements?
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

'''
This is an implementation of an arbitary tree.
The functions defined are:

add_node(key,children,parent) -> updates tree with a node
The function above adds a node to the tree. The name of the node is key, the
children is a list of the node's children, and the parent is parent.

add_child(node_name,child) -> adds child to existing node
The function above adds a child to the existing node. After the new child
is added to the node, it checks to see if child exists as a node. If the child
is not a node, then it adds this node to the tree.

update_parent(name,parent) -> changes the parent of a node.
Use the function above only for special cases. The function only changes the
name of the parent, but if you think about this further then changing the name
of the parent means that this node must already be a child of parent. The
function defined does not take that into account.

'''

#implementation of a tree
class Tree:
    def __init__(self,root=None,nodes={}):
        self.root = root
        self.nodes = nodes

    def __str__(self):
        return self.nodes

    #adds a new node to the tree
    def add_node(self,key,children,parent):
        if parent == None:
            self.root = key
        # if self.nodes.get(key) == None:
        self.nodes[key] = {"children": children, "parent": parent}
        for child in children:
            if self.nodes.get(child) == None:
                self.nodes[child] = {"children": [], "parent": key}

    #adds a child to existing node
    def add_child(self,node_name,child):
        if self.nodes.get(node_name) != None:
            self.nodes[node_name]["children"].append(child)
            if self.nodes.get(child) == None:
                tree.add_node(child,[],node_name)
        else:
            return "Error: Node does not exist"

    #adds or updates a parent of existing node
    def update_parent(self,name,parent):
        if self.nodes.get(name) != None:
            self.nodes[name]["parent"] = parent
        else:
            return "Error: Node does not exist"

    #returns the depth of a tree
    def depth(self):
        if self.root != None:
            queue = Queue()
            queue.enqueue(self.root)
            current_depth = 0
            left_till_increase_depth = 1
            future_till_increase_depth = 0
            while queue.empty() == False:
                name = queue.dequeue()
                left_till_increase_depth -= 1
                children = self.nodes[name]["children"]
                future_till_increase_depth += len(children)
                if left_till_increase_depth == 0:
                    current_depth += 1
                    left_till_increase_depth = future_till_increase_depth
                    future_till_increase_depth = 0
                for child in children:
                    queue.enqueue(child)
            return current_depth
        else:
            return 0
