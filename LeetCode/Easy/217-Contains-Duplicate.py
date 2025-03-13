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