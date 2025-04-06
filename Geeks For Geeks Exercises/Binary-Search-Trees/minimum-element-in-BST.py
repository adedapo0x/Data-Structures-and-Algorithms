'''
Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

Constraints:
0 <= number of nodes <= 105
0 <= node->data <= 105
'''

class Solution:
    #Function to find the minimum element in the given BST.
    def minValue(self, root):
        # iterative approach
        # TC for both iterative and recursive for optimal approach: O(H), SC: O(1)
        if not root:
            return -1
        curr = root
        while curr.left:
            curr = curr.left
        return curr.data
            
        
        # recursive solution        
        if not root.left or not root:
            return root.data
        return self.minValue(root.left)
    
        # A bruteforce way would be to do inorder traversal on the BST and keeping a list as part of the arguments of the recursive functionn
        # We know that inorder traversal of a BST leads to a sorted array, so we can have our preorder recursive function take in root and arr as arguments
        # so as per preorder, we go left, then for the root, we append the value to the arr then we go right, at the end of the recursion, we have a sorted list and can just return the first element in it
        # TC: O(N), SC: O(N)

