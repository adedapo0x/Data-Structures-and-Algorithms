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

        
        '''
        Note that this approach would have worked assuming there was a guarantee that the matrix is a binary matrix ie it only contains 0 or 1.
        It fails a testcase on LC where the matrix initially contains -1 and we wrongly change it to 0, since the Leetcode question of this is not a binary matrix, it can contain both
        positive and negative numbers.

        The approach here is to go through the array and any index that has 0 as its element, we call markCol and markRol which are helper functions
        on it to mark that row and column to the end with -1. So after doing that for all the zeros present, we then go through the array once again and convert all the 
        -1 to 0s and we have our answer

        TC: O(M x N)(M + N) + O(M x N), approximately O(MN) ^ 3 I think
        SC: O(1)
        '''
        ROWS, COLS = len(matrix), len(matrix[0])

        def markRow(i):
            for j in range(COLS):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        def markCol(j):
            for i in range(ROWS):
                if matrix[i][j] != 0:
                    matrix[i][j] = -1

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == 0:
                    markRow(i)
                    markCol(j)

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j] == -1:
                    matrix[i][j] = 0
