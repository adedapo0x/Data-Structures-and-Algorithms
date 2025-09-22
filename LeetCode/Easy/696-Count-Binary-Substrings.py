class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        Bruteforce quadratic time solution, works but gives TLE on Leetcode, too slow
        so what we do is we take each character as the start of a possible substring, and go down s starting from that character to see if we have a valid substring
        
        to know if a substring is valid, we use a helper function, in it we use a count variable, cnt. and two pointers, left and right
        initially both left and right are at the same index i, then we start to increment right, as long as character at right and left are the same, we are still seeing the same character and we keep on
        incrementing count, when we come across a new character, we stop the loop, and start another loop that tries to decrease the count to 0, this would be successfull if the length of the first character seen is the same
        as the length of the second character (this is what makes a valid substring btw), and we can return 1 signalling we found 1 valid substring else 0. we return once count is back at 0 since there is no need to continue down the string s for that index

        we have to be careful not to run into index out of range error when we increment our right and we have to check for it before we try to access the s[right] in order not to get an error

        TC: O(N^2) and SC: O(1)
        '''
        count = 0

        for i in range(len(s)):
            count += self.checkSubString(s, i)

        return count

        
    def checkSubString(self, s, indx):
        cnt = 0
        left = right = indx
        while right < len(s) and s[left] == s[right]:
            cnt += 1
            right += 1

        left = right
        while right < len(s) and s[left] == s[right]:
            cnt -= 1
            right += 1
            
            if cnt == 0:
                return 1
        return 0

        