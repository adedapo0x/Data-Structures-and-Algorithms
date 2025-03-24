'''
Given an unsorted array arr[] of integers and an integer x, find the floor and ceiling of x in arr[].

Floor of x is the largest element which is smaller than or equal to x. Floor of x doesn’t exist if x is smaller than smallest element of arr[].
Ceil of x is the smallest element which is greater than or equal to x. Ceil of x doesn’t exist if x is greater than greatest element of arr[].

Return an array of integers denoting the [floor, ceil]. Return -1 for floor or ceiling if the floor or ceiling is not present.
'''

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # done in a single pass, TC: O(N)
        res = []
        fl = -1
        ce = sys.maxsize
        
        for n in arr:
            if n <= x:
                fl = max(fl, n)
            if n >= x:
                ce = min(ce, n)
        res.append(fl)
        res.append(ce) if ce != sys.maxsize else res.append(-1)
        return res

        # for the two pass (one for ceil, other for floor)
        # TC: O(N) + O(N) = O(N)
        
        # for n in arr:
        #     if n <= x:
        #         fl = max(fl, n)
        # res.append(fl)
        
        # for n in arr:
        #     if n >= x:
        #         ce = min(ce, n)
        # res.append(ce) if ce != sys.maxsize else res.append(-1)
        # return res
            
