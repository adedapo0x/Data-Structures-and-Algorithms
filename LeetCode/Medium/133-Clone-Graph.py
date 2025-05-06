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

            
        