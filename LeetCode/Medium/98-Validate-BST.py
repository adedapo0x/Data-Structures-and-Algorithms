# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:  
        '''
        Approach here is to use boundaries, we know that for each node there is something that it must not be less than or something it must not be greater than
        so here we recursively check if the val of each node obeys that law. If not node, we return True, as that is technically a valid BST

        so in each time we explore a .left we use a new right limit, since that element at the left must not be greater than its parent. Aso, when we explore .right,
        we update our left limit, because that number at the right has to be greater than its parent.

        TC: O(N), SC: O(N) where N is the number of nodes in the treee
        '''

        def validateTree(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return (validateTree(node.left, left, node.val) and 
            validateTree(node.right, node.val, right))
        
        return validateTree(root, float("-inf"), float("inf"))