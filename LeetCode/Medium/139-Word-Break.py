class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Here, we use memoization, that is the only difference with what is in the bruteforce, we save ourselves the cost of having to recompute whether a segmentation
        can be made while starting from an index by storing the answer in a dict the first time the result for that index returns, whether True or False

        and because with this we get rid of unnecessary revisitations,
        the TC collapses from being exponential to being quadratic,
        for each unique start position, we can check from start + 1 up until end so that is basically O(n^2)
        TC: recursion depth + memo dictionary, and our set too, so O(N)
        
        '''
        n = len(s)
        wordSet = set(wordDict)
        memo = {}

        def check(start):
            if start == n:
                return True

            if start in memo:
                return memo[start]

            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet:
                    if check(end):
                        memo[end] = True
                        return True

            memo[start] = False
            return False
        return check(0)
        '''
        bruteforce approach, here we do recursion, 
        we start from every index in s and we check if that substring is in wordSet (convert to set for O(1) lookup)
        if it is, we shift start to the end of the valid index and call the dfs to check for the next substring
        once we get to the end of s we can return True

        e.g s = "bloomberg", and wordSet = { bloom, berg, bloomber }
        we check from b up until m, we see that bloom is in our set, so that is covered, we then make a call from b in berg and we get that berg to later and
        return True as we go up the recursion tree. 
        say we had an example s = "bloomber", we go bloom, we see that it in set, then we call for b in ber, but there is no ber, so we finish the iteration without calling our recursive check
        then we return to index 5, then iteration continues checking if bloomb or bloombe, then finally bloomber is valid

        for TC: because at every index we can choose whether to pick our segregation from ther or not, we end up having 2 choices of recursion per index
        and this grows exponentially and hence not accurate, so TC is O(n.2^n), the extra n is cost of going over all the ends when start from a start
        and SC is O(N), recursion call stack + set
        '''
         
        

        wordSet = set(wordDict)
        n = len(s)

        def check(start):
            if start == n:
                return True

            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet:
                    if check(end):
                        return True

            return False

        return check(0)