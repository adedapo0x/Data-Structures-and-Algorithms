class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        '''
        We use a visited array to keep of track of what we have visited to avoid traversing a cycle which would run indefinitely and not
        having to unnecessarily reprint nodes that we have previously encountered and printed. This is necessary for both directed and non directed graphs.
        A queue is used to maintain the order in which we traversal, it is important to note that the BFS traversal doesn't have to start from the root node, it 
        can be from anywhere in the graph.

        TC: O(N * E) for directed graph and O(N * 2E for undirected graph) which is still reduced to O(N + E) in big O notation, where N = number of nodes/ vertices, E = number of edges
        It is important to note that the TC is O(N + E) and not O(N * E) because the for loop runs for a total of all the edges, not that for each node i.e for each while iteration, that
        the for loop runs E times, no, it is the collective time the for loop run in the entirety of the program that is E, hence O(N + E)

        SC: O(3N) which is simplified to O(N), ie for queue, for visited array and for the res list(if we are considering output in SC)
        '''
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