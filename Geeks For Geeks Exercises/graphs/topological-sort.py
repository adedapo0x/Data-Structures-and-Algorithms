'''
Given a Directed Acyclic Graph (DAG) of V (0 to V-1) vertices and E edges represented as a 2D list of edges[][],
where each entry edges[i] = [u, v] denotes a directed edge u -> v. Return the topological sort for the given graph.

Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u -> v,
vertex u comes before v in the ordering.

Note: As there are multiple Topological orders possible, you may return any of them. If your returned Topological sort is correct then the output will be true else false.
'''

from collections import defaultdict
class Solution:
    
    def topoSort(self, V, edges):
        adj = defaultdict(list)
        visited = set()
        stack = []
        ans = []
        
        for i in range(len(edges)):
            adj[edges[i][0]].append(edges[i][1])
                
        
        def dfs(node):
            visited.add(node)
            
            for n in adj[node]:
                if n not in visited:
                    dfs(n)
            stack.append(node)
        
        for i in range(V):
            if i not in visited:
                dfs(i)
                
        while stack:
            ans.append(stack.pop())
            
        return ans
            
            