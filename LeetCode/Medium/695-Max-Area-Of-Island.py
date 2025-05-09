class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Similar approach to number of Islands problem (LC 200), but here we are trying to get the area of each of the islands then find the maximum
        So here using a DFS, for each beginning of an island we encounter, we then count one for that island and try to fetch the nodes of all the other
        four directions recursively. 

        so after we are done with an island and it has returned the area, we compare it with our maxArea variable that we are using to keep the max of the areas found so far

        TC and SC: O(M * N), this can also be done with BFS, prolly do that some other time.
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        maxArea = 0 

        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == 0 or (row, col) in visited):
                return 0
            
            visited.add((row, col))

            return 1 + dfs(row -1, col) + dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea

        
        