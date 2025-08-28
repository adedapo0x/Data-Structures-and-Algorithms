class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        mini = nums[0]        
        while l <= r:
            # Another optimization can be done here that is not explained above (solution still works without it)
            # if at any point in time, element at left is lesser than or equal to element at the right ie our left to right is sorted, 
            # just have element at left as the answer if it is smaller than what is currently being held in minValue.
            # we still have to do min check after we see that the subarray we are considering is sorted is because the fact that is is sorted doesn't mean the beginning of the sorted part is the minimum 
            if nums[l] <= nums[r]:
                mini = min(mini, nums[l])
                break

            mid = l + (r - l) // 2 # another way of finding mid apart from (l + r) // 2 (better in case of overflow)
            mini = min(mini, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return mini

      
        # Bruteforce solution. Linear traversal to find the minimum element in the array
        # TC: O(N), SC: O(1)
        return min(nums)