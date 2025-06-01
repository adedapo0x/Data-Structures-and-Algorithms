class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Approach here is to use multi-source BFS. Since we are looking for nearest zero, we can do the reverse, start from all the zeros simultaneously,
        use a set to keep track of the indexes seen already, then traverse outwardly, keeping track of the distance of the 1s that we come across as we move outward

        So as we come across a 1, we put in the queue while incrementing the dist from the zero. So we then pop, update our ans list (tracking distance), then search its
        four adjacent sides for a valid unseen position

        TC: O(M.N)
        SC: O(M.N)

        '''
        visited = set()
        queue = collections.deque()
        ROWS, COLS = len(mat), len(mat[0])
        ans = []
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        # create a dist list to return as input (good practice not to mutate input)
        for i in range(ROWS):
            temp = []
            for j in range(COLS):
                temp.append(0)
            ans.append(temp)

        # another way to instantiate the ans array that represents the dist array
        # ans = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # get all the zeros and put it in the queue, we start traversal from there, that is multisource BFS, distance is also put in the queue, 
        # initially 0 
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    queue.append((r, c, 0))
                    visited.add((r, c))
        
        while queue:
            row, col, dist = queue.popleft()
            ans[row][col] = dist

            for dr, dc in positions:
                nRow, nCol = dr + row, dc + col
                if (nRow >= 0 and nRow < ROWS and nCol >= 0 and nCol < COLS and (nRow, nCol) not in visited):
                    queue.append((nRow, nCol, dist + 1))
                    visited.add((nRow, nCol))

        return ans


        '''
        This gives TLE on leetcode
        Good for bruteforce sha. The appproach here is that for each 1 that we come across in the grid, we do a BFS from there to find
        the distance to the nearest 0.

        TC: O(m.n)^2
        SC: O(m.n) 
        '''
        ans = []
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        ROWS, COLS = len(mat), len(mat[0])

        # creating a copu of input grid
        for i in range(len(mat)):
            temp = []
            for j in range(len(mat[i])):
                temp.append(mat[i][j])
            ans.append(temp)

        def bfs(r, c):
            dist = 0
            queue = collections.deque([(r, c)]) 
            visited = set()
            visited.add((r, c))
            while queue: 
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    if mat[row][col] == 0:
                        return dist
                    for dr, dc in positions:
                        neiR, neiC = dr + row, dc + col
                        if (neiR >= 0 and neiR < ROWS and neiC >= 0 and neiC < COLS and (neiR, neiC) not in visited):
                            queue.append((neiR, neiC))
                            visited.add((neiR, neiC))
                dist += 1
        
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                    ans[r][c] = bfs(r, c)

        return ans
