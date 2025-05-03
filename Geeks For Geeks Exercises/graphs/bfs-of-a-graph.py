class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        
        import collections
        queue = collections.deque([0])
        visited = [0] * len(adj)
        visited[0] = 1
        res = []
        
        while queue:
            node = queue.popleft()
            res.append(node)
            
            for n in adj[node]:
                if visited[n] != 1:
                    queue.append(n)
                    visited[n] = 1
                    
        return res