# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # TC: O(H) where H is height and is equal to logN, so O(logN)
        curr = root
        while curr and curr.val != val:
            if val > curr.val:
                curr = curr.right
            else:
                curr = curr.left
        return curr
    
        # added recursive solution 
        if not root or root.val == val:
            return root
        if val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
        
        