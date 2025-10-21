class Solution:
    def removeDuplicates(self, s: str) -> str:
        '''
        Stack approach, we put in the stack if element in top of stack and where we are currently in string do not match, if they do, means duplicates, 
        so we pop from the stack and move to the next character in the string

        TC: O(N), SC: O(N)
        '''
        stack = []

        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)


        '''
        Doesn't work in Python!
        The purpose of this is to get an O(1) space solution without a stack. We cannot do this in Python since strings are immutable, so we cannot directly assign a character to an index eg s[i] = c, 
        To get constant space, we could simulate the stack in the string without actually using the stack. we keep pointer i to denote where the simulated stack is, and c is used 
        to traverse the array, so if we come across a lettter that is in s[i-1] that is the top of the simulated stacck that means there are adjacent duplicates, then we can decrement 
        i by one to reduce the simulated stack. If the elements are different we update the the indx i and move forward

        
        '''
        i = 0

        for c in s:
            if i > 0 and s[i-1] == c:
                i -= 1
            else:
                s[i] = c
                i += 1
        return s[:i]

        '''
        bruteforceyy, gets TLE on Leetcode
        Here, we basically do what the questions ask, we scan through the string, if we see duplicates of size 2 we get rid of them then we start 
        from the beginning again to look for duplicates

        TC: O(N^2)
        SC: O(1)
        
        '''
        i = 0

        while i < len(s) - 1:
            if s[i] == s[i+1]:
                s = s[:i] + s[i+2:]
                i = 0
            else:
                i += 1

        return s