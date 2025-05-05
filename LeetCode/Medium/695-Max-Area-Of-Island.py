class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Similaar approach to number of Islands problem, 
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

        
        