# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        Approach here is to try to check if there both root and subroot initially given are the same tree(use helper function here), if so return True, that's best case
        if not check if subroot is the same tree as the left subtree of the root, or check if it is same as the rightsubtree, we only need one subtree to be the same as the
        subroot so we use an OR, so we do this recursively. Checking for each node in our root tree if it is the same as the subtree

        Base cases used in the isSubtree; (if not subRoot) ie if the subRoot initially given is None, we return True since it is always a None tree is always a subroot of a tree
        Second one (not root and subRoot) is if root was initially None or during recursion, for the root tree, we get to a node that is None but our subtree still exists, then it is def False
        as a existing node cannot be a subtree to a None node

        TC: O(N * M) where N and M are the number of nodes in N and M respectively
        SC: O(H) which is O(N) for worst case scenario in a skewed tree
        '''
        if not subRoot:
            return True
        if not root and subRoot:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, root, sub):
        if not root and not sub:
            return True
        if root and sub and root.val == sub.val:
            return (self.isSameTree(root.left, sub.left) and self.isSameTree(root.right, sub.right))
        return False


