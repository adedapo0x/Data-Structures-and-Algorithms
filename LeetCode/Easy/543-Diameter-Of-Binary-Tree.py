# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        '''
        Optimal solution, TC: O(N), rather than doing that for each node we encounter, we look for its left and right subtree height then add and compare,
        here, we do it together, as we get the left and right height of each node that we come across, we calculate the maximum path(diameter) that could be gotten if 
        that node was the meeting point/curvature of the two subtrees that would make up the path, and at the same time computing the heights to be used.

        Note that for our maxi that we return, we are using a list to store it, cos if we store it as a normal variable, we get error, cause it won't be able to be accessed
        by the outer method and we would prolly have to do it like the second solution, using the nonlocal or global keyword.

        Took a while to wrap my head around the solution from Striver sef, lmao
        '''
        maxi = [0]
        self.getHeightAndMaxi(root, maxi)
        return maxi[0]
    
    def getHeightAndMaxi(self, node, maxi):
        if not node:
            return 0
        left = self.getHeightAndMaxi(node.left, maxi)
        right = self.getHeightAndMaxi(node.right, maxi)
        maxi[0] = max(maxi[0], left + right)
        return 1 + max(left, right) 

        '''
        Less optimal solution here, uses TC of O(N^2). gets TLE on leetcode
        The approach here is to add the height of the left and right subtree of a node and we get the diameter (longest path), with that node which we are
        taking to find left and right of, as the curvature point of the two nodes mentioned in the question connection path.
        It is very important to note that we necessarily do not have to go through the root, there could be other longer connection paths between two nodes that do not
        involve the root, so because of this, we have to do the adding up of the sum of the left and right subtree of each node, not just that of the root node
        
        We are implementing this recursively, first we have a helper recursive function that gets the maximum length between the right and left subtree of a node, then
        we use that for each node starting from the root to find the left and right subtree height, then we sum it up updating our global result variable maxi if we have seen
        a bigger connection path (diameter)
        '''
        maxi = 0
        def findDiameter(node): # 
            nonlocal maxi # using nolocal here because inside this inner function it is going to treat maxi as another separate variable which we have not previously instantiated
            if not node:  # note that we could just put maxi in an array, that'll make it a reference that can be accessed inside the inner arrayy
                return
            l = self.getHeight(node.left)
            r = self.getHeight(node.right)
            maxi = max(maxi, l + r)
            findDiameter(node.left)
            findDiameter(node.right)
        findDiameter(root)
        return maxi
    
    def getHeight(self, node):
        if not node:
            return 0
        left = self.getHeight(node.left)
        right = self.getHeight(node.right)
        return 1 + max(left, right)



        