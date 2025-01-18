class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            w = r - l
            area = h * w
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else: r -= 1
        return res
    
        # Brute force approach O(N^2), leads to TLE
        # here we check every single possible container and return the one with max area, since we don't eant it to spill, we use side with lesser height to calculate the area
        n = len(height)
        maxA = 0
        for i in range(n):
            for j in range(i+1,n):
                h = min(height[i], height[j])
                w = j - i
                area = h * w
                maxA = max(area, maxA)
        return maxA