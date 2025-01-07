class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Optimal solution, uses two pointers, checks if num at pointer l is not zero, if that is the case, it swaps with element at pointer l
        # TC: O(N), SC: O(N)
        l = r = 0
        while r < len(nums):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
            r += 1

        # Brute force solution would have been to use a loop to iterate through the array initially, store the values of the non zeros in a temp array,
        # then loop through the array again replacing each value in input array with values in temp until temp is exhausted, then fill the rest of the input array with zer
        # TC: O(N) + O(x) + O(N - x) = O(2N) = O(N), where x is the number of non-zero numbers
        # SC: O(x), but worse case when there are no zeros in the input array, we have O(N) as entire array is stored again in temp