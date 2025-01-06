class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # optimal solution, shorter more direct code
        # in this case loops never runs if the length of nums is 1
        # TC: O(N), SC:O(1)

        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j
    

        # two pointers approach (more like a rewrite of the first one, came up with it in revision)
        if len(nums) == 1: return 1
        l = r  = 1
        n = len(nums)
        while r < n:
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
            r += 1

        return l
        


        # better solution, still not completely optimal, uses two pointer method
        # TC: O(N), SC: O(1)

        k = 0
        l = 0

        for r in range(len(nums)):
            if r != 0 and nums[r] == nums[r - 1]:
                continue
            k += 1
            nums[l] = nums[r]
            l += 1
    
        return k


        # not at all optimal, my first shot at the question, uses extra memory when the question said to solve it in-place
        # time complexity: O(N) but takes two passes
        # space Complexity: O(N), can be better can be O(1)

        uniqueHash = {}

        for n in nums:
            uniqueHash[n] = uniqueHash.get(n, 0) + 1

        i = 0
        for n in uniqueHash:
            nums[i] = n
            i += 1

        return len(uniqueHash)