import singlyLinked

class LinkedListFunctions(singlyLinked.LinkedList):
    """
    Additional singly linked list advanced functions.
    """
    def remove_dups1(self):
        """
        Removes duplicates from unsorted linked list. Additional
        space is allowed.
        Running time: O(n) Space: O(n)
        """
        if self.head:
            vis = set()
            vis.add(self.head.key)
            curr = self.head
            while curr.next:
                if curr.next.key in vis:
                    curr.next = curr.next.next
                else:
                    vis.add(curr.next.key)
                    curr = curr.next

    def remove_dups2(self):
        """
        Removes duplicates from unsorted linked list. Additional space
        is not allowed.
        Running time: O(n^2) Space: O(1)
        """
        curr = self.head
        runner = self.head
        while curr:
            while runner.next:
                if curr.key != runner.next.key:
                    runner = runner.next
                else:
                    runner.next = runner.next.next
            curr = curr.next
            runner = curr
            # curr = runner = curr.next

    # def kth_last(self,k): #find the kth last element
        ###continue by answering this question!!!


linkedlst = LinkedListFunctions()
linkedlst.insert(1)
linkedlst.insert(2)
linkedlst.insert(2)
linkedlst.insert(2)
linkedlst.insert(3)
linkedlst.insert(1)
print(linkedlst.__str__()) #[1,2,3]
linkedlst.remove_dups2()
print(linkedlst.__str__())
