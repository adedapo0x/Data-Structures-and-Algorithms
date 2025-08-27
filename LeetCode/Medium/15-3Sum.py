class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        optimal approach here is to sort the list, then take a first number, then try to get the next two numbers that their combined sum would equal 0 using similar
        technique used in two sum II, we are able to do this since the array is now sorted
        we ensure no duplicacy in our result like this:
        since we have the array sorted, duplicate numbers are now side by side in the list
        - for the first number selection, once we pick a number, the next number we pick as first number is not allowed to be that same number, so we skip for that index
        - for the second number selection, after we have one that gives us answer as 0, to pick the next second element, should in case the next number is the same as the second number that gave us the answer
        we put a check for it and we keep incrementing till we come across a number different from the second number

        these two ways ensure that there is no duplicates in the answer as the question requested,
        TC: O(NlogN) + O(N^2) = O(N^2)
        SC: O(M) 
        where N is the length of the nums array and m is the number of triplets
        '''
        n = len(nums) - 1
        nums.sort()
        res = []
        
        for i, a in enumerate(nums):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            l, r = i + 1, n
            while l < r:
                total = a + nums[l] + nums[r]
                if total == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return res