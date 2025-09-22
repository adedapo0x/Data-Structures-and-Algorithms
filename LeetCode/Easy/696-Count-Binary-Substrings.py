class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        '''
        Optimal approach is to note a pattern as to how valid substrings are made.
        a sequence of a number is like that particular number grouped together, so for example a sequence of 0 can be 0000 or 00, while that of 1 can be 1111111, 1, 11 etc
        now a boundary is where a sequence change to another sequence, e.g 1111|000|1111, so in this string those places with | are the boundaries
        
        now we notice that for a substring to be valid it must contain two sequences with a boundary between them
        also for that substring we would be able to find how many valid substrings can be derived from that substring with: min(length of first sequence, length of second sequence)
        e.g if we have a string 000111, this contains 2 sequences and one boundary, the min of the length of the sequence is 3, so 3 valid substrings can be generated from it: 01, 0011, 000111
        also take 00111, the min of length of sequences is 2, so two substrings: 01, 0011.

        so with this we can get it now, we go through the string starting from index 1, so prevCount keeps count of the previous sequence we saw, initially it is 0
        currCount is the length of the current sequence we are in, so since we are starting from index 1, we have the currCount set to 1, since we have an element in index 0 that is already been noted as being in the current count

        also need to remember to take min after the loop has ended to add the final valid substrings that would be generated after the last two sequences of the string has been traversed

        TC: O(N), SC: O(1) 
        '''
        prevCount = 0
        currCount = 1

        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                currCount += 1
            else:
                ans += min(prevCount, currCount)
                prevCount = currCount
                currCount = 1
        ans += min(prevCount, currCount)
        return ans        


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

        