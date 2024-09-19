class Solution:
    def topKFrequent(self, nums, k: int):
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
