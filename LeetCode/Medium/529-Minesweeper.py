class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        '''
        approach is straightforward, if we click the spot that has M (mine) we change it to x and return immediately, game over
        if not then that means the spot contains an E, then we check the neighbours along all valid 8 sides (top, right, bottom, left, diagonals)
        to see if any of them contain a mine and we count the amount of neighbours contain mines, if any of them do we update the value in that spot
        if none of the neighbours have a mine, we then put B in the spot, and recursively process neighbours looking for mines.

        TC: O(M*N) where M, N is the row, col of the board respectively
        '''
        row, col = click
        ROWS, COLS = len(board), len(board[0])

        if board[row][col] == "M":
            board[row][col] = "X"
            return board

        positions = [
            (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
        ]

        def dfs(row, col):
            if board[row][col] != "E":
                return

            count = 0
            for deltaR, deltaC in positions:
                neighR, neighC = row + deltaR, col + deltaC
                if (0 <= neighR < ROWS and 0 <= neighC < COLS):
                    if board[neighR][neighC] == "M":
                        count += 1

            if count > 0:
                board[row][col] = str(count)
                return

            board[row][col] = "B"

            for deltaR, deltaC in positions:
                neighR, neighC = row + deltaR, col + deltaC
                if (0 <= neighR < ROWS and 0 <= neighC < COLS):
                    dfs(neighR, neighC)

        dfs(row, col)
        return board


