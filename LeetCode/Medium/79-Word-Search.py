class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        approach here is to use backtracking, in this approach first we will linearly search the entire matrix to find the first letter matching our given string.
        If we found that letter then we can start backtracking in all four directions to find the rest of the letters of the given string.
        the base cases/checks conditions are for if our row and col variable ( r and c) ever get out of bounds, from our r + 1, c -1 calculations, we know to return
        False, or if the characters at where we are matrix and character at our position do not match which is the main thing we check for, we return False

        
        '''


        '''
        Same approach as above, but here, we use a set to determine if we have come across a particular character in the matrix for a particular run by storing the index positions of r and c in a 
        tuple and putting them in a set, if we have we return False as we cannot reuse the same letter cell for a particular check
        don't forget to remove the indexes of that r and c as we backtrack back up our recursion tree
        '''


        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def backtrack(r, c, indx):
            if indx == len(word):
                return True
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != word[indx] or (r, c) in visited:
                return False

            visited.add((r, c))

            top = backtrack(r + 1, c , indx+1)
            right = backtrack(r, c + 1, indx+1)
            bottom = backtrack(r - 1, c, indx + 1)
            left = backtrack(r, c - 1, indx + 1)

            visited.remove((r, c))

            return top or right or bottom or left

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0):
                    return True

        return False