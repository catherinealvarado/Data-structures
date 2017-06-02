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


--- if youre a multiple of 4 you are guaranteed to win
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
[1,2,3,3,2,4,5,7,4,5,7] (we can use ^)
'''
def single_number(lst):
    curr = lst[0]
    for i in range(1,len(lst)):
        curr = curr ^ lst[i]
    return curr

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
class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None

def add_linked_lists(l1,l2):
    carry = 0
    dummy = Node("dummy")
    prev = dummy
    while l1 or l2:
        curr_sum = 0
        curr_sum += carry
        if l1:
            curr_sum += l1.val
            l1 = l1.next
        if l2:
            curr_sum += l2.val
            l2 = l2.next
        new_val = Node(curr_sum % 10)
        carry = curr_sum // 10
        prev.next = new_val
        prev = new_val
    if carry == 1:
        prev.next = ListNode(1)
    return dummy.next

'''
198: House Robber -
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight without
alerting the police.
[10,2,13,1,61,1] max_amount = 84
[20,1,1,20] max_amount = 40
'''
def house_robber(lst):
    n = len(lst)
    if not lst:
        return 0
    if n == 1:
        return lst[0]
    prev_prev = lst[0]
    prev = max(prev_prev,lst[1])
    for i in range(2,len(lst)):
        temp = prev_prev + lst[i]
        prev_prev = prev
        prev = max(prev_prev,temp)
    return prev

'''
219: Contains Duplicate II -
Given an array of integers and an integer k, find out whether there are two
distinct indices i and j in the array such that nums[i] = nums[j] and the
absolute difference between i and j is at most k.
[1,2,3,9,5,2] k = 3  {1,2,3,9}
'''
def contains_duplicate(lst,k):
    if k <= 0:
        return False
    curr_nums = set()
    for i in range(len(lst)):
        if i > k:
            curr_nums.remove(lst[i-k-1])
        if lst[i] in curr_nums:
            return True
        else:
            curr_nums.add(lst[i])
    return False

'''
108: Convert Sorted Array to Binary Search Tree -
Given an array where elements are sorted in ascending order, convert it
to a height balanced BST.
[1,2,3,4,5,6,7,8]

'''
class TreeNode:
    def __init__(self,val=None):
        self.val =  val
        self.left = None
        self.right = None

def sorted_arr_bin_search(lst):
    if not lst:
        return None
    mid = len(lst)//2
    root = TreeNode(lst[mid])
    root.left = sorted_arr_bin_search(lst[:mid])
    root.right = sorted_arr_bin_search(lst[mid:])
    return root

'''
202: Happy Number -
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with
any positive integer, replace the number by the sum of the squares of its
digits, and repeat the process until the number equals 1 (where it will
stay), or it loops endlessly in a cycle which does not include 1. Those
numbers for which this process ends in 1 are happy numbers.


19 {19}

sum = 9*9 + 1*1
19
'''
def find_squares_sum(n):
    curr_sum = 0
    while n:
        last = n % 10
        curr_sum += last*last
        n = n//10
    return curr_sum

def happy_number(num):
    vis_nums = set()
    while num:
        if num in vis_nums:
            return False
        if num == 1:
            return True
        vis_nums.add(num)
        num = find_squares_sum(num)
