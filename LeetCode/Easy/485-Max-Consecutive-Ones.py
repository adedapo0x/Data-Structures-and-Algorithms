class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Loops through the array, if zero, reset count, else increment count and updates maxCount
        # TC: O(N), SC: O(1)
        maxCount = count = 0
        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
                maxCount = max(maxCount, count)
        return maxCount



        # Tried to implement sliding window approach here, worked (might be relatively slower, dk)
        l = r = maxCount = 0

        while r < len(nums):
            if nums[r] == 0:
                l = r+1
            else:
                maxCount = max(maxCount, r -l + 1)
            r += 1
        return maxCount
