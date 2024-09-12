class Solution:
    def groupAnagrams(self, strs):
        anagramDict = {}
        for chars in strs:
            # sorts each string element and assigns sorted string as key,
            # and all anagrams from it as value
            sortedWord = ''.join(sorted(chars))
            if sortedWord not in anagramDict:
                anagramDict[sortedWord] = []
            anagramDict[sortedWord].append(chars)
        return list(anagramDict.values())