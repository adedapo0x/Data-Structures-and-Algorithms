'''
this is a variation of the leetcode question 419. Counting Battleships

here, rather than counting the number of battleships, we want to print the cells that the battle ships are in

for example we have

[["X",".",".","X"],
 [".",".",".","X"],
 [".",".",".","X"]]
You may assume the following rules:

You receive a valid board, made of only battleships or empty slots.
Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships

output should be [(0,0)] [(0,3), (1,3), (2,3)} representing 2 ships on the board


a follow up could be: 
to implement  is_valid_board: every ship must be a straight line, and ships may not touch each other (including diagonally)

'''

def find_ships(board):
    '''
    approach is to find the beginning (top left corner) of the each ship and then check horizontally or vertically for the remnants of the ship
    as they can only span over one column or one row

    TC: O(M*N), SC: auxiliary space is O(k) where k is the total number of ship cells on board
    '''
    ROWS, COLS = len(board), len(board[0])
    positions = []
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                if (row == 0 or board[row - 1][col] != "X") and (col == 0 or board[row][col - 1] != "X"):
                    cells = [(row, col)]
                    # check horizontally
                    tempC = col + 1
                    while tempC < COLS and board[row][tempC] == "X":
                        cells.append((row, tempC))
                        tempC += 1
                    # check vertically
                    tempR = row + 1
                    while tempR < ROWS and board[tempR][col] == "X":
                        cells.append((tempR, col))
                        tempR += 1
                    positions.append(cells)
    return positions


'''
for the follow up of is valid board
the approach here is to make sure that for every X we come across, that none of its diagonal is also a X,
for example, if we have 

[["X","X",".","X"],
 [".","X",".","X"],
 [".",".",".","X"]]

we see that (0, 0) has an X on its diagonal at (1, 1), which violates the rule that they have to be entirely be in a single col or row
'''
def is_valid_board(board):
    # TC: O(M * N) where M and N is row and cols of board respectively.
    #  SC: O(1) no extra space used, directions is constant space (it never exceeds a length of 4)
    directions = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
    ROWS, COLS = len(board), len(board[0])
    
    for row in range(ROWS):
        for col in range(COLS):
            if board[row][col] == "X":
                for dr, dc in    directions:
                    neighbour_R, neighbour_C = row + dr, col + dc
                    if (0 <= neighbour_R < ROWS and 0 <= neighbour_C < COLS
                        and board[neighbour_R][neighbour_C] == "X"):
                        return False
                    
    return True
