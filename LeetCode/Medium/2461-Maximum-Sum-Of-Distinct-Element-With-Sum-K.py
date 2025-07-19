class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        
        '''
        l = 0
        subarray = {}
        maxSum = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            subarray[nums[r]] = subarray.get(nums[r], 0) + 1

            if r - l + 1 > k:
                total -= nums[l]
                subarray[nums[l]] -= 1
                if subarray[nums[l]] == 0:
                    del subarray[nums[l]]
                l += 1

            if len(subarray) == k and r - l + 1 == k:
                maxSum = max(total, maxSum)

        return maxSum
        