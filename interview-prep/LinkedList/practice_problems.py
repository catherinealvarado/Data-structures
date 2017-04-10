#PROBLEMS FROM LEETCODE AND CRACKING THE CODING INTERVIEW
#I am extending the SinglyLinkedList class
import singlyLinked

class SinglyLinkedList(singlyLinked.SinglyLinkedList):

    def remove_dups1(self): #Can use extra space
        #remove duplicates from unsorted linked list
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

    def remove_dups2(self): #Cannot use extra space
        #remove duplicates from unsorted linked list
        curr = self.head
        second = self.head
        while curr:
            while second.next:
                if curr.key != second.next.key:
                    second = second.next
                else:
                    second.next = second.next.next
            curr = second = curr.next

    def kth_last(self,k): #find the kth last element
        ###continue by answering this question!!!


linkedlst = SinglyLinkedList()
linkedlst.push_back(1)
linkedlst.push_back(2)
linkedlst.push_back(2)
linkedlst.push_back(2)
linkedlst.push_back(3)
linkedlst.push_back(1)
print(linkedlst.__str__()) #[1,2,3]
linkedlst.remove_dups2()
print(linkedlst.__str__())
