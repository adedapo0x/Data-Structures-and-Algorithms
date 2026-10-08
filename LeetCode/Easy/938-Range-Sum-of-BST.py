# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        '''
        Optimal DFS solution, we can use the property of BST to our advantage here, if the current node val is greater than high, 
        we know that all the nodes in the right subtree will be greater than high as well, so we do not consider it, same for if node val is lower than low,
        all left subtree is not considered.
        TC: O(N), SC: O(N)
        '''
        if not root:
            return 0

        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)

        return (root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high))



        # DFS solution, iterate all through the tree and add if valid
        # TC: O(N), SC: O(N) where N is the number of nodes in the tree
        if not root:
            return 0

        res = root.val if root.val >= low and root.val <= high else 0
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)
        return res
