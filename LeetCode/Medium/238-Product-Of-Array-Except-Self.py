class Solution:
    def productExceptSelf(self, nums):
        prefix, suffix = 1, 1
        res = [1] * len(nums)

        # res array first stores the prefix of each of the input array element
        # then gets multiplied with suffix in second loop

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i] # updating prefix after every iteration
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res
    


        '''
        Here, we use two arrays, one for prefix, the other for suffix, we first calculate them for each index
        Note that the first element as no prefix and it remains 1 hence why we start the iteration from index 1, also the last element has no suffix
        hence why we start the iteration from the second to the last element and not the last element


        then after, we multiply them into an ans array and return that as our ans
        TC: O(N) + O(N) + O(N) = O(3N) = O(N)
        SC: O(N)
        '''
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        ans = []
        for i in range(len(nums)):
            ans.append(prefix[i] * suffix[i])

        return ans
