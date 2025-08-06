class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # TC: O(N), SC: O(M) where N is the length of the string and M is the number of unique characters in the string
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # checks if length (window) of substring minus most appearing character which gives amount of charcters we need to change
            # is bigger than the limit of what we can change given by k
            # if so, the window has to shift so we decrease the value of the character at left pointer in the dictionary and shift the left pointer by 1
            while (r - l + 1) - max(count.values()) > k and l <= r:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) # then check for max of all the windows we get for the answer
        return res
    

        # implemented without iteration done by count.values()

        # l, r = 0, 0
        # count = {}
        # maxLength, maxCount = 0, 0
        # while r < len(s) and l <= r:
        #     count[s[r]] = 1 + count.get(s[r], 0)
        #     maxCount = max(maxCount, count[s[r]])
        #     if (r - l + 1) - maxCount > k:
        #         count[s[l]] -= 1
        #         l += 1
        #     else:
        #         maxLength = max(maxLength, (r - l + 1))
        #     r += 1
        # return maxLength



        '''
        The bruteforce approach to this problem. The intuition is similar, but we do not use sliding window pattern here
        we  determine the amount of letters that needs changing by taking the subtraction of the length of the substring to the max frequence of 
        letters in the substring

        so we start from the beginning of the string, using a hashmap for each outer iteration, this is used to keep frequency of the letters in the substring,
        then we calculate if we can change (ie still within limit of k), once we aren't we break and we start checking from the next letter 

        TC: O(N^2), SC: O(M) where N is the length of the string and M is the number of unique characters in the string
        '''
        maxLen = 0

        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                if (j - i + 1) - max(count.values()) <= k:
                    maxLen = max(maxLen, j - i + 1)
                else:
                    break
        return maxLen
                
