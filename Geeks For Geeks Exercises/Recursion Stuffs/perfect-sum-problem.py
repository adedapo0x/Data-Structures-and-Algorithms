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
    # There is a problem with this, works fine but I get TLE on GFG since TC here is o(2^n), and for large arrays this is a problem
    # There is a memoization solution (DP) that runs faster, but haven't learnt DP yet, so this stays here for now I suppose
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
	