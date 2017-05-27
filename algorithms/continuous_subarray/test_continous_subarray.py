import unittest
from subarray_continuous import maximum_sum_subarray

class ContinousSubarrayTests(unittest.TestCase):
    def test_empty_list(self):
        '''An empty list should return a 0 as maximum sum.'''
        self.assertEqual(maximum_sum_subarray([]), 0)

    def test_all_negatives_list(self):
        '''A list with all negatives should return 0.'''
        self.assertEqual(maximum_sum_subarray([-9,-3,-12,-8]), 0)

    def test_one_positive(self):
        '''List with one positive and all negatives returns that positive.'''
        self.assertEqual(maximum_sum_subarray([-2,-6,1,-9]),1)

    def test_all_positives(self):
        '''List with all positives should return sum of entire list.'''
        self.assertEqual(maximum_sum_subarray([1,2,4,9,3]), 19)

    def test_general(self):
        self.assertEqual(maximum_sum_subarray([-10,5,-2,3,-6]), 6)

if __name__ == '__main__':
    unittest.main()
