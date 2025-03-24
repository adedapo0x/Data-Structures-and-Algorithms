class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        Optimal approach, uses binary search since array is sorted, we basically run a traditional BS then check just before the loop condition 
        becomes false for the position the element should be inserted in, which would be the new l, thatt's if you didn't find the target in the array
        TC: O(logN), SC: O(1)

        Bruteforce would entail using a linear search, then once you see the first element higher, return that index you are in. Edge case would
        prolly be if the element is to be at the end of the array, we can check explicitly for that

        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid -1 
            if l > r:
                return l