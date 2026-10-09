# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        '''
        approach is to use DFS to taverse the tree in its entirety, while keeping track of values in the path and when we see a node no longer has
        children ie it is a leaf node, we can then store that in res in the format indicated by the question.

        TC: O(n * h), DFS traverse across n nodes, and length of each part is h which is the height of the tree, this cost incurred when copying the path to output list
        the h here for a binary tree can be in worst case O(n) if the tree is skewed or O(logn) if the tree is balanced
        so TC can be O(n^2) or O(nlogn) 
        SC: O(h) due to recursion stack, excluding the output 
        '''
        res = []

        def traverse(node, temp):
            if not node:
                return

            temp.append(str(node.val))

            if not node.left and not node.right:
                res.append('->'.join(temp))
 
            traverse(node.left, temp)
            traverse(node.right, temp)

            temp.pop()

        traverse(root, [])
        return res
