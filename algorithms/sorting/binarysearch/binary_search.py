'''
Different functions that use binary search or modified
binary search.
'''

def median_sorted_lst(lst1,lst2):
    '''
    This recursive algorithms finds the median of two sorted arrays
    where the length of both arrays is n.
    Overview of how algorithm works:
    lst1 = [a1,a2,m1,a3,a4]
    lst2 = [b1,b2,m2,b3,b4]
    Base Cases:
    if n == 2:
        lst11 = [a2,m1] lst2 = [b2,m2]
        Return max(a2,b2) + min(m1,m2)
    if m1 == m2:
        Return m1
    (also base case for n == 1)
    If length of n is greater that 2 then we fo follow the following:
    casses - remember that we have two sorted lists:
    m1 < m2:
        {a1,a2,some bs},m1,{...},m2,{b3,b4,some as}
        Can get rid of a1, a2, b3, b4 for sure and continue algorithm.
    m1 > m2:
        {b1,b2, some as},m2,{...},m1,{a3,a4,some bs}
        Can get rid of b1,b2,a3,a4 for sure and continue algorithm.
    '''
    n = len(lst1)
    if not lst1:
        return 0
    if n == 1:
        return (lst1[0] + lst2[0])/2
    if n == 2:
        return (max(lst1[0],lst2[0])+min(lst1[1],lst2[1]))/2
    s1 = 0
    e1 = n
    s2 = 0
    e2 = n
    mid1 = (e1 - s1) // 2
    mid2 = (e2 - s2) // 2
    if lst1[mid1] == lst2[mid2]:
        return lst1[mid1]
    elif lst1[mid1] < lst2[mid2]:
        return median_sorted_lst(lst1[mid1:],lst2[:mid2+1])
    else:
        return median_sorted_lst(lst1[:mid1+1], lst2[mid2:])

print(median_sorted_lst([],[2]))
