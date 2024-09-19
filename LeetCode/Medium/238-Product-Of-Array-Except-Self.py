class Solution:
    def productExceptSelf(self, nums):
        prefix, suffix = 1, 1
        res = [1] * len(nums)
        # res array first stores the prefix of each of the input array element
        # then gets multiplied with suffix in second loop
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # updating prefix after every iteration
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res