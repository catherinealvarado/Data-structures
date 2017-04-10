#Simple implementation of a heap
#Based on Cracking the Coding Interview and
#https://www.youtube.com/watch?v=t0Cq6tVNRBA
class Min_Heap:
    def __init__(self):
        #initializing the heap
        self.arr = []
        self.length = 0

    def __str__(self):
        #prints out the heap as an array
        print(self.arr)

    def get_left_child_index(self,index):
        #return the left child index of an index
        return (2 * index) + 1

    def get_right_child_index(self,index):
        #returns the right child index of an index
        return (2 * index) + 2

    def get_parent_index(self,index):
        #returns the parent index of an index
        return (index - 1) // 2

    def has_left_child(self,index):
        #returns True if an index has a right child, otherwise False
        return self.get_left_child_index(index) < self.length

    def has_right_child(self,index):
        #returns True if an index has a left child, otherwise False
        return self.get_right_child_index(index) < self.length

    def has_parent(self,index):
        #returns True if an index has a parent, otherwise False
        return self.get_parent_index(index) >= 0

    def left_child(self,index):
        #returns the value of the left child of index
        return self.arr[self.get_left_child_index(index)]

    def right_child(self,index):
        #returns the value of the right child of index
        return self.arr[self.get_right_child_index(index)]

    def parent(self,index):
        #returns the parent value of index
        return self.arr[self.get_parent_index(index)]

    def swap(self,ind1,ind2):
        #switches the values of two positions in the heap
        temp = self.arr[ind1]
        self.arr[ind1] = self.arr[ind2]
        self.arr[ind2] = temp

    def insert(self,val):
        #inserts a new value into the heap
        self.arr.append(val)
        self.length += 1
        self.heapify_up()

    def heapify_up(self):  #O(log n)
        #once a new value is inserted into the heap, we check all of its
        #parents to make sure that the heap maintains its min property
        curr_ind = self.length - 1
        val = self.arr[curr_ind]
        while self.has_parent(curr_ind) and self.parent(curr_ind) > val:
            parent_ind = self.get_parent_index(curr_ind)
            self.swap(parent_ind,curr_ind)
            curr_ind = parent_ind

    def peek(self):
        #returns the minimum element in the heap
        if self.arr:
            return self.arr[0]

    def remove_min(self):
        #removes the minimum element in the heap and heapfies down
        if self.arr:
            smallest = self.arr[0]
            self.arr[0] = self.arr[self.length - 1]
            self.length -= 1
            self.arr = self.arr[:-1]
            self.heapify_down()
            return smallest

    def heapify_down(self): #O(log n)
        #starts from the root of the heap and swaps values starting
        #from the root node to make sure it maintains its min structure
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
