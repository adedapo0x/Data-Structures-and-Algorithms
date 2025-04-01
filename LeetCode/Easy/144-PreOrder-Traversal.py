# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative better way of doing it
        # We use a stack, adding to it right then left, this is because stacks are LIFO, we need left before right and we can get it since it
        # is the last thing we add to the stack
        #TC: O(N), SC: O(H) where H is the height, cos the maximum number of nodes that can be in the stack at a time is of same number as height of the tree
        # which happens when the tree is skewed I think
        preorder = []
        if not root:
            return preorder
        stack = [root]
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder

        # Normal recursive way for doing preorder
        res = []
        def preOrder(root):
            if not root:
                return
            res.append(root.val)
            preOrder(root.left)
            preOrder(root.right)
        preOrder(root)
        return res

        
        