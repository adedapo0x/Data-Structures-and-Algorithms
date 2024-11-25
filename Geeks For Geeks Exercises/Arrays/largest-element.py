# Given an array arr[]. The task is to find the largest element and return it.

from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        biggest = arr[0]
        
        for i in range(1, len(arr)):
            biggest = max(biggest, arr[i])
            
        return biggest
            