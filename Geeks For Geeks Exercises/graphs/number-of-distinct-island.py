'''
Given a boolean 2D matrix grid of size n * m. You have to find the number of distinct islands where a group of connected 1s
 (horizontally or vertically) forms an island.

Two islands are considered to be distinct if and only if one island is not equal to another (not rotated or reflected).
'''

import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        ans = set()
        positions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        
        
        def dfs(row, col, temp, row0, col0):
            visited.add((row, col))
            temp.append((row - row0, col - col0))
            
            
            for dr, dc in positions:
                nRow, nCol = row + dr, col + dc
                if (nRow >= 0 and nRow < ROWS and nCol >= 0 and nCol < COLS
                    and (nRow, nCol) not in visited and grid[nRow][nCol] == 1):
                        dfs(nRow, nCol, temp, row0, col0)
                
                        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    temp = []
                    dfs(r, c, temp, r, c)
                    ans.add(tuple(temp))
                
                
        return len(ans)