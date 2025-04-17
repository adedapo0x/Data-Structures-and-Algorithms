'''
 Perfect Sum Problem
Given an array arr of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

Examples:

Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
Output: 3
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.

Input: arr[] = [2, 5, 1, 4, 3], target = 10
Output: 3
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.

Input: arr[] = [5, 7, 8], target = 3
Output: 0
Explanation: There are no subsets of the array that sum up to the target 3.

'''

class Solution:
    # There is a problem with these two solutions below, same logic in both just different implementation, works fine but I get TLE on GFG since TC here is o(2^n), and for large arrays this is a problem
    # There is a memoization solution (DP) that runs faster, but haven't learnt DP yet, so this stays here for now I suppose
    
    def perfectSum(self, arr, target):
        return self.checkTotal(0, 0, arr, target)
    
    # This is the better version that does not use global variables. and gets rid of having to use the temp data structure, we simply just add and deduct from
    # total as we go
    def checkTotal(self, indx, total, arr, target):
        if total > target: # This is because once total exceeds target, adding anything more is obvs also going to exceed target
            return 0 # Note that this extra base case only holds if the arr elements are only positive values (no negative values)!
        if indx == len(arr):
            if total == target:
                return 1 # if condition match, return 1 that is there is a valid subsequence that sum equals target
            return 0 # return 0
            
        total += arr[indx]
        left = self.checkTotal(indx+1, total, arr, target)
        
        total -= arr[indx]
        right = self.checkTotal(indx+1, total, arr, target)
        
        return left + right # get for left, get for right,, add together, return sum
	


    # This was my naive solution kinda, apperently there is a better way to keep the count rather than using a global variable and without having to keep track of
    # the subset array since we are not storing or printing each subset

    def perfectSum(self, arr, target):
        self.count = 0

        def countSum(indx, temp, total):
            if indx == len(arr):
                if total == target:
                    self.count += 1
                return
                 
            temp.append(arr[indx])
            total += arr[indx]
            countSum(indx+1, temp, total)

            temp.pop()
            total -= arr[indx]
            countSum(indx+1, temp, total)
	   
        countSum(0, [], 0)
        return self.count
	