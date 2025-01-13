class Solution:
    def firstUniqChar(self, s: str) -> int:
        # TC: O(2N) = O(N), SC: O(26) which is constant time, because the string can only consist of the lowercase letters which are 26 in number
        mapCount = {}

        for ch in s:
            mapCount[ch] = mapCount.get(ch, 0) + 1

        for i in range(len(s)):
            if mapCount[s[i]] == 1:
                return i

        return -1
            