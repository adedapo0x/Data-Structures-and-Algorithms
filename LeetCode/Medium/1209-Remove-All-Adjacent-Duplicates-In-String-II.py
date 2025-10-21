class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        '''
        Bruteforce approach, we scan through each time for k adjacent duplicates, once we find one, we change the string, then restart from the beginning
        to look for the next one, we stop only when we complete a pass and the length of the string doesn't change, so length would now be equal to len(s)

        TC: O(N^2/k) since we go through the entire string N/k times and each time we do O(N) copying of string
        SC: O(N) for string copies since python strings are immutable 
        '''
        length = -1
        while length != len(s):          # keep looping until string stops changing
            length = len(s)
            count = 1
            for i in range(1, len(s)):
                if s[i] == s[i - 1]:
                    count += 1
                    if count == k:
                        s = s[:i - k + 1] + s[i + 1:]  # remove k characters
                        break                           # restart scan
                else:
                    count = 1
        return s
