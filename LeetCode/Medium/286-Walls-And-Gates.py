class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        inf = (2 ** 31) - 1

        def bfs(row, col):
            visited = set()
            queue = collections.deque([(row, col)])
            visited.add((row, col))
            dist = 0

            while queue:
                for _ in range(len(queue)):
                    r, c = queue.popleft()
                    if grid[r][c] == 0:
                        return dist
                    for deltaR, deltaC in positions:
                        neighR, neighC = deltaR + r, deltaC + c
                        if (neighR >= 0 and neighR < ROWS and neighC >= 0 and neighC < COLS 
                            and grid[neighR][neighC] != -1 and (neighR, neighC) not in visited):
                            queue.append((neighR, neighC))
                            visited.add((neighR, neighC))
                dist += 1
            return inf

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == inf:
                    grid[row][col] = bfs(row, col)
         