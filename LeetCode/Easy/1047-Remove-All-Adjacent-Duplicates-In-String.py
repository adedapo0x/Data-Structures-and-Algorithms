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