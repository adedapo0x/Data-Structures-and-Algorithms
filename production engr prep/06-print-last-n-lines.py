from collections import deque

def print_last_n_line(filepath, n):
    '''
    here we use a queue and we go over the entire file, but keep only the last n lines that we have seen in the queue, so at the end we would have the last n lines
    TC: O(L), L is number of lines in file, SC: O(n), n is the number of lines we want to print

    another approach is to store the entire file in a list using readlines and we then iterate from the last n elements in the file to get the last n lines,
    this is less efficient as we have to store the entire file in memory, and if the file is large, this can be a problem
    TC: O(L) where L is the number of lines in the file, SC: O(L), we end up storing the entire file in memory
    '''
    
    if n < 0:
        raise ValueError("n must be positive")
    
    last_lines = deque(maxlen=n)
    with open(filepath, "r") as file:
        # we could get last_line by doing last_lines = deque(file, maxlen=n)
        # and we would not need the loop to be appending to the queue one by one, it does it automatically 
        for line in file:
            last_lines.append(line)
            
        for line in last_lines:
            print(line)


try:
    print_last_n_line("test.txt", 3)

except ValueError as ve:
    print(f"Error: {ve}")
except FileNotFoundError:
    print(f"Error: File not found")