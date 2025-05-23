class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS, COLS = len(board), len(board[0])
        positions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def capture(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS 
                or board[r][c] != "O"):
                return

            board[r][c] = "T"
            for dr, dc in positions:
                neiR, neiC = dr + r, dc + c
                capture(neiR, neiC)


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r == 0 or r == ROWS - 1 
                    or c == 0 or c == COLS - 1):
                    capture(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"


        