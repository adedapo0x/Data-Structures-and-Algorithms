class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # just a simple two pointer solution
        a, b = 0, 0

        while a < len(s) and b < len(t):
            if t[b] == s[a]:
                a += 1
            b += 1

        return a == len(s)
        