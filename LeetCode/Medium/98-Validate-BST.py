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
    

        # we could do something very similar to approach above using BFS, same TC and SC


        '''
        Another way of doing this without keeping track of boundaries is to use inorder traversal, inorder works as left - parent - right, so we need left to be lesser than parent
        and parent lesser than right in a BST so we can use inorder for this here.

        we use a prev which is initialized to negative infinity because the leftmost node val can be anything, so we want something that'll definitely be lesser than it
        as we traverse our tree, prev will hold the last node value we just saw to allow us compare for BST validity
        we go to the absolute left of the tree using inorder traversal and start our check from there, then compare with parent, update prev, then compare with right 

        using nonlocal for prev since we wouldn't be able to access prev inside the recursive function otherwise. note not to include prev as a parameter in the recursive function as this is something that is 
        constantly changing and the prev int value we called up in the recursion prolly with float(-inf) would not be the same prev we currently have, one way we could put it as a parameter
        is to use a list, like [prev] so we initially call it with [float("-inf)], this way the prev value would be dynamic

        TC: O(N), SC: O(N)
        '''

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
                                                        
        def inorderValidate(node):
            nonlocal prev
            if not node:
                return True

            if not inorderValidate(node.left):
                return False

            if node.val <= prev:
                return False

            prev = node.val
            return inorderValidate(node.right)

        prev = float("-inf")
        return inorderValidate(root)

        