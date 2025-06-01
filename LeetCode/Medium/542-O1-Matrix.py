class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
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
