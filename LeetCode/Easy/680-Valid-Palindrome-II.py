class Solution:
    def validPalindrome(self, s: str) -> bool:
        # uses duplicate function to continue checking once one pair isn't equal
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return self.paliUtil(s, l + 1, r) or self.paliUtil(s, l, r - 1)
            l, r = l + 1, r - 1
        return True	

    def paliUtil(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    

    # uses recursion, but changes input arguments

# class Solution:
#     def validPalindrome(self, s: str, check=False) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             if s[l] != s[r]:
#                 if not check:
#                     return self.validPalindrome(s[l:r], True) or self.validPalindrome(s[l+1:r+1], True)
#                 return False
#             l, r = l + 1, r - 1
#         return True