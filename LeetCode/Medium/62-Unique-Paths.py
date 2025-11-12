class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        '''
        This is the tabulation method of doing this. we intialize our 2D DP grid used to store results of previously overlapping subproblem with 1
        because there is only one way to go from one place to that same place. 

        we start our iteration of the cols and rows from 1 up until m and n because the positions at row 0 and col 0 do not have any previous position for 
        someone to come from. so in order not to get index errors or have to explicitly check if in range, we start row and col from 1

        so for each row and col we want to find how many ways to get there, in order to get that, we need to find how many ways to get to what is on top of it
        and what is by the left of it so we can sum them up, since the question states that the only way to go to a position is to go down or right

        we then return dp[m-1][n-1] as this would contain the number of ways to get there built from the sum of the previous positions

        TC: O(M*N), SC: O(M *N) we get rid of the recursive stack space here
        '''

        dp = [[1] * n for _ in range(m)]

        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m - 1][n - 1]
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
    

        # still exactly same memoization approach, only now I am going as the question described from (0,0) to target not in reverse order
        # still same TC and SC
        dp = [[-1] * n for _ in range(m)]
        def countUnique(r, c):
            if r == m - 1 and c == n - 1:
                return 1
            if r >= m or c >= n:
                return 0

            if dp[r][c] != -1:
                return dp[r][c]

            right = countUnique(r, c + 1)
            down = countUnique(r + 1, c)

            dp[r][c] = right + down
            return right + down

        return countUnique(0, 0)

    

    '''
    Bruteforce approach, at every position, we go both up and left, we do it in reverse of how the question stated it since we are moving from the target to start
    and not from start to target as the question described
    '''
    def uniquePaths(self, m: int, n: int) -> int:
        
        def countUnique(m, n):
            if m == 0 and n == 0:
                return 1
            if m < 0 or n < 0:
                return 0

            up = countUnique(m - 1, n)
            left = countUnique(m, n - 1)

            return up + left

        return countUnique(m - 1, n - 1)

        