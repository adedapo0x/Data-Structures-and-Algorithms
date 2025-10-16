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


            
        