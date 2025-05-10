class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Multisource BFS here. we go through the grid to get all the rotten ones initially while also keeping track of all the fresh ones, this
        is to determine if at the end of the BFS we have no more fresh oranges left, so we know what to return.

        So after getting all the positions of the rotten oranges and putting them in the queue so we can traverse from both ends simultaneoiusly,
        we then start checking neighbouring positions of those rotten oranges looking for fresh oranges while making sure the neighbours indexes are in bounds
        so if we see, we turn it rotten, put it on the queue to check its own neighbours and decrement the count of fresh oranges.

        Note: for the condition to keep the BFS running, we add freshCount > 0 because of a by 1 logical error we get at the end if it was not included.
        Because, at the end, after we have the last fresh orange turn rotten, our code still append it to the queue to look for neighbours even if there are no more fresh oranges
        it checks, no neighbours, so that's another unnecessary layer of the queue and that results in a 1 being added to the times after the for loop is done, with
        freshCount > 0, we can get rid of that

        TC: O(M * N),
        SC: O(M * N)
        '''
        ROWS, COLS = len(grid), len(grid[0])
        time, freshCount = 0, 0
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshCount += 1

        while queue and freshCount > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in positions:
                    neiR, neiC = dr + r, dc + c
                    if (neiR >= 0 and neiR < ROWS and neiC >= 0 and neiC < COLS 
                        and grid[neiR][neiC] == 1):
                        queue.append((neiR, neiC))
                        grid[neiR][neiC] = 2
                        freshCount -= 1
            time += 1

        return time if freshCount == 0 else -1

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
