'''
Given an array arr and target sum k, check whether there exists a subsequence such that the sum of all
 elements in the subsequence equals the given target sum(k).

Example:

Input:  arr = [10,1,2,7,6,1,5], k = 8.
Output:  Yes
Explanation:  Subsequences like [2, 6], [1, 7] sum upto 8

Input:  arr = [2,3,5,7,9], k = 100. 
Output:  No
Explanation:  No subsequence can sum upto 100

Your Task:
You don't need to read or print anything. Your task is to complete the boolean function checkSubsequenceSum() which takes N, 
arr and K as input parameter and returns true/false based on the whether any subsequence with sum K could be found.


Expected Time Complexity: O(N * K).
Expected Auxiliary Space: O(N * K).

'''

class Solution:
    def checkSubsequenceSum(self, N, arr, K):
        # Uses recursive backracking to include and exclude element
        # no memoization or DP optimization here, so I get a TLE on Geeks for Geeks code editor
        # TC: O(2^N), SC: O(N)
        def check(indx, temp, total):
            if indx == N:
                if total == K:
                    return True
                return False
            temp.append(arr[indx])
            total += arr[indx]
            if check(indx+1, temp, total) == True:
                return True
            
            temp.pop()
            total -= arr[indx]
            if check(indx+1, temp, total) == True:
                return True
            return False
            
        return check(0, [], 0)
