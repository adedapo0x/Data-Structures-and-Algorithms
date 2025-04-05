# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # my own murky solution after looking at neetcode's hints
        curr = root
        while curr:
            mini, maxi = min(p.val, q.val), max(p.val, q.val)
            if curr.val == p.val or curr.val == q.val or mini < curr.val < maxi:
                return curr
            elif curr.val > mini:
                curr = curr.left
            else:
                curr = curr.right 
        