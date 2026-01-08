class NumMatrix:
    '''
    The optimal approach. Here we use prefix sums to precompute the sums of sub-matrices. we do this within the init before the sumRegions is called
    to use prefix sum here, we take another matrix (prefixMatrix) to store those sums. for each index in prefixMatrix, we take that as the bottom right of the matrix
    and it'll contain the sum of all the elements from the topmost left of the input matrix up until that index, note that it doesn't go beyond that index in col (ie further to the right)
    or in row (ie lower than that index), just sums of elements within that sub region with each index denoting the bottomRight corner

    note the size of the prefixMatrix, we make it bigger than the input matrix and prefilll with 0 to avoid edgecases. since we always get sum above and by the left, if we try to get 
    for the topmost or leftmost corner of the input matrix, our index becomes invalid. so that extra upper row and left col makes sure when we try to get up and left for those indexes, we end up just
    adding 0 to it which is still accurate.

    the prefix calculation itself is we get the sum from the start of that row to that particular index we are in, the sum being added up in the prefix variable for that row then add it with the index above, which would contain the sum of all above it.
    to get sumRegion, we take bottomRight that contains all elements from first element in matrix to that index, then subtract whatever is above the submatrix, subtract whatever is by the left of the submatrix, but by subttracting
    what is above and by the left, we end up minusing the elements sum that are to the left of the submatrix and above it as it is contained in both parts that is subtracted, ,hence the need to add it back once

    TC: for initializing O(N^2), while for sumRegion O(1)
    SC: O(N^2)
    '''
    
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