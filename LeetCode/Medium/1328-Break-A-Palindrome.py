class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        '''
        The algorithm checks half the input string, since we want to break the palindrome in a lexicographically smallest order
        So we are looking to turn the first non 'a' character to 'a', just one change of character is enough to break the palindrome
        We account for both even and odd length, since we are using integer division, 5 // 2 is 2, so we don't get to the third element at index 2 which is in the second half of the string
        If the input string consists of just a's, our if in the loop never happens and it is still a palindrome
        Way to solve that is to change the last character to 'b', that way the string will contain a's and end with b, which is still the smallest lexicographical way it could have been broken
        '''
        n = len(palindrome)
        # checks if string is of more than one length
        if n < 2:
            return ""
        mid = n // 2
        paliList = list(palindrome)
        # checks the list up until its mid (since it's a palindrome, no need to check the rest)
        for i in range(mid):
            if paliList[i] != 'a':
                paliList[i] = 'a'
                return "".join(paliList)

        # thsi
        paliList[-1] = 'b'
        return "".join(paliList)
