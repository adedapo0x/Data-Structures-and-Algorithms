# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: TreeNode | None, low: int, high: int) -> TreeNode | None:
        '''
        we check if the value of each node is in the within low and high, if not we only consider the appropriate subtree given the properties of BST
        if it is not, we skip left subtree if it is too low, as the left subtree will be even lower, and we skip the right subtree if it is too high, 
        as the right subtree will be even higher. If it is in range, we keep it and check both subtrees (right and left)
        TC: O(N), SC: O(N) for the recursion stack. N is the number of nodes in the tree
        '''
        if not root:
            return None

        if root.val > high:
            return self.trimBST(root.left, low, high)

        if root.val < low:
            return self.trimBST(root.right, low, high)

        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root


        