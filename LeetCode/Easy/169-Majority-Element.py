class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Approach here is to use an hashmap to store the occurence of each value in the input array, then since we know there is going to be
        one which is the majority element, ie its occurence will be greater than half the array, so we now loop through the hashmap to find the
        one that fit this condition.
        TC: O(N), SC: O(N)
        '''
        countHash = {}
        length = len(nums)
        for n in nums:
            countHash[n] = countHash.get(n, 0) + 1

        for key, val in countHash.items():
            if val > (length // 2):
                return key




        
        