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

            
        