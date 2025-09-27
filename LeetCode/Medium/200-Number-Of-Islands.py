class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        The BFS solution. So we basically traverse through the 2D grid and kinda treat it like a graph, once we encounter a 1 that we have not seen before,
        we check both vertically and horizontally (note that assuming we had to check in all directions ie including diagonally we would have just ran two loops one inside the other
        from -1 to 1 for both loops cos that would get all the positions of top, slant, right, etc rather than having the positions in a list).

        So we check all its neighbours, if any of them is 1, and has not been visited, we consider it as part of the current island (ie add to visited and keep the BFS going) until there are no neighbour 1s. 
        then we keep on traversing in the grid until we meet the next 1 that hasn't been visited, or until we complete the traversal of the grid.

        Each time we come across a new unvisited 1 from our traversal that denotes the start of an island, we increment the count of islands.
        TC: O(m * n) where m and n is number of rows and cols
        SC: O(m *n) from visited list and queue used
        '''

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islandCount = 0

        for m in range(ROWS):
            for n in range(COLS):
                if (m, n) not in visited and grid[m][n] == "1":
                    islandCount += 1
                    self.bfs(m, n, visited, grid)

        return islandCount
    
    def bfs(self, row, col, visited, grid):
        visited.add((row, col))
        queue = collections.deque([(row, col)])
        ROWS, COLS = len(grid), len(grid[0])
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        while queue:
            r, c = queue.popleft()
            for deltaR, deltaC in positions: 
                rNeighbour = r + deltaR
                cNeighbour = c + deltaC

                if (rNeighbour >= 0 and rNeighbour < ROWS and cNeighbour >= 0 and cNeighbour < COLS 
                    and grid[rNeighbour][cNeighbour] == "1" and (rNeighbour, cNeighbour) not in visited):

                    queue.append((rNeighbour, cNeighbour))
                    visited.add((rNeighbour, cNeighbour))

    '''
    The DFS solution, same logic, but thisi time the traversal is done using DFS algorithm
    '''

    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        islandCount = 0

        for m in range(ROWS):
            for n in range(COLS):
                if (m, n) not in visited and grid[m][n] == "1":
                    islandCount += 1
                    self.dfs(m, n, visited, grid)

        return islandCount

    def dfs(self, row, col, visited, grid):
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in visited or grid[row][col] == "0"):
            return

        visited.add((row, col))
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for rIndx, cIndx in positions:
            self.dfs(row + rIndx, col + cIndx, visited, grid)

    # another more intuitive way the dfs could have been impelemented similar to the bfs style also 
    # this function would have to be inside the main function btw
    # def dfs(r, c):
    #     visited.add((r, c))
    #     for dr, dc in positions:
    #         neiR, neiC = r + dr, c + dc
    #         if (neiR >= 0 and neiR < ROWS and neiC >= 0 and neiC < COLS and 
    #             grid[neiR][neiC] == "1" and (neiR, neiC) not in visited):

    #             dfs(neiR, neiC)
