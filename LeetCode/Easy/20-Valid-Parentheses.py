from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # using an helper function
        if len(s) < 2:
            return False
        stack = deque()
        def matches(c1, c2):
            obj = {
                "(": ")",
                "{": "}",
                "[": "]"
            }
            return obj[c1] == c2

        for ch in s:
            if ch == "(" or ch == "{" or ch == "[":
                stack.append(ch)
            elif ch == ")" or ch == "}" or ch == "]":
                if len(stack) == 0:
                    return False
                if not matches(stack.pop(), ch):
                    return False
        if len(stack) != 0:
            return False
        return True
                
