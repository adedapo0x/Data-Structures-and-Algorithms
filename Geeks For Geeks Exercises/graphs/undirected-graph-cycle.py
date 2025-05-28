from collections import *
class Solution:
    def isCycle(self, V, edges):
        adj = defaultdict(list)
        visited = set()
    
        for val1, val2 in edges:
            adj[val1].append(val2)
            adj[val2].append(val1)
           
        def detect(first):
            queue = deque([(first, -1)])
            visited.add(first)
            while queue:
                node, parent = queue.popleft()  
                for val in adj[node]:
                    if val not in visited:
                        visited.add(val)
                        queue.append((val, node))
                    elif (val != parent):
                        return True
            return False
    
        for i in range(V):
            if i not in visited:
                if detect(i):
                    return True
        return False
            
        