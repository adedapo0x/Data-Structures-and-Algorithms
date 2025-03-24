'''
Problem statement
You're given a sorted array 'a' of 'n' integers and an integer 'x'.

Find the floor and ceiling of 'x' in 'a[0..n-1]'.

Note:
Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.
'''

def getFloorAndCeil(a, n, x):
    
    # logic to read from standard input, found out it wasn't necessary 
    # import sys 
    # input = sys.stdin.readline
    # n, x = map(int, input().split())
    # a = list(map(int, input().split()))

    l, r = 0, n - 1
    ce = fl = -1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x: # if the target x, exists, it'll be the floor and ceil
            ce = fl = a[mid]
            return [fl, ce]
        elif a[mid] < x:
            fl = a[mid]
            l = mid + 1
        else:
            ce = a[mid]
            r = mid - 1

    return [fl, ce]

            
