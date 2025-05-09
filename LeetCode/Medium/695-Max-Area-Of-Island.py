class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        Similar approach to number of Islands problem (LC 200), but here we are trying to get the area of each of the islands then find the maximum
        So here using a DFS, for each beginning of an island we encounter, we then count one for that island and try to fetch the nodes of all the other
        four directions recursively. 

        so after we are done with an island and it has returned the area, we compare it with our maxArea variable that we are using to keep the max of the areas found so far

        TC and SC: O(M * N), this can also be done with BFS.
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
    
        """
        BFS Approach. Still same logic, only difference is we do traversal here using BFS and not DFS and we do not use a visited set
        This is because a visited set gives Memory Limit Exceeded on leetcode, so here we have to alter the input grid values for each position
        that we have come across, so we turn each to 0 so we do not recalculate them.

        Same TC as approach above
        """

        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxIslands = 0

        def bfs(row, col):
            queue = collections.deque([(row, col)])
            count = 1
            grid[row][col] = 0

            while queue:
                r, c = queue.popleft()
                for deltaR, deltaC in positions:
                    neighbourR, neighbourC = deltaR + r, deltaC + c
                    if (neighbourR >= 0 and neighbourR < ROWS and neighbourC >= 0 and neighbourC < COLS
                        and grid[neighbourR][neighbourC] == 1):
                            queue.append((neighbourR, neighbourC))
                            grid[neighbourR][neighbourC] = 0
                            count += 1
            return count

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    area = bfs(row, col)
                    maxIslands = max(area, maxIslands)
        return maxIslands


        
        