from collections import *
class Solution:
    '''
    Using BFS to find cycles in graph, can handle for both connected and unconnected graphs.
    The approach is to start from a node(start node), keep track of its source/parent for the start node, it can have anything as the parent
    say -1 that is surely not a node in the graph. We also use a visited set or array to keep track of the nodes that we have come across previously.

    Then the traversal starts, we pop, add the neighbours of the node with their parents, repeat and repeat.
    We can say that we have found a cycle if we encounter a node that has been previously visited and it is not the parent of that node, that means
    something else got there first in the traversal, and hence we return True, if the BFS ends and we haven't returned True, we then return False signalling that there
    are no cycles. 

    TC: O(N) + O(V + 2E, O(N) for the outer loop and V + 2E is the TC for the BFS traversal
    SC: O(N)

    '''
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
            
        