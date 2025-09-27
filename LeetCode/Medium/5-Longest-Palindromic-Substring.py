class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Approach here is that we change how we check for palindromes, in the solution below, we checked for palindromes from the edges inwards, and we had to generate all possible 
        substrings before we could check which gave it O(N^3), but here we check from inwards to outwards. 
        we take every index as if it were the middle of the palindrome and expand outwards to check if the characters match and keep expanding till characters do not match
        so here we do not need to generate all substrings before we do the palindromic check

        important to note that we use two pointers, l and r, 
        case 1: if string is "aaba", and we use l = r = i, we end up getting palindromes of only odd lengths, 
        e.g for i = 0, only a, for i = 1, only a again, for i = 2, b and aba, for i = 3, only a. see how we missed the aa there because it was of even length

        case 2: we account for even by using l = i, r = i + 1, so if i = 0, i + 1 = 1, we get the aa as a palindrome also
        so we need to do both for each index.

        TC: O(N) for scanning through by O(2N) for checking at each index if palindrome ==> so all is O(N^2)
        SC: O(1)

        but note that we are slicing whenever we get a new palindrome, which could downgrade the TC to O(n^3) back, so we need to implement this without the 
        slicing anytime we find something longer, also code to check palindrome is repeated, we could make that into helper function, reimplementation of this expand
        outwards approach up
        '''
        res = ""
        resLen = 0

        for i in range(len(s)):
            # get odd length
            l = r = i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # get even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if r - l + 1 > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res



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