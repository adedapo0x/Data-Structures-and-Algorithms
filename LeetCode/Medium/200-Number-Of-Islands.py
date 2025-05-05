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