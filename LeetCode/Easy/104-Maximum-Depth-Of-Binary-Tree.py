# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # used recursive DFS, so we find the max depth of both the right and left subtree for each node recursively and add 1. notice that we need to add 1
        # TC: O(N), all nodes are visited, 
        # SC: O(h), where h is height, best case for balanced tree is O(logn) where h = logn, worst case is O(n) for degenerate tree where h = n
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)


        # Used BFS here
        if not root:
            return 0
        queue = collections.deque([root])
        length = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            length += 1
        return length

        