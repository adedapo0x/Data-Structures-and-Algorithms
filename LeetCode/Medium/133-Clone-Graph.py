"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        DFS Approach:
        Approach here is to clone each original node and then link the new clone to clone of the original node neighbours recursively 
        while traversing through the original graph. We use a map to link the original nodes with its clone so we do not clone the same node twice,
        so the clone function returns a cloned version of the node that goes into it and that gets appended as neighbours

        TC: O(V + E) where V and E are the vertices and edges respectfully as we literally go through each vertex(node) and edge
        '''
        if not node:
            return None 

        oldToClone = {}

        def clone(node):
            if node in oldToClone:
                return oldToClone[node]

            copy = Node(node.val)
            oldToClone[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(clone(n))
            return copy
        
        return clone(node)

        '''
        BFS Approach: We use a queue as usual in BFS and the oldToClone map. So we start with starting node(usually 1 as given in the problem
        statement), putting the node in the queue and storing its clone in the map. then we popleft, go through each of the neighbors and clone and append them
        too
        '''
        if not node:
            return None
        oldToClone = {}

        def clone(node):
            copy = Node(node.val)
            oldToClone[node] = copy
            queue = collections.deque([node])

            while queue:
                curr = queue.popleft()
                for n in curr.neighbors:
                    if n not in oldToClone:
                        copy = Node(n.val)
                        oldToClone[n] = copy
                        queue.append(n)
                    oldToClone[curr].neighbors.append(oldToClone[n])
        
        clone(node)
        return oldToClone[node]
    
        