'''
Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], 
where each adj[i] represents the list of vertices connected to vertex i. 
Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list,
and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.
'''

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

    def dfs(self, adj):
            '''
            Iterative approach to doing the DFS using a stack. We keep it running till the stack is empty that is no more nodes to output. we start with our
            start node in the stack ( 0 if 0-indexed, or 1 if 1-indexed), then we pop, add all its neighbours to the stack, and start popping from the neigghbours in the next
            while iteration , repeat repeat. 

            We use a set to keep track of if we have visited a node i.e has been outputted before, similar to using a set with its index as node
            We are reversing since we want to follow the order given in the question, i.e follow how it is arranged in the adjacency list
            '''
            start = 0
            stack = [start]
            visited = set()
            res = []
            
            while stack:
                node = stack.pop()
                if node in visited: # extra check here is cos we can have the same nodes multiple times in our stack and we only one to output once
                    continue
                    
                visited.add(node)
                res.append(node)
                
                # Add neighbors in reverse order directly
                for neighbor in reversed(adj[node]): # returns an iterator not a list, but it does the job since we are just iterating, could hav used [::-1] here too
                    if neighbor not in visited: # only add to 
                        stack.append(neighbor)
        