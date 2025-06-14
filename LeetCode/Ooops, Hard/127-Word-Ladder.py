class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        The approach here is to start from the beginWord and try and change each character one after the other, and see if it exists
        in the wordSet, we convert the wordList to a set for faster lookup each time we want to check.

        so if we find it in wordSet, it is a valid word on our path to finding the endWord and can be envisioned in our tree.
        We are using BFS to find the shortest path of valid words being changed letter by letter.

        TC: O(M x N x 26) = O(M x N) where M is the length of the wordList and N is the length of each word in the wordList and since we are 
        checking for 26 letters each time, but the 26 is a constant so no issues there.
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





        