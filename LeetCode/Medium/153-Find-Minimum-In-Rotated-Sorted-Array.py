class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Optimal approach is to use a binary search, each time we split the sorted rotated array, there is always going to be one half
        # that is sorted while the other is not sorted. We can get the minimum from the one that is sorted by getting the one at the leftmost end
        # i.e left for left-mid half, and mid for mid-right half. After we get the mid there, we cross to the other side to check if there is any value
        # smaller than what we currently have and we run the same logic again
        # TC: O(logn), SC: O(1)
        l, r = 0, len(nums) - 1
        minimumVal = nums[0]        
        while l <= r:
            # Another optimization can be done here that is not explained above (solution still works without it)
            # if at any point in time, our left to right is sorted, just have element at left as the answer if it is smaller than what is 
            # currently being held in minValue. this is because for this to happen, the rest of the array has been eliminated or the input array was completely sorted
            if nums[l] <= nums[r]:
                minimumVal = min(minimumVal, nums[l])
                break
            mid = (l + r) // 2
            if nums[l] <= nums[mid]:
                minimumVal = min(minimumVal, nums[l])
                l = mid + 1
            else:
                minimumVal = min(minimumVal, nums[mid])
                r = mid - 1 
        return minimumVal

      
        # Bruteforce solution. Linear traversal to find the minimum element in the array
        # TC: O(N), SC: O(1)
        return min(nums)