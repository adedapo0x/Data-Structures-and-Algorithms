class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        Since they can be nodes that might not be connected, we have to check if a province start from each node, and use a set to keep track of 
        nodes that we have visited. we then use dfs to traverse each positions

        Note that we are given input as an adjacency matrix, we could have converted to an adjacency list and used it that way too, (adjacency
        list -> a list which key represents node and the values are arrays of their connections)
        
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



        