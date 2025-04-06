# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # came up with this solution myself, lmao. not straightforward at all, an AC tho, so a W for me
        # did a postorder traversal on this one 
        if not p and not q:
            return True
        if (p and not q) or (q and not p): return False
        left = self.isSameTree(p.left, q.left)
        if not left: return False
        right = self.isSameTree(p.right, q.right)
        if not right: return False
        return p.val == q.val


        