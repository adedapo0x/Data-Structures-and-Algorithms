class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        Optimal solution, TC: O(N), SC: O(1)
        We use two pointers here, we set our left at the beginning, right at the end, and the maxLeft and maxRight to the values at the left and right respectively
        In previous solution we did min(maxLeft, maxRight) - height[i]. We don't exactly need the exact maxLeft and maxRight here
        We check if maxLeft <= maxRight, this means that for this to happen there has to be at least a block on the right with its length equal to or greater than maxLeft,
        so we can safely use maxLeft as the minimum height required. Same for if maxRight < maxLeft (the else condition), ie there exists at least one block or structure on the left that is >= maxRight, 
        so maxRight can be used. Then to avoid checking for negative values and to update our leftMax or rightMax, we do max(leftMax) - height[l]) or rightMax and r as the case may be.
        TC: O(N), SC: O(1)
        '''

        n = len(height)
        l, r = 0, n - 1
        maxLeft = height[0]
        maxRight = height[n-1]
        res = 0
        while l < r:
            if maxLeft <= maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res
        '''
        Approach is to use prefix and suffix arrays. The prefix array is to find the longest structure by the left of each index. Suffix is to find the
        longest by the right of each index. Note that first element would have a prefix of 0 and last element a suffix of 0. So if we have that, we take the minimum of both for each index,
        minimum because if we take the one that is greater, the water overspills. So for each index, we are checking the min(longestPrefix, longestSuffix) - height[i] 
        ie minus the length of that block to get how many blocks of water each block can retain above it
        note how we create the maxRight array, since we are appending to maxRight, even if our loop to create the maxRight is going from right to left, our
        maxRight is being created in a reversed order from left to right cos of append, so we have to start our iteration from maxRight from behind

        woulda been better to just have prefixed the size like maxRight = [0] * n , but this is another unnecessary O(N) op.
        
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
    

        # Bruteforce, gets TLE
        # Still uses the formular of min(leftMax, rightMax) - height[i] but we for each i we initially assume that height[i] is leftMax and rightMax,
        # so in this case, we don't have to deal with potential negatives. For each height[i], we check the entire elements before and after it to try to 
        # update its left and right max
        # TC: O(N^2), SC: O(1)
        n = len(height)
        res = 0

        for i in range(n):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])
            
            res += min(leftMax, rightMax) - height[i]
        return res

