'''
Question here is to generate a minesweeper board of specified size, put n mines across random cells in the board
and then calculate for each safe cell calculate the amount of neighbour cells that contains mines
neighbours are in all direction, top, right, bottom, left and all four diagonals

follow-up: implement reveal_cell, which reveals the cell at (row, col). If the revealed cell has no neighboring mines,
all of its neighbors must be revealed automatically, and this continues for any neighbor that also has no neighbouring mines.
Cells with neighbouring mines are revealed but do not expand further. If the user reveals a mine, print a losing message.
'''

# we can model this as a class

import random
class MineSweeper:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
        self.board = [[0] * cols for _ in range(rows)]
        # this is_revealed is added to track positions that we have revealed, when asked the follow up question.
        self.is_revealed = [[False] * cols for _ in range(rows)]


    def generate_minesweeper(self, num_mines):
        '''
        approach to generate random cells to put mines: we use random.sample which takes a specified number of random elements from a given iterable, in this case
        range(rows * cols), 
        '''
        board = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        positions = random.sample(range(self.rows * self.cols), num_mines)

        for position in positions:
            row, col = divmod(position, self.cols)
            board[row][col] = -1
            
        for row in range(self.rows):
            for col in range(self.cols):
                if board[row][col] != -1:
                    count = 0
                    for dr, dc in self.directions:
                        neiR, neiC = dr + row, dc + col
                        if (0 <= neiR < self.rows and 0 <= neiC < self.cols and board[neiR][neiC] == -1):
                            count += 1
                    board[row][col] = count
        return board    
                
    def reveal_cell(self, row, col):
        if self.is_revealed[row][col]:
            return

        if self.board[row][col] == -1:
            print("GAME OVER!!!")
            return

        self.is_revealed[row][col] = True

        if self.board[row][col] == 0:
            for dr, dc in self.directions:
                neighbour_r, neighbour_c = row + dr, col + dc
                if (0 <= neighbour_r < self.rows and 0 <= neighbour_c < self.cols
                    and self.board[neighbour_r][neighbour_c] != -1 and not self.is_revealed[neighbour_r][neighbour_c]):
                    self.reveal_cell(neighbour_r, neighbour_c)


'''
another minesweeper variation problem being asked
Problem: You are given a m*n grid. You are asked to generate k mines on this grid randomly.
Each cell should have equal probability of k / m*n of being chosen.


There is a question about minesweepers that is an LC question
revise that also - Leetcode 529

'''

'''
Four approaches to solving this:
1. we can randomly generate cell coordinates and if it doesn't already have a mine, we include it to our list of mines up until we get k mines
2. we can also get all the cell coordinates in a list, shuffle that list, so we indeed have random coordinates and we pick from the list of random coordinates to put our mines
3. (approach used above) use inbuilt sample method to take numbers from the list of available spot without replacement
4. there is also a reservoir sampling approach, but I am not exploring that
'''

# Approach 2:
# here we shuffle all possible cells then pick from them so anyone could have been shuffled to any position
# TC: O(MN) where M, N is number of rows and cols respectively. through creating board, cells and also shuffling cells 
# SC: O(MN) to store board and cells
import random
def generate_minesweep(rows, cols, num_of_mines):
    board = [
        [0 for _ in range(cols)] for _ in range(rows)
    ]

    cells = [(row, col) for row in range(rows) for col in range(cols)]
    random.shuffle(cells)
    
    for row, col in cells[:num_of_mines]:
        board[row][col] = "M"
        
    return board




# Approach 1:
# less efficient in a way cos if the grid is almost filled with mines, we could be generating a lot of random coordinates that are already filled with mines, 
# so we would have to keep generating until we get a coordinate that is not filled with a mine which could take a while
import random
def generate_minesweep(rows, cols, num_of_mines):
    board = [
        [0 for _ in range(cols)] for _ in range(rows)
    ]
    mines_created = 0
    while mines_created < num_of_mines:
        row = random.randint(0, rows - 1)
        col = random.randint(0, cols - 1)
        
        if board[row][col] != "M":
            board[row][col] = "M"
            mines_created += 1
            
    return board
