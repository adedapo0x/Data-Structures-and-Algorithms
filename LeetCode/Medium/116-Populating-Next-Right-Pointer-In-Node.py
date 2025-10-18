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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
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
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        Approach here is still bfs like, but without the queue, curr is for the node we are in, next is for the start of the next level which is initially
        root.left, so while curr and next are valid, we connect the left child node to the right, in the case that there is still more to connect, the curr will have a .next, 
        then we connect it's right child node to the next node left, since that is what is by its right, we then shift our curr to that next node, and continue from there

        when we get to the end for a level, ie there is no curr.next, we need to go to the next level, so we update our curr to the beginning of the next level, and update the 
        what we are using to store next level start which is the next variable. the loop ends when we are done with the leaf nodes as there would be no next level

        TC: O(N), SC: O(1)
        '''
        if not root:
            return root

        curr, next = root, root.left
        while curr and next:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left

            curr = curr.next
            if not curr:
                curr = next
                next = curr.left

        return root



        '''
        Approach here is to use standard BFS, on each level we connect the next pointer to the next node in that level. until the size of the queue for that level is 1. 
        then we know that the node is not going to have anything by its right

        TC: O(N), SC: O(N/2) when the queue holds all the leaf nodes and we can simplify to O(n)
        '''
        if not root:
            return None

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
        

        '''
        Optimal DFS approach, similar idea to the optimal BFS solution.
        
        TC: O(N), SC: O(1) since we do not consider the stack space
        '''
        if not root:
            return root

        if root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        return root
