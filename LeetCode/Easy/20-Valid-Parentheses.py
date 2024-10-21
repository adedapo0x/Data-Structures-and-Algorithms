from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # first solution; without helper function

        stack = deque()

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if (len(stack) == 0
                or (ch == ')' and stack[-1] != '(') 
                or (ch == '}' and stack[-1] != '{') 
                or (ch == ']' and stack[-1] != '[')):
                    return False
                stack.pop()
        return not stack
    

        # using an helper function
        # if len(s) < 2:
        #     return False
        # stack = deque()
        # def matches(c1, c2):
        #     obj = {
        #         "(": ")",
        #         "{": "}",
        #         "[": "]"
        #     }
        #     return obj[c1] == c2
         
        # for ch in s:
        #     if ch == "(" or ch == "{" or ch == "[":
        #         stack.append(ch)
        #     elif ch == ")" or ch == "}" or ch == "]":
        #         if len(stack) == 0:
        #             return False
        #         if not matches(stack.pop(), ch):
        #             return False
        # if len(stack) != 0:
        #     return False
        # return True
                