class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        Approach here is similar to the initial one I came up with down below. Only difference is we do not wait till the dictionary is
        fully constructed before we start manipulating to append to the ans list

        Here, as we append to the dict values, we check its length, once the length is equal to the group size we want we append that list to our ans,
        clear it in our hashmap, then clear the list from the hashmap. and we keep on iterating.

        TC: O(N)
        SC: O(N) due to the hashmap
        '''
        hashMap = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            size = groupSizes[i]
            hashMap[size].append(i)

            if len(hashMap[size]) == size:
                ans.append(hashMap[size])
                hashMap[size] = []

        return ans
        

        '''
        Approach here is to run through the input list initially and use a dictionary to store key, a list as values 
        the numbers in the input array (ie group sizes) are the keys and the indexes (ie the people themselves) are the values in a list

        then we iterate through the dictionary, and we do some interesting logic that I came up with to get the groups
        times is the number of batches that we have for a particular group sizes, eg for group size of 3, the key in the dict is 3, 
        and the indexes with that group size, say there are 6, so times become 2. so we can get two arrays from the val array
        l and r is for the indexes manipulation, so we run the loop a particular number of times which is times, and we get the subarrays appended
        to the ans array that is to be returned.

        TC: O(N) or thereabouts 
        SC: O(N) cause of the dict
        '''
        hashMap = defaultdict(list)
        ans = []

        for i in range(len(groupSizes)):
            hashMap[groupSizes[i]].append(i)

        for key, val in hashMap.items():
            times = len(val) // key
            l, r = 0, 1
            for i in range(times):
                ans.append(val[l * key: key * r])
                l += 1
                r += 1
        return ans
