'''
The approach here is that there can be maximum of 1000 * 1000 points to check for ships in worst case scenario. So trying to go through all those points
one million times won't work since we are are going to have to call hasShips a million times, (ie for every point), but we are told that we can only call the 
hasShips maximum of 400 times. 

since we are also told that a maximum of 10 ships is what is going to be in the rectangle size given, so out of 1,000,000 points only 10 points contain ships,
so we know there are going to be a lot of empty spots. we can use divide and conquer, we split the rectangle into 4 different quadrants/parts. This is because
we are working with a 2D representation, if it were a 1D we would divide by 2. so 2D, divide by 4 roughly equal parts, I say roughly because when a side is odd, we do not
want to deal with decimals, so we take integer division always. 

note that we only want to recursively go over a quadrant if there is actually a ship in it. so before we start our splitting and recursion, we call the hasShips to see if there is 
a ship here, if there is not, we return 0, and no need to explore further for that one. This way we eliminate a lot of search space as we go down the recursion

now, to split, we take each quadrant and we note how it is formed, use graph below as reference, say we start from bottomLeft, we start from x1 up until xMid,
then for its y axis, we start from y1 up until midY, note that we do not want overlaps that causes repeating a position, so topLeft, on x axis starts from x1 to xMid
and for y axis, yMid + 1 to y2, the +1 is important, we do not want it to overlap with yMid, bottomLeft is already covering that. we do that for all the quadrants,
a breakdown is given below. then for all the x and y ranges for each quadrant we build our own bottomLeft and topRight from it in order to recursively call
'''


# 5                   *

# 4               *

# 3           *

# 2       *

# 1   *

# 0   1   2   3   4   5

# x1, y1 = bottomleft
# x2, y2 = topright
# bottomLeft = (x1, midX) (y1, yMid) = [x1, y1], [midX, yMid]
# bottomRIght = (midX+1, x2) (y1, yMid) = [midX+1, y1] [x2, yMid]
# topLeft = (x1, xMid) (yMid+1, y2) = [x1, yMid+1] [xMid, y2]
# topRight = (midX+1, x2) (midY + 1, y2) = [midX+1, midY+1] [x2, y2]

# topRight = [4,4]
# bottomLeft = [0,0]
# mid = [2,2]

# check if ship exists here
# check if it is a point return 1
# split, check split recursively


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        x1, y1 = bottomLeft.x, bottomLeft.y 
        x2, y2 = topRight.x, topRight.y

        # check if the rectangle coordinates are valid before calling hasShips. they may get invalid as we go down the recursion
        # x1 should always be <= x2 as it is either below it or same as it, same for y1 to y2
        if x1 > x2 or y1 > y2:
            return 0

        if not sea.hasShips(topRight, bottomLeft):
            return 0

        # if the coordinates are the same that means, shrink the rectangle into a single point and for we to have gotten all the way here, means our hasShips is still telling us that 
        # there is a ship here, if not we would have returned before we got here, so we add that one ship to our count
        if x1 == x2 and y1 == y2:
            return 1

        midX = (x1 + x2) // 2
        midY = (y1 + y2) // 2

        bottomLeft = self.countShips(sea, Point(midX, midY), bottomLeft)
        bottomRight = self.countShips(sea, Point(x2, midY), Point(midX+1, y1))
        topLeft = self.countShips(sea, Point(midX, y2), Point(x1, midY+1))
        topRight = self.countShips(sea, topRight, Point(midX+1, midY+1))

        # aggregate the total number of ships we come across in the four quadrants and return as answer
        return bottomLeft + bottomRight + topLeft + topRight