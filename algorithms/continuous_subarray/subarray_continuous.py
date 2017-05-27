'''
Different functions that fall into continuous subarray kind
of problems.
'''

def maximum_sum_subarray(lst):
    ''''Returns the maximum positive sum of a continuous subarray. If
    all the numbers in lst are negative return 0.'''
    curr_max = 0
    global_max = 0
    for ind,value in enumerate(lst):
        curr_max += value
        if curr_max < 0:
            curr_max = 0
        global_max = max(global_max,curr_max)
    if global_max < 0:
        return 0
    else:
        return global_max
