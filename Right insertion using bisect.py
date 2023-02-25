'''Write a Python program to locate the right insertion point for a specified value in sorted order.
'''

import bisect
def indexing(a,x):
    i = bisect.bisect_right(a,x)
    return i

a = [1,2,4,7]
print(indexing(a,6))
print(indexing(a,5))
print(indexing(a,3))