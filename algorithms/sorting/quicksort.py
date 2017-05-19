"""
Recursive implementation of quick sort algorithm.
Best Running Time: O(nlog(n))
Worst Running Time: O(n^2)
Space: O(1)
"""

def partition(arr,left,right,pivot):
    while left < right:
        while arr[left] < arr[pivot]:
            left += 1
        while arr[right] > arr[pivot]:
            right -=1
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
    return left

def quick_sort(arr,left,right):
    if left >= right:
        return
    pivot = (left + right) // 2
    ind = partition(arr,left,right,pivot)
    quick_sort(arr, left, ind)
    quick_sort(arr, ind+1, right)

def sort(arr):
    quick_sort(arr,0,len(arr)-1)
    return arr

print(sort([2,4,3]))
