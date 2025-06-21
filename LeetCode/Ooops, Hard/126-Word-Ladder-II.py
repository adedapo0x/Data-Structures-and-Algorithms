class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordSet = set(wordList)
        queue = collections.deque([[beginWord]])
        usedList = [beginWord]
        level = 0
        ans = []

        while queue:
            valList = queue.popleft()
            word = valList[-1]

            if len(valList) > level:
                level += 1
                for val in usedList:
                    wordSet.discard(val)

            
            if word == endWord:
                if len(ans) == 0:
                    ans.append(valList)
                elif len(ans[0]) == len(valList):
                    ans.append(valList) 

            for i in range(len(word)): 
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    mutatedWord = word[:i] + c + word[i+1:]
                    if mutatedWord in wordSet:
                        queue.append(valList + [mutatedWord])
                        usedList.append(mutatedWord)
        return ans
