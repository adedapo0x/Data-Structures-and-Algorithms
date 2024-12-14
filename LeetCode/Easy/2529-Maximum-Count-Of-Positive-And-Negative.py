class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # more optimal solution using binary search
        # created helper function to find the turning point of where negative int ends and where positive int begins
        # first called to find where negative ends, 0 is the target cos presence of our first zero or any other positive int denotes the end of negatives
        # second time helper function is called with 1, our first one or non-zero integer is the beginning of the positives
        # where negative stops is returned for count of negatives, len(nums) - where positive starts is count of positives, use examples to check it out
        # then we return max of both

        def findTurningPoint(nums, target):
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l # important to note that we are not returning mid here but left pointer, dry run examples to check out why

        return max(findTurningPoint(nums, 0), len(nums) - findTurningPoint(nums, 1))
            

        # this is the less optimal solution , TC: O(N)
        # more straightforward, just traverse through, keep count of positive and negatives, then return max
        # pos, neg = 0, 0
        # for n in nums:
        #     if n > 0:
        #         pos += 1
        #     elif n < 0:
        #         neg += 1
        # return max(pos, neg)
        