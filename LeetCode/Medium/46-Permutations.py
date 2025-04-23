class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res = []
        def computePermute(temp, tempSet):
            if len(temp) == len(nums):
                res.append(temp[:])
                return
            for i in range(len(nums)):
                if nums[i] not in tempSet:
                    temp.append(nums[i])
                    tempSet.add(nums[i])
                    computePermute(temp, tempSet)
                    temp.pop()
                    tempSet.remove(nums[i])
        computePermute([], set())
        return res
        