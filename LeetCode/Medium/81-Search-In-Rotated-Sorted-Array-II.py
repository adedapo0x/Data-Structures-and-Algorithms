class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        this is like a build up on question 33, but in this case, elements can have duplicates unlike in 33 were elements are guaranteed to be unique
        So say we have a test case of [1, 0, 1, 1, 1], we get mid at index 2 and since nums[l] <= nums[mid], our code will assume that part to be sorted and since zero is not in that range,
        it moves to the other half where it would never find zero and return False despite zero being in nums. 

        So we want to avoid issues like this, they only arise when nums[l] == nums[mid] == nums[r], after we have checked that the the element at mid is not the target
        so we shift the boundaries one way left and right, the continue statement checks again in case if we have multiple elements that meet the condition, so the rest of the code
        doesn't run until numbers at mid, l and r are not equal to each other

        Note: IMportant to put the edgecase after checking that value at mid is not the target, this is because say during the BS, say we are on the last element to be checked (which happens to be our target)
        whereby l and r are on the same index, we get mid as the same index too, so the values are all equal, but we cannot adjust l and r in that case cos that is what we are looking for, so we 
        def need to run the nums[mid] == target check first.

        TC: O(logN) for best and average case, but for worst case this is O(n/2), this is bcos for worst case, all elements in nums will be the same but are not the target, like 
        [3,3,3,3,3,3,3,3,3,3] and target is 0, so we keep up on shifting both left and right by one until they go out of bounds and the code would have ended up running about n/2 times
        SC: O(1)
        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return True
            # The edgecase to check for
            if nums[l] == nums[mid] and nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue
            if nums[l] <= nums[mid]:
                if target >= nums[l] and target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if target >= nums[mid] and target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1 
        return False
    

        # Bruteforce is obviously to traverse through the array linearly and find if the element is there
        # TC: O(N), SC: O(1)