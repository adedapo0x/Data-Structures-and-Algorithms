# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Uses standard BFS, when we are at the last element for a level, that is its rightmost and we can append that into res
        '''
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        dfs approach to solving this, similar to how we went about dfs approach of 102 and 103
        we keep track of the depth as we go down the tree, once we come across the start of a new level, ie a new depth, then len of our
        res would be equal to depth, since we start depth from 0, when res contains [5], ie one element, we would just want to explore the second level
        (depth 1), and since we do our dfs call from node.right this time around, we always start a new level from the rightmost node in that level

        TC: O(N), SC: O(N)
        
        '''
        res = []

        def dfs(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return res