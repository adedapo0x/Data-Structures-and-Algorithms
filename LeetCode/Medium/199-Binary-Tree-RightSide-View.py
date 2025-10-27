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