class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        This is the optimal solution for this problem with TC of O(N) and SC of O(1)
        We use the Moore's voting algorithm to check for the majority element, we basically traverse through the list initially taking the 
        first element as the majority, then if we come across same number as what we are considering might be the majority, we increase, and if 
        we come across a different number, we decrease. So once we decrease up to an extent that count falls back to zero, this simply means that 
        we have gotten other numbers that their collected frequency is equal to the one we were considering and therefore that cannot be the majority, then we take the next 
        element and try the process again. This algorithm gives us the correct answer because we are going to have majority in the input list
        Note: If we are not sure if the array is going to actually contain a majority element (not just that occurs most, but that occurs for more than half the size of the array)
        we check the answer given by the Moore's algorithm, count how many times it appears to know if it is actually a majority, else return -1 or whatever
        '''
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1
        return res




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




        
        