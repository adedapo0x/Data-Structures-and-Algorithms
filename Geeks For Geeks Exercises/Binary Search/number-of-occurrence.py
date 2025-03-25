'''
Given a sorted array, arr[] and a number target, you need to find the number of occurrences of target in arr[]. 
'''

class Solution:
    # The approach here is to use BS to find start and end of the occurence of the target, then minus the indexes + 1 to get the count
    # Similar approach in LC 34
    def countFreq(self, arr, target):
        #code here
        first = self.countOccurrence(arr, target, True)
        if first == -1:
            return 0
        second = self.countOccurrence(arr, target, False)
        return second - first + 1
    def countOccurrence(self, arr, target, bias):
        l, r = 0, len(arr) - 1
        indx = -1
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == target:
                indx = mid
                if bias:
                    r = mid - 1
                else:
                    l = mid + 1
            elif arr[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
                
        return indx