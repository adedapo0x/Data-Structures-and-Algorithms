class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        Approach here uses the slinding window. We use a set to keep track of the window, and use pointers l and r for left and right pointers
        the first thing we do is to check if we are out of bounds and adjust the window accordingly by deleting from the set and moving the left pointer

        we coming across an element previously seen in the window signifies our condition is True, else we add the element we are currently on ie nums[r]
        to the window and keep the loop running. If at the end we do not find any duplicate in the appropriate window length, we return False.

        TC: O(N), SC: O(N)
        '''
        window = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                window.remove(nums[l])
                l += 1
            
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False

        
        

        