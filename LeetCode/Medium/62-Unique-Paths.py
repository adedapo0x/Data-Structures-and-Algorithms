class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        dp memoization approach, where we store any overlapping problem
        we start the dp from the target, all the way up to the start of the grid, when one of the recursions get to the start, we return 1, 
        as that is a unique path, we have another check to keep the search space within the grid, once either the row index or the col index is
        beyond range, we want to return, we return 0 here as it has no effect on our count and the return stops the recursion from continuing
        down that path

        TC: O(m.n) since we no longer have to do repeated computations
        SC: O(path + M*N) where path is (m - 1) + (n - 1) that is going from end of grid to start, and the M*N is as a result of the dp grid 
        we use for memoization
        '''
        dp = [[-1] * n for _ in range(m)]
        def countUnique(m, n):
            if m == 0 and n == 0:
                return 1
            if m < 0 or n < 0:
                return 0

            if dp[m][n] != -1:
                return dp[m][n]

            up = countUnique(m - 1, n)
            left = countUnique(m, n - 1)

            dp[m][n] = up + left
            return up + left

        return countUnique(m - 1, n - 1)

        