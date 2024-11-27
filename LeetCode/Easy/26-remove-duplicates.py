class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


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