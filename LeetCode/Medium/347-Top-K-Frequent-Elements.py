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

        '''
        Here, we use a heap, I feel this is a more intuitive solution, similar to what is implemented above but a bit better since we use a heap
        we get the frequencies of the elements in a hashmap, then we insert it as a pair into the maxheap, taking (freq, number), so when we are asked to get top K 
        frequent element, all we need to do is to pop from the heap k times

        TC: O(NlogN) from creating the heap, SC: O(N)
        '''

        mapper = Counter(nums)
        heap = []

        for num, freq in mapper.items():
            heapq.heappush(heap, [-freq, num])

        res = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)

        return res
        



        '''
        less optimal solution
        uses a hashmap to store occurrences, then we run a loop k times to get the k top frequent elements, then we go through the hashmap to see the onee
        with the max frequency, then we store its key in the hashmap, then delete that key from the hashmap so we can get the next frequent element

        TC: O(N^2), O(N) for hashmap, then considering in worst case, k can be n and the array can consist of n unique elements, 
        so the second for loop, has a TC of O(N^2) that way.

        '''
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
