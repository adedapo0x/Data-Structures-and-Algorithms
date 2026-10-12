class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        '''
        Approach is to just count the beginning of the ships. the beginning is the top left corner of the ship and since no ship is adjacent, there always has to be an empty cell
        in between them, then we can just check that if we come across a X and it has no X in the row above it and the col before it, that means it is the start(top left corner) of the battleship
        and we keep a count of each that we discover

        TC: O(M*N) where M and N is the row, col of the board
        SC: O(1)
        '''
        count = 0
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "X":
                    if (row == 0 or board[row - 1][col] != "X") and (col == 0 or board[row][col - 1] != "X"):
                        count += 1

        return count

        