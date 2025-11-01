class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Approach here is to use tabulation (bottom up approach) DP. here we take a list that contains boolean values for each index of s if a
        segmentation can be made at that index. since s[a:b] doesn't include b, when we give dp[] its size, it has to be len(s) + 1, since to cover the end of the string
        at len(s) - 1, our index would be at len(s) and arrays initializing would have done 0 to n - 1

        we set dp[0] to True as this is the trivial case in our bottom up, an empty string can always be segregated. we then start looping from index 1, ie covering only the 
        first character at index 0 using variable i, the j is to use traverse from 0 up until i to check if there is a possible segregation between 0 and j-1, and j to i - 1
        here we rely on previously solved overlapping subproblems, hence why it is DP. for each i, we go using j from 0 to i, to check, since our initial j = 0, dp[j] is always true, 
        we are looking for a segmentation from 0 up until that index. once we find one, that dp[j] = True and that word after j to i-1 is in wordSet, that means thats two words from j to i - 1

        as we go once we find a possible segmentation, we mark that index as True in our dp[], break, then continue the loop for i, 
        we know that once we reach the end of the string and we mark it as true, that means there is a valid segmentation path from the start of the string to the end of the string
        so we return dp[len(string)] since that covers up until the end of the string at index len(s) - 1

        TC: O(N^2), SC: O(N)
        '''
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
            
        return dp[len(s)]




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
        bruteforce approach, gets TLE on Leetcode, here we do recursion, 
        we start from every index in s and we check if that substring is in wordSet (convert to set for O(1) lookup)
        if it is, we shift start to the end of the valid index and call the dfs to check for the next substring
        once we get to the end of s we can return True

        e.g s = "bloomberg", and wordSet = { bloom, berg, bloomber }
        we check from b up until m, we see that bloom is in our set, so that is covered, we then make a call from b in berg and we get that berg to later and
        return True as we go up the recursion tree. 
        say we had an example s = "bloomber", we go bloom, we see that it in set, then we call for b in ber, but there is no ber, so we finish the iteration without calling our recursive check
        then we return to index 5, then iteration continues checking if bloomb or bloombe, then finally bloomber is valid

        for TC: because at every index we can choose whether to pick our segregation from ther or not, we end up having 2 choices of recursion per index
        and this grows exponentially and hence not accurate, so TC is O(n.2^n), the extra n is cost of from the string slicing we do for every valid word
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