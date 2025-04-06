# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # clean recursive DFS solution, uses like preorder traversal. 
        # TC: O(p + q)
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        return False # handles condition when one is null, the other is a node, and also when both are nodes but their values are not equal


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


        