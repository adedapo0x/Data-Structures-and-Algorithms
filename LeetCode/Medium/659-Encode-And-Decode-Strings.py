class Solution:
    def encode(self, strs) -> str:
        res = ""
        for s in strs:
            # there is need for the hash symbol because the length might not be just one digit
            # then we'll need something to tell where the length ends and the str begins
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str):
        # personal soln, didn't use Neetcode own
        res = []
        l, r = 0, 0
        while r < len(s):
            if s[r] == "#":
                length = int(s[l:r]) # gets length
                l = r + 1 # puts left pointer at the beginning of the the word
                r += length + 1 # increments left pointer to the index after the end of the word
                res.append(s[l:r])
                l = r # updates left character to begin process again for next word
            else:
                r += 1
        return res