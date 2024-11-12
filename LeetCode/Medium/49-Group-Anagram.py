class Solution:
    def groupAnagrams(self, strs):
        # this method uses an array to store the count of characters in each word, those with same number of characters means they are anagrams
        # this is used to avoid sorting which is a O(nlogn) operation. 
        # then we store the count as the key, wrapped in a tuple, as lists are not hashable in Python
        # with values of the hashmap as a list of different words that are anagrams 

        # Time complexity: O(m.n) where m is number of strings and n is length of the longest string
        # Space complexity: O(m)
        from collections import defaultdict
        res = defaultdict(list)

        for str in strs:
            count = [0] * 26

            for c in str:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(str)

        return list(res.values())



        # uses sorting in this case, here the sorted version of the string is the key 
        # Time complexity: O(m.nlogn)
        # m is number of string in input array, n is the length of longest string, nlogn is because that is the TC of the sorting algorithm
        

        # anagramDict = {}
        # for chars in strs:
        #     # sorts each string element and assigns sorted string as key,
        #     # and all anagrams from it as value
        #     sortedWord = ''.join(sorted(chars))
        #     if sortedWord not in anagramDict:
        #         anagramDict[sortedWord] = []
        #     anagramDict[sortedWord].append(chars)
        # return list(anagramDict.values())