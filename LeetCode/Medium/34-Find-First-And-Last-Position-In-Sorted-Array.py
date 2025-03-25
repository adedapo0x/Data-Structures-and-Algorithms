class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        '''
        Optimal approach: This is to use binary search on the array twice, first to get the first occurence(lower bound) then run it again 
        if the element is present to find the last occurrence(upper bound).  
        TC: O(logN) + O(logn) = O(logN)  
        '''
        if len(nums) == 0:
            return [-1, -1]
        first = self.occurenceIndex(nums, target, True)
        if first == -1:
            return [-1, -1]
        second = self.occurenceIndex(nums, target, False)
        return [first, second]
    
    # if bias is True, we are trying to find first occurrence so right point has to shift to left, 
    # if bias is False, finding the last occurence and left pointer gotta shift to the right
    def occurenceIndex(self, nums, target, bias):
        l, r = 0, len(nums) - 1
        occur = -1 # default value if target not found
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                occur = mid
                if bias:
                    r = mid - 1
                else: l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return occur


    # Bruteforce way to do this would have been to linearly traverse through the array and find the first and last 
    # occurence index. More straighforward
    # TC: O(N)
