class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        The approach here is to start from the beginWord and try and change each character one after the other, and see if it exists
        in the wordSet, we convert the wordList to a set for faster lookup each time we want to check.

        so if we find it in wordSet, it is a valid word on our path to finding the endWord and can be envisioned in our tree.
        We are using BFS to find the shortest path of valid words being changed letter by letter.

        TC: O(M x N x 26) = O(M x N) where M is the length of the wordList and N is the length of each word in the wordList and since we are 
        checking for 26 letters each time, but the 26 is a constant so no issues there.
        because of python, the TC would become O(M x N x N x 26) since strings are not dynamic and we have to create a new string everytime with newWord
        SC: O(M) where M is the length of the wordlist that gets converted to a set
        '''
        wordSet = set(wordList)
        if not endWord or endWord not in wordSet:
            return 0

        queue = collections.deque([(beginWord, 1)])
        wordSet.discard(beginWord)
        
        while queue:
            curr, steps = queue.popleft()
            if curr == endWord:
                return steps
            
            for i in range(len(curr)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    if c == curr[i]:
                        continue 
                    newWord = curr[:i] + c + curr[i+1:]
                    if newWord in wordSet:
                        queue.append((newWord, steps + 1))
                        wordSet.discard(newWord)
        return 0


        # Added another solution for the problem. same approach but here I am using a list here to dynamically change the words

        # queue = collections.deque([(beginWord, 1)])
        # wordSet = set(wordList)
        # if endWord not in wordSet:
        #     return 0

        # wordSet.discard(beginWord)
        # while queue:
        #     word, steps = queue.popleft()
        #     if word == endWord:
        #         return steps
        #     wordL = list(word)
        #     for i in range(len(wordL)):
        #         originalChar = wordL[i]
        #         for ch in range(ord("a"), ord("z") + 1):
        #             wordL[i] = chr(ch)
        #             mutatedWord = "".join(wordL)
        #             if mutatedWord in wordSet:
        #                 queue.append((mutatedWord, steps + 1))
        #                 wordSet.discard(mutatedWord)
        #         wordL[i] = originalChar
        # return 0

        