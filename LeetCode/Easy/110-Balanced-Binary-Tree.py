# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Came up with this solution myself.
        if not root:
            return True
        status = [True]
        self.getHeight(root, status)
        return status[0]
        

    def getHeight(self, node, status):
        if not node:
            return 0
        left = self.getHeight(node.left, status)
        right = self.getHeight(node.right, status)
        pre = False if max(left, right) > min(left, right) + 1 else True
        status[0] = status[0] and pre
        return 1 + max(left, right)
        