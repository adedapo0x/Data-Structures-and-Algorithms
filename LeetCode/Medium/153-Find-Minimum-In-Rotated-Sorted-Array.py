class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Optimal solution here is to use binary search. For a rotated sorted array, there is usually 2 sorted sections of the array, the left sorted part
        and the right sorted part. This is because rotation of a sorted array simply means taking the smallest element in front of the array and putting it in the back
        so from this, we can say that there are two sorted parts, and the left sorted part will ALWAYS contain BIGGER numbers than the one in the right sorted part.

        so we get middle index, compare with what we initially have as mini, which is nums[0], could have been any element in the array, just makes more sense to use the first element
        if smaller, we update the mini variable. then we try to know where to go next, to do that, we have to know if the middle element is in the left sorted part or right sorted part
        if it is in the left sorted part, we want to go to the right sorted part as the left sorted part would never contain the minimum element
        if it is in the right sorted part, we try to go left, just to check if there are any lesser elements in the array that are also in the right sorted part.

        we figure out which part we are in like this:
        if the element at the mid index is greater than or equal to what is in the left index, we are in the left sorted part, this is because for an element to be in the right
        sorted part, it has to be less than every element in the left sorted part.
        if element at mid is less than what is in the left, we know the element is in the right sorted part,
        then we shift our pointers accordingly to find mini

        TC: O(logn), SC: O(1)
        '''
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