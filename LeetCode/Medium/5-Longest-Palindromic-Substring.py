class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Bruteforce approach, got TTL on leetcode
        The approach here is to check every possible substring to see if it is a palindrome and maintain a maxSub that stores the longest palindromic string we have seen so far
        to go through the string to get substrings is O(N^2) and the cost of checking a substring to see if it is a palindrome is O(N)
        so the overall TC is O(N^3), SC: O(1)
        '''
        maxSub = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPali(s[i:j+1]):
                    maxSub = s[i:j+1] if len(s[i:j+1]) > len(maxSub) else maxSub
        return maxSub

    def isPali(self, s):
        l, r = 0, len(s) - 1

        while l <= r and r < len(s):
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True