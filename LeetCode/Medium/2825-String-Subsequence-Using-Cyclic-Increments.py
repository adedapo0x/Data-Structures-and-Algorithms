class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # using two pointers approach
        # one pointer at beginning of str1, another at str2, checks if they are equal or if 
        # when cyclic operation performed on str1 makes it equal to character at str2 or the z and a edgecase

        # returns True if pointer is of length s2 meaning all matches were found 

        s1, s2 = 0, 0

        while s1 < len(str1) and s2 < len(str2):
            if str1[s1] == str2[s2] or chr(ord(str1[s1]) + 1) == str2[s2] or (str1[s1] == "z" and str2[s2] == "a"):
                s2 += 1
            s1 += 1

        return True if s2 == len(str2) else False