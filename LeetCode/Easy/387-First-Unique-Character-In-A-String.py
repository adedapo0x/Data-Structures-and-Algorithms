class Solution:
    def firstUniqChar(self, s: str) -> int:
        mapCount = {}

        for ch in s:
            mapCount[ch] = mapCount.get(ch, 0) + 1

        for i in range(len(s)):
            if mapCount[s[i]] == 1:
                return i

        return -1
            