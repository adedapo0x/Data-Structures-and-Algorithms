# Given an array of positive integers arr[], return the second largest element from the array. 
# If the second largest element doesn't exist then return -1.

# Note: The second largest element should not be equal to the largest element.

# Examples:

# Input: arr[] = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.


# Brute force solution
# Time complexity: O(nlogn) + O(n) = O(nlogn)

class Solution:
    def getSecondLargest(self, arr):
        arr.sort()
        
        largest = arr[-1]
        
        for i in range(len(arr) - 1, -1, -1):
            if arr[i] != largest:
                return arr[i]
        return -1
    

# Better solution
# Time complexity: O(n) + O(n) = O(2n) = O(n)

class Solution:
    def getSecondLargest(self, arr):
        
        largest = sLargest = 0
        
        # gets largest in the array
        for n in arr:
            if n > largest:
                largest = n
                
        # to check for second largest
        for n in arr:
            if n > sLargest and n < largest:
                sLargest = n
                
        if sLargest == 0:
            return -1
        else:
            return sLargest
        
        # cleaner way of writing this same 2 pass approach is:
        second = -1
        first = max(arr)
        
        for num in arr:
            if num > second and num < first:
                second = num
                
        return second
        
        
    
# Optimal solution
# Solution above is O(N) but takes two passes, there is better solution with just one pass
# The optimal solution here takes O(N) in one pass

class Solution:
    def getSecondLargest(self, arr):
        
        # we could have also just initially set both to -1, so there would be no need for the check after the loop, we can just return direct
        largest = sLargest = 0

        
        for n in arr:
            if n > largest:
                sLargest = largest
                largest = n
            elif n > sLargest and n != largest:
                sLargest = n
                
        if sLargest == 0:
            return -1 
        else:
            return sLargest
