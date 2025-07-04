from collections import deque, defaultdict
class Solution:

    def topoSort(self, V, edges):
        queue = deque()
        
        adj = defaultdict(list)
        
        for node, neigh in edges:
            adj[node].append(neigh)
        
        indegree = [0] * V
        
        for node, neigh in edges:
            indegree[neigh] += 1
            
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        ans = []   
        while queue:
            node = queue.popleft()
            ans.append(node)
            
            for n in adj[node]:
                indegree[n] -= 1
                
                if indegree[n] == 0:
                    queue.append(n)
                    
        return ans