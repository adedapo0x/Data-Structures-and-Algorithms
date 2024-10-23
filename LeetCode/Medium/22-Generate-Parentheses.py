class Solution:
    def generateParenthesis(self, n: int):
        # Note to self: Neetcode used a stack solution, this doesn't and is more simpler and straightforward
        # major concept here is backtracking, which I am yet to get very familiar on
        res = []

        def backtrack(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            
            if left < n:
                backtrack(left + 1, right, s + "(")

            if right < left:
                backtrack(left, right + 1, s + ")")

        backtrack(0, 0, "")
        return res
        