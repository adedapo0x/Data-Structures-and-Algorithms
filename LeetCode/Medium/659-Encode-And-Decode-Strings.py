class Solution:
    def encode(self, strs) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str):
        # personal soln, didn't use Neetcode own
        res = []
        l, r = 0, 0
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r])
                l = r + 1
                r += length + 1
                res.append(s[l:r])
                l = r
            else:
                r += 1
        return res