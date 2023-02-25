'''Write a Python program to locate the left insertion point for a specified value in
sorted order.'''

import bisect

#bisect works only on sorted array
#performs binary search for the position where element 'x' should be inserted to the list 'a'

def index(a,x):
    #bisect_left performs search to find index of the leftmost occurence of 'x' in the list 'a'
    i = bisect.bisect_left(a,x)
    return i

a = [1,2,4,5,6]
print(index(a,7))
print(index(a,4))
print(index(a,3))
print(index(a,4))

#y o/p are :
# 5
# 2
# 2
# 2