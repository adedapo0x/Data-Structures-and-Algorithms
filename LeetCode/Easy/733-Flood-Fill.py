class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        Having to create a new copy of image since it is good practice to not mutate the input data unless specified.
        TC: O(NM) + O(4 * NM) = O(NM), in worst case scenario, the entire image is of the same color, so we have to traverse through the entire image
        and for each position, we have to check 4 adjacent positions, so we have that
        SC: 
        '''
        ROWS, COLS = len(image), len(image[0])
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        begin = image[sr][sc]
        copy = []
        
        for row in image:
            temp = []
            for item in row:
                temp.append(item)
            copy.append(temp)

        def dfs(r, c, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or copy[r][c] == prev
                or copy[r][c] != begin):
                return

            copy[r][c] = prev
            for dr, dc in positions:
                neiR, neiC = r + dr, c + dc
                dfs(neiR, neiC, prev)

        dfs(sr, sc, color)
        return copy
            