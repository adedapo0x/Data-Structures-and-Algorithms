class Solution:
    def containsDuplicate(self, nums) -> bool:
        freqSet = set()
        for x in nums:
            if x in freqSet:
                return True
            else:
                freqSet.add(x)
        return False
    

        # a one liner
        # compares the length since a set only allows one occurrence of an element
        return len(nums) != len(set(nums))
    
        # TC: O(NlogN), since we sort
        # when we sort, the duplicates are next to each other so we just check for that
        # nums.sort()
        # n = len(nums)

        # for i in range(n - 1):
        #     if nums[i] == nums[i+1]:
        #         return True

        # return False