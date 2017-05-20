import unittest
from quick_sort import sort

class QuickSortTests(unittest.TestCase):
    """
    These are several tests for the function sort that is an implementation
    of quick sort.
    """
    def test_empty_list(self):
        """Is an empty list sorted to an empty list?"""
        self.assertTrue(sort([])==[])

    def test_len_one_list(self):
        """Does a list of length one return itself?"""
        self.assertTrue(sort([2])==[2])

    def test_len_three_list(self):
        """List of length three is sorted correctly?"""
        self.assertTrue(sort([1,5,2])==[1,2,5])

    def test_len_four_list(self):
        """List of length four is sorted correctly?"""
        self.assertTrue(sort([9,8,7,6])==[6,7,8,9])

    def test_sorted_list(self):
        """A sorted list returns itself?"""
        self.assertTrue(sort([6,7,8,9])==[6,7,8,9])

    def test_general_one(self):
        """Check if [1,5,2,8,3] if sorted correctly."""
        self.assertTrue(sort([1,5,2,8,3])==[1,2,3,5,8])

    def test_general_two(self):
        """"Check if [19,10,2,6,1,9,3,8,4,4] if sorted correctly."""
        self.assertTrue(sort([19,10,2,6,1,9,3,8,4,4])==[1,2,3,4,4,6,8,9,10,19])


if __name__ == '__main__':
    unittest.main()
