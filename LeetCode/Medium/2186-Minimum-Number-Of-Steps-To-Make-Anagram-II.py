class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        Similar approach to 1347, but here since the strings are not of equal length, we need to add both the positive and the negatives
        differences between their frequencies

        TC: O(M + N), SC: O(26)
                
        '''
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord("a")] += 1

        for c in t:
            freq[ord(c) - ord("a")] -= 1

        count = 0
        for i in range(len(freq)):
            if freq[i] != 0:
                count += abs(freq[i])            

        return count
        