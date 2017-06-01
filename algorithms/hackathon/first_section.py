'''
This file contains problems from LeetCode that I have already solved.
I am doing a self hackathon where I answer as many questions as
possible within two hours.
(There are the current most popular questions on Leetcode.)
'''

'''
1: Two Sum -
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
        if val in diff_dic:
            return [diff_dic[val],ind]
        else:
            diff_dic[sum_tot-val] = ind

'''
292: Nim Game -
Given number of stones determine whether you will win the game
I can remove 1,2,3
example: 4 I will lose

3 <= 3 I win
4 - - - - No win
5 - - - - - Yes win
6 - - - - - - Yes win
7 - - - - - - - Yes
8 - - - - - - - - N
'''

'''
344: Reverse a string -
Takes a string as a input and reverses the string.
'''
def rev_string(s):
    rev = [list(word) for word in s.split(' ')]
    for i in range(len(rev)):
        curr = rev[i]
        n = len(curr)
        for j in range(n//2):
            temp = curr[j]
            curr[j] = curr[n-1-j]
            curr[n-1-j] = temp
        rev[i] = ''.join(rev[i])
    return ' '.join(rev)

'''
136: Single number -
Given an array of integers, every element appears twice except for one.
Find that single one.
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
[1,2,3,3,2,4,5,7,4,5,7]
'''
def single_number(lst):
    curr = lst[0]
    for i in range(1,len(lst)):
        curr = curr ^ lst[i]
    return curr
print(single_number([1,2,3,3,2,4,5,7,4,5,7]))

'''
2: Add two numbers -
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order and each of their nodes
contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except
the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
'''
