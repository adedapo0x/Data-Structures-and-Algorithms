class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        we use two pointers here, go through the array, when we come across something that is not val, we put it in front by swapping with what is in the left pointer index
        so left pointer keep tracks of valid answer

        TC: O(N), SC: O(1)
        '''
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1

        return left 

        
        