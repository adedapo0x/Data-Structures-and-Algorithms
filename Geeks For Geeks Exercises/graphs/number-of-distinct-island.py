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
        '''
        This is an extension of the Number of Islands problem. Here, the approach is very similar to what we do in the Number of Islands problem.
        But here, for each islands we come across we need a way to store the shape of how the islands look like, if we decide to just store the indexes of
        the islands we come across, when we come across one of same shape, even though they have the same shape, we won't be able to recognize since they will
        obvs have different indexes

        So the best way to go about storing the distinct shapes is to use the first index of the island as a base, so we subtract every other land index positions that make up
        the island from the first land index, we find out that for similar shape islands we get the same indexes. So these subtracted indexes for a particular island
        is stored in a list as we go through the island. After we are done, with the islands, we store the list in a set cos it filters the duplicates out (in
        actuality, we add the tuple of the list elements to the set, since lists as itself cannot be hashed)

        Then after everything, we can simply return the length of the set as that would contain the distinct tuples that represents the islands.
        '''
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