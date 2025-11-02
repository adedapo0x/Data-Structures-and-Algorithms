class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        Dp bottom up approach (tabulation) used here. we take a dp array of len(s) + 1, in order to hold for len(s). this array[i] stores the
        sentences that can be created from the beginning of the string up until that index i. we set dp[0] to contain an empty string because that is 
        the base case, 0 doesn't cover any string and is such assigned an empty string

        so we go from 1 to len(s) using i, then our inner j checks from 0 up until i for valid sentences in our wordDict. so when we see a valid sentence from s[j:i],
        we take all the prev valid sentences we have formed from dp[j] and add it to the word we found at s[j:i] then use it to populate dp[i], if there was no 
        previous word there, say we are just starting out, say s[0:3] and what is in s[0] is "", we want to make sure we do not add any unnecessary space, that is why we have to check 
        if there is a prevSentence, that determines if we just append to dp[i] or we have to add to prevSentence with space before appending

        we then return dp[len(s)], this would contain an array of sentences that has been formed from the start of the string right up until we get to the end of s

        TC: O(N^2 + T) where T is the cost of exploring all possible paths if every substring is valid , T can be O(2^n)
        SC: O(n + T), O(N) because of set, and T because of the dp array holding all possible valid sentences
        
        '''




        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]
        wordSet = set(wordDict)

        for i in range(1, len(s) + 1):
            for j in range(i):
                word = s[j:i]
                if word in wordSet:
                    for prevSentence in dp[j]:
                        if prevSentence:
                            dp[i].append(prevSentence + " " + word)
                        else:
                            dp[i].append(word)
        return dp[len(s)]




class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        '''
        The memoization DP approach, here we use a memoization hashmap to store previously computed values for each index so we do not have to recompute them again
        the values here is, for each index, we get the sentences that could be segregated to the end from that index, and we store it in the hashmap
        so i : ["abc de", "abc d e"], so that way if we come across the index again no need to do recursive calls for it again

        when we makek a recursive call with start as the length of s, ie we have covered the entire string, and we return [""], this is for the prefix that comes before it to be added to it
        we store the strings in a list, because there could be multiple segregations to the end of the string made from a single index, it depends on what is in wordDict

        so if we have s[start:end] in wordSet, we keep that as prefix, then check further down s starting from end, we only want to start populating the memo hashmap and returning and appending and all
        if we get to the base case, that way we would have a tail returned that is appended to prefix. the res there holds all possible segregation for that index
        when all the recursive calls are complete, we return res like we did during recursion since res would now contain all the sentences that can be formed with spaces starting from 0

        TC: best or average case is O(N^2 + T) where T is the total length of all valid sentences generated
        worst case could still be exponential, O(N.2^N) as we have to explore all possible combinations in a case such as "bbbbbb.." where b, bb, bbb, ... are all in the 
        dictionary, ie where every suffix and prefix is valid.

        SC: O(N + T) where recursion stack space can grow up until O(N) and T is for the sentences that could be generated which in the worst case would
        have a size of 2^n, so SC could be O(N + 2^N)
        '''
        wordSet = set(wordDict)
        memoization = {}

        def generateSentence(start):
            if start == len(s):
                return [""]

            if start in memoization:
                return memoization[start]

            res = []
            for end in range(start + 1,len(s) + 1):
                prefix = s[start:end]
                if prefix in wordSet:
                    remainingSentence = generateSentence(end)
                    for tail in remainingSentence:
                        sentence = prefix + ("" if tail == "" else " " + tail)
                        res.append(sentence)

            memoization[start] = res
            return res

        return generateSentence(0)
    



'''
Bruteforce approach, here we basically just explore all possible paths that could generate valid sentences, building in temp and when we get to the end
of the string meaning we have covered all, we can then append the sentence to res.

TC: O(N*2^N) cost of visiting every possible valid path and string slicing done at them
SC: O(2^N) complexity for all valid path (sentences) that needs to be stored
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        res = []

        def findWords(start, temp):
            if start == len(s):
                res.append(" ".join(temp))
                return

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    temp.append(word)
                    findWords(end, temp)
                    temp.pop()

        findWords(0, [])
        return res


        