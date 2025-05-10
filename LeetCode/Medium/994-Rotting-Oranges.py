class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Initial solution by myself, bit of redundancy done here and had to experiment with flags to get some testcases without any rotten
        # oranges to pass
        ROWS, COLS = len(grid), len(grid[0])
        minMinutes = 0
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = collections.deque()
        zFlag, oneFlag = False, False

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 0:
                    zFlag = True
                if grid[r][c] == 1:
                    oneFlag = True
        
        if not queue and not oneFlag and zFlag:
            return 0


        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in positions:
                    neiR, neiC = dr + r, dc + c
                    if (neiR >= 0 and neiR < ROWS and neiC >= 0 and neiC < COLS 
                        and grid[neiR][neiC] == 1):
                        queue.append((neiR, neiC))
                        grid[neiR][neiC] = 2
            minMinutes += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return minMinutes - 1 if minMinutes != 0 else -1
