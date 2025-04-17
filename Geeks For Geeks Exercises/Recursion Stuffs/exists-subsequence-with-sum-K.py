

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
