# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # iterative clean solution, TC: O(H) where H is the height of the tree which is usually logn for BST
        # The logic is once both p and q values given are greater than the value of the current node that we are in, there is no way that is
        # going to be an ancestor since the tree is a BST, hence we have to go right. Same is true for the opposite, i.e when p and q values are both
        # less than the current node we are on value, then obvs there is still an ancestor to the left, so we have to shift to the left.
        # 
        # Should the node value we are on be equal to either of the p and q given, or if our curr node value is in between p and q, lesser than one
        # but greater than the other, through examples we see that the node would also be our LCA, this is what is covered by the else statement and we just have to return that node. 
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr




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
        