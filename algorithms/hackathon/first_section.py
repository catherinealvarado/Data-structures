'''
This file contains problems from LeetCode that I have already solved.
I am doing a self hackathon where I answer as many questions as
possible within two hours.
(There are the current most popular questions on Leetcode.)
'''

'''
1: Two Sum:
Given an array of integers, return indices of the two numbers such that they
add up to a specific target.
Assumptions:
You may assume that each input would have exactly one solution, and you may
not use the same element twice.
[1,9,5,8] sum = 17 output = [1,3]
[1,5,4,6,5] sum = 10 output = [5,5]
'''
def two_sum(lst,sum_tot):
    diff_dic = {}
    for ind,val in enumerate(lst):
        diff = sum_tot - val
        if diff in diff_dic:
            return [diff_dic[diff],ind]
        else:
            diff_dic[diff] = ind
print(two_sum([1,5,4,6,5]))
