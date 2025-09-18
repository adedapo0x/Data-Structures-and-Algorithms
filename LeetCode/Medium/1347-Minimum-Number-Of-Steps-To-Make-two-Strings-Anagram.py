class Solution:
    def minSteps(self, s: str, t: str) -> int:
        '''
        Optimal approach does not need to make use of a hashmap, since the string can only contain lower case letters, so we know it'll be of size 26
        also we only use one array, incrementing frequency as we go across s and decrementing as we go across t

        the logic is after we are done going through s and t and updating freq, the positive values of s means the characters that are surplus in s and needs to also be in t
        since they are of equal lengths, this is just saying replace unwanted letters in t with these letters

        the logic is: 
        if freq[i] > 0: surplus in s, we need those characters to be in t
        if freq[i] == 0: then that particular length is of same frequency in both s and t, and we do not need to do anything
        if freq[i] < 0: this means t contains more of these than s, we do not care about this, since the surplus from s would be replacing these to make it an anagram of s

        TC: O(N)
        SC: O(1)
        '''
        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord("a")] += 1

        for ch in t:
            freq[ord(ch) - ord("a")] -= 1

        count = 0
        for i in range(26):
            if freq[i] > 0:
                count += freq[i]

        return count
        '''
        Not optimal
        This approach here is to count the freq of characters in both s and t using two different hashmaps, then we go through sHash storing characters of s
        if we see characters in s that are not in t, we add their freq to our count , then if we see elements that present in both but more in s than in t, then
        we add the difference between both.

        TC: O(N)
        SC: O(N) 
        '''
        sHash = Counter(s)
        tHash = Counter(t)

        count = 0
        for ch in sHash:
            if ch not in tHash:
                count += sHash[ch]
            else:
                if sHash[ch] > tHash[ch]:
                    count += sHash[ch] - tHash[ch]

        return count