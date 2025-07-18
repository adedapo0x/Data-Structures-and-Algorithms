class Solution:
    '''
    The main idea behind the solution here is that from the word list given to us, we want to go through consecutive words since they are lexicographically sorted and 
    see the first differing letter, so first differing letter in word1 is lexicographically lesser than the differing letter in word2 since they are sorted.
    so the relationship between these two letters, say a and b is that we get to a before getting to b, something that can be represented in a graph as a -> b
    then since we want to find the sorting in a graph, which is basically topo sort, so we do that and we return that as our answer

    Note that there are two cases where the alien dictionary will not be valid and we have to return "".
    Case 1: When the first word is longer than the second word and there are equal up until where the second shorter word ends, eg 
    [apes, ape], here when comparing the first word is supposed to be lexicographically less than the second word, the word with the extra s cannot be lesser than the one without

    Case 2: If a loop exists in the graph we built, ie when doing our topo sort we discover a loop ie a cycle this is also not valid. E.g
    [ape, ede, ant], here we see that a is before e ie a -> e , then we move to the next pair and we still see that e -> a, so there is no way a is before e and e is still before 
    a, this signifies a loop and hence the dictionary is invalid and we are supposed to return ""
     
    Approach: so first from the input list, we build our adjacency list, we use a set to hold the neighbours to avoid having duplicate letters in there. then we go through the pairs of words and
    traverse through it finding the differing letters and adding them into adj list as nodes and neighbours. then we run topo sort, we use a visited hashmap to denote the nodes we have seen and the nodes still in
    path. Once we visit it, we add it to the adjList and assign True to it, then recursively go through it neighbours assigning True as we are still on the path, then when we are done and returning up the recursion tree
    we give them False as those nodes are no longer on the path we are currently on. We append to our topo stack/array as we return up the recursion

    then as per standard topo sort, we reverse the list or pop from the stack and take the elements as we pop. Note, if any of our DFS returns True, it signifies a loop and we are supposed to stop.

    TC: O(N) + O(K + E) where N is the total number of characters in the word list and K is the number of unique characters and E is the number of edges
    the O(N) is from the building of the graph, and the O(K + E) is from the DFS done to do the topo sort
    '''
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