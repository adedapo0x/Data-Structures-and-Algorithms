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

        
        '''
        works but it is slow. Here the approach is to initially traverse through the list and keep track of the indexes with the same value using a 
        dictionary, the key is the number, the value is an array of indexes where the numbers occur.

        we then go through the values of the hashmap, if it has a length greater than 1, means there are duplicates, then we go through that index list
        to check if our abs(i - j) <= k condition holds. if so, then we return True.

        TC: O(N), SC: O(N)
        '''
        # hashMap = defaultdict(list)

        # for i in range(len(nums)):
        #     hashMap[nums[i]].append(i)

        # for val in hashMap.values():
        #     if len(val) > 1:
        #         for i in range(len(val) - 1):
        #             if abs(val[i] - val[i+1]) <= k:
        #                 return True

        # return False



        # works but I get TLE
        # n = len(nums)

        # for i in range(n - 1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j] and abs(i - j) <= k:
        #             return True

        # return False


        