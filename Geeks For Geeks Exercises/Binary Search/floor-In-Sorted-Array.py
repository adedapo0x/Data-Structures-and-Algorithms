'''
Given a sorted array arr[] and an integer x, find the index (0-based) of the largest element in arr[] that is less than or equal to x.
 This element is called the floor of x. If such an element does not exist, return -1.

Note: In case of multiple occurrences of ceil of x, return the index of the last occurrence.

'''

class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        # Optimal way is to use binary search since the array is sorted
        l, r = 0, len(arr) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] <= x:
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res
        

        # Bruteforce approach, using a linear search
        res = -1
        for i in range(len(arr)):
            if arr[i] <= x:
                res = i
            else:
                return res
        return res




        
