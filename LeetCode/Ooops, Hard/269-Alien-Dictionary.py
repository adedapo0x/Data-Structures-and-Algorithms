class Solution:

    def alienOrder(self, words: List[str]) -> str:
        adjList = {c:set() for w in words for c in w} # create a adj list with the unique letters as key 

        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i+1]
            minLen = min(len(word1), len(word2))

            # Here we check for Case 1
            if len(word1) > len(word2) and word1[:minLen] == word2[:minLen]:
                return ""

            for j in range(minLen):
                if word1[j] != word2[j]:
                    adjList[word1[j]].add(word2[j])
                    break
            
        visited = {}
        stack = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for nei in adjList[c]:
                if dfs(nei):
                    return True

            visited[c] = False
            stack.append(c)
            return False
        
        for c in adjList:
            if dfs(c):
                return ""
        
        stack.reverse()
        return "".join(stack)