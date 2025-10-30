class Solution:
    def equalFrequency(self, word: str) -> bool:
        '''
        A cleaner way to do it. still same logic as below, we simulate removing each character once, but here we also remove ones with freq of zero in order
        not to mess up the count since if freq becomes zero, that letter would not longer be in the string

        we get the freq of each letter, then simulate removing each letter by reducing its frequency by 1, then we get the rest of the frequencies left
        freqLeft is an iterable, we then get the frequencies left after we remove 0, eg for aabbc, when we remove c we do not want to consider its 0 frequency

        so if the non-zero frequencies are removing a letter are less than 1, we can return True, else we add back to the frequency of the letter we are at, and try to 
        check the next letters.

        note that we use a set for nonZeroFreqLeft to remove duplicate/same frequencies, eg aabbccd, our hashmap would be {a: 2, b: 2, c: 2, d: 1}, so
        when we remove d, since the rest of the freq are all the same (ie 2), we want them to count as just one freq. not three

        TC: O(N*26) = O(N) since the string can only contain lowercase English letters
        SC: O(N)  
        
        '''
        charFreq = {}

        for char in word:
            charFreq[char] = charFreq.get(char, 0) + 1

        for charToRemove in charFreq:
            charFreq[charToRemove] -= 1

            freqLeft = charFreq.values()

            nonZeroFreqLeft = { freq for freq in freqLeft if freq > 0 }

            if len(nonZeroFreqLeft) <= 1:
                return True

            charFreq[charToRemove] += 1

        return False
        

class Solution:
    def equalFrequency(self, word: str) -> bool:
        '''
        Approach here is to actually simulate removing a letter, that is we decrease its count by 1, then we take max of all the values, so if their 
        frequencies are equal, all the frequencies should be equal to the max freq. for each letter that we reduce its freq, we check the entire hashmap if we find
        any letter with a freq different from our max. We use a boolean check variable to know if we came across a different freq. if we reduce for a letter and we go through
        the hashmap and check is still True, then we can return True.

        Note that we do not check the letter we removed if its new freq is now 0, as that would mess up our answer. take an example of "abc", if we remove a, freq of a turns 0
        while the rest freqs are 1. so the rest of the characters actually have the same freq, and we can only get that if we do not check for the letter we removed
        '''
        wordCount = Counter(word)

        for key in wordCount:
            wordCount[key] -= 1
            maxVal = max(wordCount.values())
            check = True
            for k, v in wordCount.items():
                if key == k and wordCount[key] == 0:
                    continue
                
                if maxVal != v:
                    check = False
            wordCount[key] += 1 
            if check:
                return True
        return False


            
        