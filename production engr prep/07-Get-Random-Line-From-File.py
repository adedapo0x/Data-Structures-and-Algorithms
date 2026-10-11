'''
Implement a function that returns a random fortune from a file containing multiple fortunes, where each fortune is separated by a delimiter (#).
The file may be too large to fit into memory, so you should process it one line at a time. Each fortune should have an equal probability of being selected.

Each fortune can contain multiple lines, and # marks the end of a fortune.
Our function should return one randomly selected fortune, with each of the three fortunes having an equal chance of being chosen.
There are two requirements to keep in mind:
- We shouldn't load the entire file into memory.
- We shouldn't need to know the total number of fortunes before we start.


approach: we can use reservoir sampling to solve this problem, we can keep track of the number of fortunes we have seen so far,
and for each fortune we see, we can generate a random number between 1 and the number of fortunes seen so far, 
if the random number is 1, we replace the current chosen fortune with the new fortune. This way, each fortune has an equal probability of being chosen.
TC: O(L), L is the number of lines in the file, SC: O(1), we only keep track of the current fortune and the chosen fortune, and the count of fortunes seen so far


bruteforce would be to load the entire file into memory, split by the delimiter and then choose a random fortune from the list, 
but this is not optimal as we would end up loading the entire file into memory.
TC: O(L), SC: O(L)
'''

import random
def print_random_line(filename, delimiter="#"):
    current_fortune = []
    chosen = None
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if line.strip() == delimiter:
                if current_fortune: # explicitly check here in case we have multiple delimiters in a row
                    count += 1
                    probability = random.randint(1, count)
                    if probability == 1:
                        chosen = "".join(current_fortune)
                    current_fortune = []
            else:
                current_fortune.append(line)
        if current_fortune:
            count += 1
            probability = random.randint(1, count)
            if probability == 1:
                chosen = "".join(current_fortune)
    return chosen
