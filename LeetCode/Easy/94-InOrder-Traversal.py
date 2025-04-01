# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Iterative method of doing inorder traversal. we keep shifting left while the node are not Null, in order to start from the leftmost node,
        all along storing the nodes we come across in our stack. When we get to leftmost, our node.left becomes None and the else statement runs in the next iteration
        we then check if the stack is empty, if at any point it is, then we want to end the traversal as there are no nodes to be found again
        if that is not the case(nodes still dey stack), we remove the topmost(last in), append it to our stack, then move the node to the node to our right to continue traversing
        
        It kinda follows the recursive pattern too, we go left then print/append to result then go right.
        Use pen and paper to dry run if you ever get stuck
        TC: O(N), SC: O(N) or more like height of the binary tree
        """
        stack = []
        inorder = []
        node = root
        while True:
            if node:
                stack.append(node)
                node = node.left
            else:
                if not stack: break
                node = stack.pop()
                inorder.append(node.val)
                node = node.right
        return inorder



        # normal recursive wayy, left - root - right
        order = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            order.append(root.val)
            inOrder(root.right)
        inOrder(root)
        return order
        