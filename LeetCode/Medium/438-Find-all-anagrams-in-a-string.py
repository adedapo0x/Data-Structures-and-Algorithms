class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        more optimal solution, here we use the sliding window technique, we create a hashmap for p and then we create a sliding window 
        of length len(p) in s and we keep track of the characters in that window using another hashmap, if at any point the two hashmaps are equal,
        then we have found an anagram and we add the starting index of that window to our result list.

        TC: O(N + M) where N is the length of s and M is the length of p,
        SC: O(M) for storing the hashmap of p or O(1) since we can only have 26 letters
        '''
        lenP, lenS = len(p), len(s)
        if lenP > lenS:
            return []
        sCount, pCount = {}, {}

        for i in range(lenP):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)

        l = 0
        res = [0] if sCount == pCount else []

        for r in range(lenP, lenS):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1

            if sCount[s[l]] == 0:
                sCount.pop(s[l])
            l += 1

            if sCount == pCount:
                res.append(l)
        return res



                   
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        '''
        brutefore approach: since we are looking for p anagrams in s, we can sort p and then for every substring of s
        of length len(p), we can sort that substring and compare it with sorted p, if they are equal, 
        then we have found an anagram and we can add the starting index of that substring to our result list.
        TC: O(N * M log M) where N is the length of s and M is the length of p, SC: O(M) for storing sorted p
        '''
        lenP = len(p)
        lenS = len(s)
        if lenP > lenS:
            return []

        sortedP = sorted(p)
        res = []
        for i in range(lenS - lenP + 1):
            sortedS = sorted(s[i:i+lenP])
            if sortedS == sortedP:
                res.append(i)

        return res
            

        