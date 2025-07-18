class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
        Use a set to keep track of the indexes that have zero and go through it again to check the rows and columns there
        '''
        ROW, COL = len(matrix), len(matrix[0])
        checker = set()
        for i in range(ROW):
            for j in range(COL):
                if matrix[i][j] == 0:
                    checker.add((i, j))

        
        for row, col in checker:
            for i in range(COL):
                matrix[row][i] = 0
            for j in range(ROW):
                matrix[j][col] = 0
