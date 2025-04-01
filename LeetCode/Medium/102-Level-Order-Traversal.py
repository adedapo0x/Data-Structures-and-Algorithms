# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        The question is straightforward. basically asking you to implement BFS. So we use a queue and and list of lists.
        The queue is to maintain the order of the nodes, and the list of list is what is returned 
        TC: O(N), SC: O(N), note that for SC we are not considering the list of list being returned
        '''
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        res = []
        while queue:
            inner = []
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                inner.append(node.val)
            res.append(inner)

        return res 