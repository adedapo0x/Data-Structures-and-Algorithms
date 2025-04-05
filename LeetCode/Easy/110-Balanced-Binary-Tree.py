# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Came up with this solution myself.
        # TC: O(N)
        if not root:
            return True
        status = [True] ## Using this cos of I need it in a reference rather than as a primitive
        self.getHeight(root, status)
        return status[0]
        

    def getHeight(self, node, status):
        # gets the height while checking the status of the tree at the same since it is passed as an argument
        if not node:
            return 0
        left = self.getHeight(node.left, status)
        right = self.getHeight(node.right, status)
        pre = False if max(left, right) > min(left, right) + 1 else True # checks if the diff between subtree height is more than 1
        status[0] = status[0] and pre
        return 1 + max(left, right)
    

        # Naive / bruteforce solution, 
        # For each node we first get the left and right subtree height then check if it is balanced, then we move on to the children to get
        # their own length and this keeps on repeating till we get to the leaf nodes.
        # TC: O(N^2) since for each node we have to get their left and right subtree which means having to traverse the rest of the tree each time for each node
        if not root:
            return True
        lH = self.getHeight(root.left)
        rH = self.getHeight(root.right)
        if abs(lH - rH) > 1:
            return False
        left = self.isBalanced(root.left)
        if not left: return False
        right = self.isBalanced(root.right)
        if not right: return False

        return True


    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return 1 + max(left, right)

        