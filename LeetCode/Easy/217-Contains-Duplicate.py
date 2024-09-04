class Solution:
    def containsDuplicate(self, nums) -> bool:
        freqSet = set()
        for x in nums:
            if x in freqSet:
                return True
            else:
                freqSet.add(x)
        return False
