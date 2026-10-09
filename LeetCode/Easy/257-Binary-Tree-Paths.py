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
    



        '''
        approach uses iterative method of iterating through the tree with a stack to store paths, we do not use recursion here
        stack stores (node, and path up until that node), so when we see a node with no children, we can then add to our results list which is path
        TC: O(N * h) , where N is number of nodes and H is the height of the tree, h comes from the cost of creating a new string if the node is at depth h
        and SC: O(h) stack
        '''
        paths = []
        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()

            if not node.left and not node.right:
                paths.append(path)
                continue

            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))

        return paths

