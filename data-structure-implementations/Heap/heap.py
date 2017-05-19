class Min_Heap:
    """
    Implementation if a min_heap. This could also be turned
    to a max heap if all numbers added that are positive
    are turned to a negative numbers and all negative numbers
    that are added are turned to positive numbers.
    """

    def __init__(self):
        self.arr = []
        self.length = 0

    def __str__(self):
        """Prints out the heap as an array."""
        print(self.arr)

    def get_left_child_index(self,index):
        """Return the left child index of given index."""
        return (2 * index) + 1

    def get_right_child_index(self,index):
        """Returns the right child index of given index."""
        return (2 * index) + 2

    def get_parent_index(self,index):
        """Returns the parent index of given index."""
        return (index - 1) // 2

    def has_left_child(self,index):
        """Returns True if an index has a right child, otherwise False."""
        return self.get_left_child_index(index) < self.length

    def has_right_child(self,index):
        """Returns True if an index has a left child, otherwise False."""
        return self.get_right_child_index(index) < self.length

    def has_parent(self,index):
        """Returns True if an index has a parent, otherwise False."""
        return self.get_parent_index(index) >= 0

    def left_child(self,index):
        """Returns the value of the left child of index."""
        return self.arr[self.get_left_child_index(index)]

    def right_child(self,index):
        """Returns the value of the right child of index"""
        return self.arr[self.get_right_child_index(index)]

    def parent(self,index):
        """Returns the value of the parent of an index."""
        return self.arr[self.get_parent_index(index)]

    def swap(self,ind1,ind2):
        """
        Swaps the values at the positions ind1 and ind2 of the heap.
        """
        temp = self.arr[ind1]
        self.arr[ind1] = self.arr[ind2]
        self.arr[ind2] = temp

    def insert(self,val):
        """Inserts a new value into the heap."""
        self.arr.append(val)
        self.length += 1
        self.heapify_up()

    def heapify_up(self):  #O(log n)
        """
        When a new value is inserted into the heap, we check all of its
        parents to make sure that the heap maintains its min property. If
        any parent is bigger than its child, then the parent and child swap.
        """
        curr_ind = self.length - 1
        val = self.arr[curr_ind]
        while self.has_parent(curr_ind) and self.parent(curr_ind) > val:
            parent_ind = self.get_parent_index(curr_ind)
            self.swap(parent_ind,curr_ind)
            curr_ind = parent_ind

    def peek(self):
        """
        Looks at the first element in the heap, which is the minumum
        element in the heap.
        """
        if self.arr:
            return self.arr[0]

    def remove_min(self):
        """Removes the minimum element in the heap and heapfies down."""
        if self.arr:
            smallest = self.arr[0]
            self.arr[0] = self.arr[self.length - 1]
            self.length -= 1
            self.arr = self.arr[:-1]
            self.heapify_down()
            return smallest

    def heapify_down(self): #O(log n)
        """
        This is called when the first element in the heap is removed. Once
        a minimum element is removed the heap needs to find the next minimum
        element in the heap. It starts searching from the root of the heap
        and swaps values until the min is found. This needs to be done to
        the min heap.
        """
        curr_ind = 0
        while self.has_left_child(curr_ind):
            smaller_child_index = self.get_left_child_index(curr_ind)
            if self.has_right_child(curr_ind) and self.right_child(curr_ind) < self.left_child(curr_ind):
                smaller_child_index = self.get_right_child_index(curr_ind)
            if self.arr[smaller_child_index] < self.arr[curr_ind]:
                self.swap(curr_ind,smaller_child_index)
                curr_ind = smaller_child_index
            else:
                break

#Example of how to use heap:
# heap = Min_Heap()
# heap.insert(4)
# heap.insert(50)
# heap.insert(7)
# heap.insert(55)
# heap.insert(90)
# heap.insert(87)
# heap.__str__()
# heap.insert(2)
# heap.__str__()
