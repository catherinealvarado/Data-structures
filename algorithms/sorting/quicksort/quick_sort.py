"""
Recursive implementation of quick sort algorithm.
Best Running Time: O(nlog(n))
Worst Running Time: O(n^2)
Space: O(1)
"""

def partition(arr,left,right,pivot):
    """
    All of the numbers to the left of the pivot index that are greater than
    the pivot are swaped with numbers on the right side of the pivot that are
    smaller than the pivot.
    Returns the left index once the left index is no longer smaller than
    the right index.
    """
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
    """Sorts the input array in place recursively."""
    if left >= right:
        return
    pivot = (left + right) // 2
    ind = partition(arr,left,right,pivot)
    quick_sort(arr, left, ind)
    quick_sort(arr, ind+1, right)

def sort(arr):
    """Sorts and returns the array."""
    quick_sort(arr,0,len(arr)-1)
    return arr
