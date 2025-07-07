from collections import defaultdict
'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge from verticex u to v.
'''

class Solution:
    def isCycle(self, V, edges):
        '''
        The approach is to keep a visited and a pathVisited array that keeps track of what we have visited. The pathVisited is to ensure that the cycle occurs on the
        same path that we are currently traversing. Once we go back in the recursion, we mark those as 0 in the pathVisited, so a cycle only occurs if we come across a node 
        that has been previously marked in our visited array and we are still on the same cycle.

        TC: O(V + E)
        '''
        adjList = defaultdict(list)
        visited = [0] * V
        pathVisited = [0] * V 

        for node, neighbour in edges:
            adjList[node].append(neighbour)
            
        def dfsCheck(node):
            visited[node] = 1
            pathVisited[node] = 1
            
            for n in adjList[node]:
                if visited[n] == 0:
                    if dfsCheck(n):
                        return True
                elif pathVisited[n] == 1:
                    return True
            
            pathVisited[node] = 0
            return False
        
        
        for i in range(V):
            if visited[i] == 0:
                if dfsCheck(i):
                    return True
        return False