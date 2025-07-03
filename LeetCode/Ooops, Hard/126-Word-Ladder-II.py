class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        '''
        The approach here is similar to what is done in Word Ladder, only here we are keeping track of the actual words that make up the ladder.
        So we use a BFS that contains list of the words that change a letter at a time to become the endWord. 

        the thing to note here is that when we come across a new word present in our wordSet, we do not remove it yet as other lists[paths formed by words]
        could also yield that same word
        e.g bat - pat - pot , bat - bot - pot, in this case, the second level would consist of [bat, pat] and [bat, bot]. If when we got pot from
        the first list, if we got rid of it we wouldn't have been able to generate the second list. Hence, the solution is to only remove a word after we are done
        with that particular level and at the next level already (here we would be sure no two paths can lead to it)

        We used a used list to keep track of word(s) that we used for a level, and they are henced removed from the set after that level
        '''
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
            
            # checks if this is the first time we get an endWord, if it is, just add normally. But, if we have previously come
            # across a list with the last element as the endWord, we want to check that we are still of the same length since we are looking for the 
            # SHORTEST PATH
            if word == endWord:
                if len(ans) == 0:
                    ans.append(valList)
                elif len(ans[0]) == len(valList):
                    ans.append(valList) 

            for i in range(len(word)): 
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    mutatedWord = word[:i] + c + word[i+1:]
                    if mutatedWord in wordSet:
                        # Here we avoid trying to append to the valList then adding to queue, then popping
                        # in python, a list is passed by reference, so we are still working with the same list all through and we end up with
                        # wrong values in the list on the queue.
                        # solution is to create a copy, by combining valList and an array of mutatedWord into a whole new list
                        queue.append(valList + [mutatedWord])
                        usedList.append(mutatedWord)
        return ans
