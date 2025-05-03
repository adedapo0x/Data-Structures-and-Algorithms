class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        '''
        Recursive Approach:
        Recursively go to the depth of each till there is no where to go then we return and explore another path
        we run a loop through each neighbours in the adjacency list, going to the absolute depth of one neighbour before exploring the other
        TC: O(N) + O(2E) for undirected, and O(N) + O(E) , same reason as one I gave in bfs-of-a-graph. 
        SC: O(N), simplified from space gotten from visited, res ( if we consider it), and the recursion auxilliary stack space
        '''
        res = []
        visited = [0] * len(adj)
        start = 0
        self.doDfs(start, adj, res, visited)
        return res
        
    def doDfs(self, node, adj, res, visited):
        res.append(node)
        visited[node] = 1
        
        for n in adj[node]:
            if visited[n] != 1:
                self.doDfs(n, adj, res, visited)