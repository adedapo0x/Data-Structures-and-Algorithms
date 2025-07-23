class Solution:
    def topKFrequent(self, nums, k: int):
        # use bucket sort to do it, we use a hashmap to keep occurrence then build a bucket ie an array of arrays and we have each bucket index
        # as an array to use to store elements that occurs that particular number

        # TC: O(N)

        # using the array solution, there's also a heap solution
        # create initial empty hashmap

        freq = {}

        # instantiate hashmap based on nums array input
        for i in range(len(nums)):
            freq[nums[i]] = 1 + freq.get(nums[i], 0)

        # count array, it's indexes to store frequency
        # group of numbers that occurs same time are in the same array for a particular index(freq) 
        
        count = [[] for i in range(len(nums) + 1)]
        result = []
        for key, val in freq.items():
            count[val].append(key)

        # loops through the array of arrays from the back, since highest index signifies highest frequency
        for i in range(len(count) - 1, 0, -1):
            for j in range(len(count[i])):
                result.append(count[i][j])
                if len(result) == k:
                    return result


        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        ans = []
        for i in range(k):
            maxi = 0
            maxKey = 0
            for key, val in count.items():
                if val > maxi:
                    maxi = val
                    maxKey = key

            ans.append(maxKey)
            del count[maxKey]
        return ans
