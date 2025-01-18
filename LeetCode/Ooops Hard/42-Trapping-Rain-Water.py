class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Approach is to use prefix and suffix arrays. The prefix array is to find the longest structure by the left of each index. Suffix is to find the
        longest by the right of each index. Note that first element would have a prefix of 0 and last element a suffix of 0. So if we have that, we take the minimum of both for each index,
        minimum because if we take the one that is greater, the water overspills. So for each index, we are checking the min(longestPrefix, longestSuffix) - height[i] 
        ie minus the length of that block to get how many blocks of water each block can retain above it
        Then we have to check that the difference we get is not less than zero (ie min height we have is not smaller than the length of the current index that we are in) if it is, we give it zero
        because negative values would mess up our count
        then add up the total of the array we used to store the water being stored
        TC: O(N), SC: O(N)
        '''
        n = len(height)
        maxLeft = []
        maxRight = []
        maxL = maxR = 0
        for i in range(n):
            maxLeft.append(maxL)
            maxL = max(maxL, height[i])
        
        for i in range(n-1, -1, -1):
            maxRight.append(maxR)
            maxR = max(maxR, height[i])

        res = []
        r = n - 1
        for i in range(n):
            fill = min(maxLeft[i], maxRight[r]) - height[i]
            toFill = fill if fill >= 0 else 0
            res.append(toFill)
            r -= 1
        
        return sum(res)
