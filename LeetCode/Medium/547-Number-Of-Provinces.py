class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Since they can be nodes that might not be connected, we have to check if a province start from each node, and use a set to keep track of 
        nodes that we have visited. we then use dfs to traverse each positions

        Note that we are given input as an adjacency matrix, we could have converted to an adjacency list and used it that way too, (adjacency
        list -> a list which key represents node and the values are arrays of their connections)

        TC: O(N) + O(V + 2E) where N is for the outer loop and V + 2E is for TC for DFS of an undirected graph.
        SC: O(N) + O(N) for visited set and stack space
        '''
        ROWS = len(isConnected)
        visited = set()
        count = 0

        def dfs(pos):
            if pos in visited:
                return
            visited.add(pos)
            for i in range(len(isConnected[pos])):
                if i != pos and isConnected[pos][i] == 1:
                    dfs(i)

        for r in range(ROWS):
            if r not in visited:
                count += 1
                dfs(r)
        return count
    

        '''
        Another way that converts the list given to an adjacency list (hashmap for easier intuition)
        problem is we use extra time and space
        '''
        adjDict = {}

        for i in range(len(isConnected)):
            adjDict[i] = []
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    adjDict[i].append(j)
        
        visited = set()

        def dfs(val):
            visited.add(val)
            for n in adjDict[val]:
                if n not in visited:
                    dfs(n)


        provinces = 0
        for i in range(len(isConnected)):
            if i not in visited:
                provinces += 1
                dfs(i)

        return provinces



        