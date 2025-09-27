class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        '''
        Using Multi Source BFS approach. we do this to avoid having to visit the same positions in the grid multiple times and improve our time
        complexity. 
        So rather than starting from the land that can be traversed and having to traverse till we come across the first zero, we start from the gate instead, ie the 0
        so from here for every INF we come across from these zeros, we just calculate its distance from the gate

        To begin, we loop through the entire grid to append all the positions that contains zero as we are going to be doing the BFS from all those positions
        simultaneously, hence the Multisource BFS name, so for each layer, they will have the same distance from a particular zero, when we get to an INF, we update the value of that position
        and then add the position index to the queue in order to check for its own neighbours

        There is also a solution of using a visited set still using this approach, but with this way we get our answer while improving the SC also

        TC: O(M.N) first iteration to get 0 positions + O(M.N) since we don't revisit indexes = O(M.N)
        SC: O(1)
        '''

        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        queue = collections.deque()
        ROWS, COLS = len(grid), len(grid[0])
        inf = (2 ** 31) - 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))

        def addToQueue(r, c, dist):
            if (r >= 0 and r < ROWS and c >= 0 and c < COLS and grid[r][c] == inf):
                queue.append((r, c))
                grid[r][c] = dist + 1

        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                for dr, dc in positions:
                    neiR, neiC = r + dr, c + dc
                    addToQueue(neiR, neiC, dist)
            dist += 1



        '''
        TLE on Leetcode
        We use normal BFS here to traverse through all valid positions and once we find a 0 we return the amount of steps it took to get there.
        We go through every single element and when we come across an inf we call a BFS on it to possibly alter its value, important to note that
        each bfs call for each INF element uses a separate visited set, so we have to instantiate the set within the BFS function and not make it a global variable

        as per normal bfs, we use a queue, that is instantiated with the position of the INF value, and we make sure our visited set reflects that,
        then we go through all four positions ie horizontally and vertically as long as we can go there (ie indexes are valid, it is not -1, which cannot be traversed as
        stated in the problem, and it is not in our visited already), while keeping track of the distance we make after we are done with every layer of the queue.
        Once we hit a zero, we immediately return the distance that it took to get there. In the case, that we cannot traverse to a 0, because we are blocked by -1s all around, 
        at the end of the loop, we return inf, leaving the value as it originally was as stated by the problem

        TC: O(M.N)^2, this is because we go through each element and for every INF element we might basically have to go through the entire grid or near about to get a 0
        SC: O(M.N)
        '''
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
         