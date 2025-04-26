class Solution:
    def partition(self, s: str) -> List[List[str]]:
        '''
        here since we are working with substrings, at every index, we have choices, try to make a partition or continue, kind of sha
        so basically for each index, we check from that index to n - 1, where n is len(s) if partitioning at every index we iterate to is valid

        put simpler, The initial idea will be to make partitions to generate substring and check if the substring generated out of the partition will be a palindrome.
        Partitioning means we would end up generating every substring and checking for palindrome at every step, and we use recursion for this
        The recursion continues until the entire string is exhausted. After partitioning, every palindromic substring is inserted in a data structure. we don't bother for substrings that are not palindromes
        When the base case (getting to the end of the string for that recursion depth) has been reached the list of palindromes generated during that recursion call is inserted in a vector of list of lists.

        TC: O(2^n * n) checking for partitions, we have 2^n, and for checking palindromes for each partition hence the extra n
        SC: O(n) considering the temp array, if we consider output array, SC: O(2^n * n) also
        '''
        res = []

        def backtrack(indx, temp):
            if indx == len(s):
                res.append(temp[:])
                return
            
            for i in range(indx, len(s)):
                if self.isPalindrome(indx, i, s):
                    temp.append(s[indx:i+1])
                    backtrack(i+1, temp)
                    temp.pop()
                
        backtrack(0, [])
        return res
    
    def isPalindrome(self, start, end, s):
        while start < end:
            if s[start] != s[end]:
                return False
            start, end = start + 1, end - 1
        return True 