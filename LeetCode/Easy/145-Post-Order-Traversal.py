# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iterative approach, uses two stack. Initially the root is put in stack1 before the traversals begin, then we pop from stack1, append to stack2
        # then check if the node we popped had a left or right child, if it does, append those to stack1, then on second loop, pop from stack1 again and repeat
        # this goes on until the stack1 becomes empty(i.e we have gotten to every node), then we start popping from our stack2 and we notice that our result is exactly like 
        # what we would get for postorder traversal
        # TC: O(N), SC: O(2N) since we are using two stacks
        postorder = []
        if not root:
            return postorder
        stack1, stack2 = [root], []
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        while stack2:
            node = stack2.pop()
            postorder.append(node.val)
        return postorder


        # normal recursive postorder traversal
        order = []
        def postOrder(root):
            if not root:
                return
            postOrder(root.left)
            postOrder(root.right)
            order.append(root.val)
        postOrder(root)
        return order
        