class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        Since we want to find out positions that can flow to both atlantic and pacific oceans, here rather than doing from the position to the oceans,
        let's consider from the ocean to the positions, so we take all the positions at the four edges of the heights grid which will obviously flow into respective 
        oceans, so from there we can dfs our way to see others that can also flow in as we go inner to the grid

        For it to flow from position to ocean, the neighbouring positions must be less or equal to that positions, so now that we are considering the reverse, our
        condition for checking as we go inner in the grid if it can flow to the ocean(edges) would be if that neighbouring position is  higher or equal to it (use examples to check
        this out and confirm). 

        so we keep two sets, one for pacific, another for atlantic, using it to track those that can to each respective oceans, then at the end, loop through the grid positions and check which
        is common to both ocean sets and return that one

        TC: O(MN)
        SC: O(MN)
        '''
        ROWS, COLS = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visitedSet, prev):
            if (r < 0 or r == ROWS or c < 0 or c == COLS
                or (r, c) in visitedSet or heights[r][c] < prev):
                return

            visitedSet.add((r, c))
            dfs(r - 1, c, visitedSet, heights[r][c])
            dfs(r, c + 1, visitedSet, heights[r][c])
            dfs(r + 1, c, visitedSet, heights[r][c])
            dfs(r, c - 1, visitedSet, heights[r][c])

        # checking from first row for pacific and last row for atlantic
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])

        # checking from first col for pacific and last col for atlantic
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])

        res = []
        # check what positions are common to both set, append to a list and return the list
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append((r, c))

        return res
        


        