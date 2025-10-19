"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        '''
        Here we use a queue to do normal BFS, it doesn't matter if some nodes are absent for a particular level. the BFS would keep track of all the available nodes for a particular
        level and these are the ones we have interest in connecting their next together. so we keep on connecting their .next together as long as the queue is of size 2 and above, 
        cos if the queue gets reduced to size 1, we then pop, there would be nothing in queue[0] for us to connect to

        TC: O(N), SC: O(N)
        '''
        if not root:
            return root
        queue = collections.deque([root])

        while queue:
            size = len(queue)
            while size > 0:
                node = queue.popleft()
                if size > 1:
                    node.next = queue[0]
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                size -= 1
        return root

        