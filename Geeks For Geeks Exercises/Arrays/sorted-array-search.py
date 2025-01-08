# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.


class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        for n in arr:
            if n == k:
                return True
            if n > k:
                break
        return False