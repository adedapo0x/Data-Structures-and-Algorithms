'''
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land).
Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally
or vertically or diagonally i.e., in all 8 directions.

Personal note: difference with this and this question on LC is that here we are checking diagonal position too, so in this solution we use loops 
to cover all 8 positions unlike in the LC solution where we have just 4 positions in a list since we are checking just horizontal and vertical
'''

class Solution:
    def numIslands(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islands = 0
        
        def dfs(row, col):
            if (row < 0 or row >= ROWS or col < 0 or col >= COLS or
            grid[row][col] == "W" or (row, col) in visited):
                return
            
            visited.add((row, col))
            
            for r in range(-1, 2):
                for c in range(-1, 2):
                    dfs(row + r, col + c)
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "L" and (row, col) not in visited:
                    islands += 1
                    dfs(row, col)
                    
        return islands

