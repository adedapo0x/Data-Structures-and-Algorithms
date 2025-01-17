class Solution:
    def countSubstrings(self, s: str) -> int:
        '''
        Approach in optimal solution is to take each element as the middle element in the palindrome we are checking, so initially we set our l and r as the 
        indexes as the loop progresses, we then keep up expanding the pointer to cover a wider range of elements, left pointer going left, right pointer going right, while checking if it is still a palindrome
        for each palindrome we get, we add to our res. We end up checking substrings of odd length 1, 3, 5 ... since initially we were looking at one element, then we shifted left and right pointer making it 3, then 5 and so on
        We still need to check for even length of pointers, so now l and r, is index i and the element after it, i + 1, ie we are starting with two elements, check that, shift l and r, we get 4, 6, 8 ...
        Note that there is no need to keep checking for more palindromes from an element as its middle once one substring of it isn't palindrome, hence the reason for the condition that leads to break.

        TC: O(N^2) + O(N^2) = O(N^2), since we take an element, expand through the rest of the array, take another, expand again. for both odd and even lengths of substrings
        SC: O(1)
        '''
        n = len(s)
        res = 0

        # checks for odd lengths of palindrome
        for i in range(n):
            res += self.checkPalindrome(s, i, i)

        # checks for even lengths of palindrome
        for i in range(n):
            res += self.checkPalindrome(s, i, i+1)

        return res

    def checkPalindrome(self,s,l,r):
        res = 0
        n = len(s)
        while l >= 0 and r < n:
            if s[l] != s[r]:
                break
            res += 1
            l -= 1
            r += 1 
        return res