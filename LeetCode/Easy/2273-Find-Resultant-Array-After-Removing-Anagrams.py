class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        '''
        Optimal soln, instantiate a prev as an empty dict, then go through the array element, making a freq count of their characters using collections.Counter
        then we compare with our prev, if it is equal to prev, that means we have consecutive anagrams and we do not want that
        TC: O(N.K) where n is the number of words in the array and k is the average length of each word
        SC: O(1) kind of
        '''
        res = []
        prev = {}

        for i in range(len(words)):
            word1 = Counter(words[i])
            if word1 != prev:
                res.append(words[i])
                prev = word1
        return res
    


        "Same logic as above, just that here we are sorting to find anagrams, so TC is worse ie O(nklogk)"
        res = [words[0]]
        lastSorted = "".join(sorted(words[0]))

        for i in range(1, len(words)):
            sortedWord = "".join(sorted(words[i]))
            if sortedWord != lastSorted:
                res.append(words[i])
                lastSorted = sortedWord

        return res
