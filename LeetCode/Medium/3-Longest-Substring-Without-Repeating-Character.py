class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Most optimal solution
        # This is also O(N) but here we can go directly to the next element after the one that is a duplicate to remove the duplicacy
        # unlike the solution below where we have to move the window one by one and check if there is still a duplicate

        hashMap = {} # to ensure there is no duplicacy
        l = longest = 0

        # more intuitive way of writing the same for loop directly below, we only truly consider it being in the hashmap if its index is within the 
        # range of the substring we are currently looking at
        for r in range(len(s)):
            if s[r] in hashMap and hashMap[s[r]] >= l:
                l = hashMap[s[r]] + 1

            hashMap[s[r]] = r
            longest = max(longest, r - l + 1)

        for r in range(len(s)):
            if s[r] in hashMap:
                l = max(hashMap[s[r]] + 1, l) # max function is used here in case where the element initially occurs is no longer in the window we are considering
            hashMap[s[r]] = r  # update hashMap if present before, or add new elements to the hash
            longest = max(longest, r - l + 1)

        return longest
    
        # this is like the one above, but here we are using a set rather than using a dictionary. and here we keep shifting until we remove the s[r] that has previously been seen
        # unlike the one above where we can figure out which index to go to next exactly
        # TC is still O(N)

        l = 0
        maxLen = 0
        substring = set()
        for r in range(len(s)):
            while s[r] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[r])
            maxLen = max(maxLen, r - l + 1)
 
        return maxLen


        # Better solution, think I came up with this myself. not so right in implementation I think
        # Thought process:
        # Have a set to check for duplicates, keep left & right pointer at 0 
        # loop through the input str and check each time if current char is in set, if not add and increment r, since that is a substr with no duplicate
        # else, delete the char at the left from the substr, move left pointer to the right by 1, check again if duplicate still exists, again and again
       # we remove left pointer since the substr has to follow one another.
       # TC: O(N), SC: O(N)

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
    


        # brute-force  solution:
        # take every element of the string as a start of a sequence till the end and only break if duplicates are found
        # we can check for duplicate in costant time using a set, once duplicate is found we break out of the inner loop and go to the next element in the string to use as the start of the sequence

        # TC: O(N^2), SC: O(N)

        longest = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i, len(s)):
                if s[j] in hashSet:
                    break
                hashSet.add(s[j])
            longest = max(longest, len(hashSet))
        return longest