class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            # checks if length (window) of substring minus most appearing character which gives amount of charcters we need to change
            # is bigger than the limit of what we can change given by k
            # if so, the window has to shift so we decrease the value of the character at left pointer in the dictionary and shift the left pointer by 1
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1) # then check for max of all the windows we get for the answer
        return res