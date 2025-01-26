class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        There is a three pointers solution for this, would come back to solving it later


        Since we know array can only contain, 0 to 2, use an array to store its frequency, then loop through the frequency array whilst
        modifying the input array
        TC: O(N), SC: O(1) since the frequency array is always of fixed size
        """
        count = [0] * 3
        for n in nums:
            count[n] += 1

        i = j = 0
        while i < len(nums):
            k = 0
            while k < count[j]:
                nums[i] = j
                k += 1
                i += 1
            j += 1

                                