class Solution:
    def twoSum(self, nums, target: int): 

               
        hash = {x:nums.index(x) for x in nums}
        for i in range(len(nums)):
            secondVal = target - nums[i]
            if secondVal in hash and hash[secondVal] != i:
                return [i, hash[secondVal]]
        return []