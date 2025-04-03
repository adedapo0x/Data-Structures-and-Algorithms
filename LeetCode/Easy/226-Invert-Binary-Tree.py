# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Uses recursive DFS (preorder, since root is processed before it goes left and right)
        if not root:
            return 
        root.right, root.left = root.left, root.right
        self.invertTree(root.left)
        self.invertTree(root.right)
    
        return root
    
        # Uses iterative DFS
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            node.right, node.left = node.left, node.right
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return root


        # Using BFS to invert
        if not root: return None
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            node.right, node.left = node.left, node.right
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root
        
        
        