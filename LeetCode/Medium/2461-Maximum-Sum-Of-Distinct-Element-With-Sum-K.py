class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        '''
        Optimal solution here is to use sliding windows. We use a dictionary to keep track of the elements in our subarray and their count
        we use a dictionary here and not a set because, take test case of [1,1,1,7,8,9], when l = 0 and r = 3, the subarray becomes too much for the first time, 
        say we had a set, we would have removed 1, the next time we want to remove 1, we get a KeyError as 1 no longer exists in the set. 

        So what we do here is to use two pointers l and r in our sliding window approach. So every element we come across we add to the total and to the dictionary to keep track.
        should the subarray length exceed the k given, we know it is time to shift our left pointer so we reduce from total, reduce from dict and shift the left pointer.
        should the len of distinct elements in our dict be equals to k and the length of the subarray is also equal to k, the conditions for the subarray to be valid according to the 
        question, we then compare the total we have been accumulating with the maxSum, after the end of everything, we return maxSum

        Note that it is important to check if subarray length is greater than k before we check if it is equal to it, because initially after we get it to be equal, we check, then we increment r, 
        so in our code we handle that by shifting the left pointer to the right, but that creates a new subarray that we also need to check before we increment r, unless we end up missing some
        subarrays which could contain the answer 

        TC: O(N)
        SC: O(N)
        '''
        l = 0
        subarray = {}
        maxSum = 0
        total = 0

        for r in range(len(nums)):
            total += nums[r]
            subarray[nums[r]] = subarray.get(nums[r], 0) + 1

            if r - l + 1 > k:
                total -= nums[l]
                subarray[nums[l]] -= 1
                if subarray[nums[l]] == 0:
                    del subarray[nums[l]]
                l += 1

            if len(subarray) == k and r - l + 1 == k:
                maxSum = max(total, maxSum)

        return maxSum
        