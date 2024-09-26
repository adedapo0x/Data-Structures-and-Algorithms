class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        import collections
        rows = collections.defaultdict(set) # rows dictionary with key 0 - 9 and value as hashset of each inner array as a row
        cols = collections.defaultdict(set) # cols dictionary with key 0 - 9 and value as hashset of each value of inner array being on it sown column 
        boxes = collections.defaultdict(set) # inner subboxes (1 to 3 rows grouped together by integer division by 3 since they all result to 0, same for 4 to 6 and co)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # if empty, empty denoted by "." skips the checks and all, goes to next value
                    continue
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in boxes[(r // 3, c // 3)]:
                    return False
                
                # if not found in the hashsets already then we add and move to next value
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])

        return True
            
