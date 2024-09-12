class Solution:
    def twoSum(self, nums, target: int): 
        hash = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [i, hash[diff]]
            hash[nums[i]] = i
        return [] 

        # not so optimized solution (two pass hash table)    
        hash = {x:nums.index(x) for x in nums}
        for i in range(len(nums)):
            secondVal = target - nums[i]
            if secondVal in hash and hash[secondVal] != i:
                return [i, hash[secondVal]]
        return []
    
