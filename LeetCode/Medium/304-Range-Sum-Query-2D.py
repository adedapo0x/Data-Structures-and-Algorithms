class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefixMatrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                # the equivalent of the input matrix row and col in prefixMatrix is row + 1, col + 1 since the prefixMatrix is bigger.
                # so trying to get the index above results is a row before that row (ie row + 1 - 1 = row) but still same col, that is why we have the variable "above" initialized like that
                above = self.prefixMatrix[row][col + 1] 
                self.prefixMatrix[row + 1][col + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomRight = self.prefixMatrix[r2][c2]
        top = self.prefixMatrix[r1 - 1][c2]
        left = self.prefixMatrix[r2][c1 - 1]
        topLeft = self.prefixMatrix[r1 - 1][c1 - 1]

        return bottomRight - top - left + topLeft



















    # Gives TLE on Leetcode, this is using the bruteforce approach, where we straightforward just loop through and try to sum them up
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                total += self.matrix[i][j]

        return total