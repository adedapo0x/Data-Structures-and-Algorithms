class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        there is a more optimal approach I think without the extra space, check on striver
        the approach here is that initially, say for test case [1, 2, 3], it can either start from 1 or from 2 or from 3, so we basically have 
        n paths the recursion would go, for this example, 3 paths. from there for the one beginning with 1, we can have 1,2 or 1,3 for one starting with 2, we can have
        2,1 or 2,3. and on and on till we get the temp array same length as num meaning all the elements are in there.
        The use of a set here is to allow for constant lookup of whether an element is in the array during the recursion rather than doing a O(N) for every check

        
        '''
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
        