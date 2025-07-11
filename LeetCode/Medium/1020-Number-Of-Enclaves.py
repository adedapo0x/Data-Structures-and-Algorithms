class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        '''
        Approach here is to start from the edges and traverse to see if there are any connected land cells as those would also be landfilled.
        We run a loop checking all the edges of the grid given (the boundaries) looking for a 1, if found we run a DFS that checks if there are any 
        connecting 1s to it and marking them as 0 as they can be flood filled since they have a edge that is at the boundary to the sea.

        After that we can say that all existing 1s in the grid, cannot walk off the boundary in any number of moves and we just traverse through the entire
        grid once again to count the 1s that are left and that is our answer.

        TC: O(M * N)
        SC: O(M * N) since we use a replica array to avoid mutating given input, and maybe the recursion stack space if it is to be considered.
        '''
        replica = []
        ROWS, COLS = len(grid), len(grid[0])
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        # replicate input grid (best practice) in order to avoid changing input when not instructed to
        for i in range(ROWS):
            temp = []
            for j in range(COLS):
                temp.append(grid[i][j])
            replica.append(temp)

        # function to run DFS on replica to check land cells that can be floodilled
        def check(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or replica[r][c] != 1:
                return

            replica[r][c] = 0 # sets those cells to 0 ie flooded
            for dr, dc in positions:
                neiR, neiC = dr + r, dc + c
                check(neiR, neiC)

        for r in range(ROWS):
            if replica[r][0] == 1:
                check(r, 0)
            if replica[r][COLS - 1] == 1:
                check(r, COLS - 1)
        for c in range(COLS):
            if replica[0][c] == 1:
                check(0, c)
            if replica[ROWS - 1][c] == 1:
                check(ROWS - 1, c)
        
        validCells = 0
        for r in range(ROWS):
            for c in range(COLS):
                if replica[r][c] == 1:
                    validCells += 1
        return validCells
            
        