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


'''
Uses DFS approach, a bit less intuitive than the BFS approach, we keep track of the node we are at, and the level we are at, 
so as we go down the tree we increment depth. depth starts at level 0 meaning the root node
when we come across a new depth we have not been in before, we know that from length of res being same as depth since we start depth from zero, 
we append an empty array to res to prepare it for the nodes that come.

TC: O(N), SC: O(K), or worst case (N)

'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfsTraversal(node, depth):
            if not node:
                return 

            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfsTraversal(node.left, depth + 1)
            dfsTraversal(node.right, depth + 1)
        dfsTraversal(root, 0)
        return res
