class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        basically just use a pointer each for each word and pick alternatively while building our res array

        TC: O(m + n)
        SC: O(m + n)
        '''
        res = []

        p1 = p2 = 0

        while p1 < len(word1) and p2 < len(word2):
            res.append(word1[p1])
            res.append(word2[p2])
            p1 += 1
            p2 += 1

        if p1 < len(word1):
            res.append(word1[p1:])

        if p2 < len(word2):
            res.append(word2[p2:])

        return "".join(res)