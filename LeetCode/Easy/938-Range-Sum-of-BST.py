# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        # DFS solution, iterate all through the tree and add if valid
        # TC: O(N), SC: O(N) where N is the number of nodes in the tree
        if not root:
            return 0

        res = root.val if root.val >= low and root.val <= high else 0
        res += self.rangeSumBST(root.left, low, high)
        res += self.rangeSumBST(root.right, low, high)
        return res
