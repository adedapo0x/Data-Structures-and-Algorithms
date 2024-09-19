class Solution:
    def longestConsecutive(self, nums) -> int:
        # converts list to set for faster lookup, if duplicates exists
        numSet = set(nums)
        longest = 0
        for num in numSet:
            # checks if current number - 1 exists, if it does, it cannot be the start of a sequence 
            # and hence continues to the next number in the hashset
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest