'''
Problem: You are given a m*n grid. You are asked to generate k mines on this grid randomly.
Each cell should have equal probability of k / m*n of being chosen.

'''

'''
Three approaches to solving this:
1. we can randomly generate cell coordinates and if it doesn't already have a mine, we include it to our list of mines up until we get k mines
2. we can also get all the cell coordinates in a list, shuffle that list, so we indeed have random coordinates and we pick from the list of random coordinates to put our mines
3. there is also a reservoir sampling approach, but I am not exploring that
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
