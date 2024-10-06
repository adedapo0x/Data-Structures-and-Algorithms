class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
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