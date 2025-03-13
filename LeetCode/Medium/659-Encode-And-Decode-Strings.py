class Solution:
    def encode(self, strs) -> str:
        #Better way to do this, since strings in Python are not mutable and a new res ends up being created for every iteration
        # more optimal to use a list then join to a string after the loop
        strList = []
        for st in strs:
            strList.append(str(len(st)) + "%" + st)
        return "".join(strList)

        res = ""
        for s in strs:
            # there is need for the hash symbol because the length might not be just one digit
            # then we'll need something to tell where the length ends and the str begins
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str):
        # edit: cleaner code I came up with again
        res = []
        l = r = 0
        while l <= r and r < len(s):
            if s[r] == "%":
                length = int(s[l:r])
                l = r + 1
                r = l + length
                res.append(s[l:r])
                l = r
            r += 1
        return res

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