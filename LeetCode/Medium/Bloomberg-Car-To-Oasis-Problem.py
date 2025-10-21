"""
Given a 2d matrix that represents a matrix where . denotes empty land, c indicates car, and o indicates oasis, and another integer gas which indicates gas we have left. Traversing one unit in the matrix consumes 1 gas unit. You can move up, down, left, and right.
So Example: the matrix below and gas = 5 returns true since we can get from c to o in 5 units (1 unit left, 3 units down, and 1 unit right)
[[. . . c .]
[. . . . .]
[. . . . .]
[ . . o . .]]

a) Check if car can reach oasis or not. (return bool val)
b) Now suppose there is a gas station in the matrix somewhere that is denoted by an integer k where k represents the gas units that the car will be refuelled. So if k is 2, car will gain gas. Check if car can still reach oasis (with or without gas station).
c) Now let's say there's obstacles in the matrix represented by r. how would you check if car can reach oasis?
[[. . . o],
 [. r . r],
 [. r r r],
 [c . . 20]]
with the above layout,
if gas = 2, output = False
if gas = 3, output = True
"""


'''
Approach is to use a single BFS to traverse through the grid

for a. we use BFS while keeping track of the fuel we have, for each node that we want to go into its neighbour, we decrease the fuel by 1, so once we can go no further for that particular path cos of no fuel, we skip that path. so if we reach oasis, return True, else queue would later become empty once fuel finishes in all path, then we return False after loop. Here we use just a set to keep track ofo (row, col) visited in order to avoid reprocessing that messes up the traversal

for b. where we can have a gas station, once we get a neighbour, we first decrement fuel, cost of going to that neighbour, then we check if that neighbour is a fuel station, if it is we update our fuel and put it in the queue when we want to call BFS next.
Note that since we can refuel, we can go through paths we have previously gone through before, but only on the condition that the fuel we now have supercedes that fuel that we were on at that path previously. This is why here we use a dictionary storing {(row, col): fuelAtRowCol}, so we know if it was present and fuel at that time. 

for c. where there can be rocks, we just check, we check before we decrement the fuel as cost of reaching that neighbour, because if that position/nodeValue is "r", we are not going through that node, so we shouldn't decrement fuel or add that position in our queue to be traversed

TC: O(N*M*F), we go through the whole desert once and can go through some parts again because of refuel condition, so hence the extra F where F is like the different number of fuel you can visit a particular node with
SC: O(N*M*F) because the queue during BFS can store same path multiple times cos of different fuel capacity

'''


import collections
def desertTraversal(desert, fuel):
    carPosition = None
    ROWS, COLS = len(desert), len(desert[0])
    
    for row in range(ROWS):
        for col in range(COLS):
            if desert[row][col] == "c":
                carPosition = (row, col)
                break
        if carPosition:
            break
    
    row, col = carPosition
    queue = collections.deque([(row, col, fuel)])
    visited = {(row, col): fuel}
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        row, col, fuelLeft = queue.popleft()
        if desert[row][col] == "o":
            return True
        if fuelLeft == 0:
            continue
        
        for deltaR, deltaC in directions:
            neighbourR, neighbourC = row + deltaR, col + deltaC
            if (neighbourR < 0 or neighbourR == ROWS or neighbourC < 0 or neighbourC == COLS):
                continue
            
            nodeValue = desert[neighbourR][neighbourC]
            if nodeValue == "r":
                continue
            
            newFuel = fuelLeft - 1
        
            if isinstance(nodeValue, int):
                newFuel += nodeValue
                
            if (neighbourR, neighbourC) in visited and newFuel <= visited[(neighbourR, neighbourC)]:
                continue
            
            queue.append((neighbourR, neighbourC, newFuel))
            visited[(neighbourR, neighbourC)] = newFuel
    return False
        