class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Thought process:
        # Have a set to check for duplicates, keep left & right pointer at 0 
        # loop through the input str and check each time if current char is in set, if not add and increment r, since that is a substr with no duplicate
        # else, delete the char at the left from the substr, move left pointer to the right by 1, check again if duplicate still exists, again and again
       # we remove left pointer since the substr has to follow one another.

        char_set = set()
        l = 0
        max_length = 0
        r = 0

        while r < len(s):
            if s[r] not in char_set:
                char_set.add(s[r])
                max_length = max(max_length, len(char_set))
                r += 1
            else:
                char_set.remove(s[l])
                l += 1
        
        return max_length