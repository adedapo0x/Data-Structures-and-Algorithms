class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        Since we want to check for Os connected both horizontally and vertically that are surrounded by X completely and we do not want 
        to include the Os by the edge of the board since they'll be a part not actually surrounded by X,

        The approach here is to get all Os at the edge of the board since we won't be considering them, run a dfs from that position to check 
        for any other connected n so we don't consider them also since they'll have a region at the edge of the board, and temporarily changing them to another
        symbol say T for example, (we mutate the board and not use a list to keep track of Os at the edge so we avoid extra space being used), 

        so after the Os at the edge and their connected Os have been changed to something else so we don't consider them, we run a loop on the board to change all 
        the Os in the board to X (since we are now totally sure that the Os are not at the edge of the board) and change the Ts back to Os

        TC: O(MN)
        SC: O(MN) prolly due to stack space 
        '''
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


        