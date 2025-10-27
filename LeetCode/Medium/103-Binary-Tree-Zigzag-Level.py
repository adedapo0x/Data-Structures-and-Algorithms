class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Optimized BFS approach, here we work around having to reverse the odd levels before appending to res, but noticing the pattern of 
        how the indexes align after reversal. so the formular is size - i - 1, gives us what index we would be at reveersed for that element at index i
        so we create a level of that size down already so we can append to whichever index we want accurately
        so no need to reverse here, if it is an odd level, the level would have been reversed as we built into the level

        TC: O(N), SC: O(N)
        '''
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            size = len(queue)
            level = [0] * size
            for i in range(size):
                node = queue.popleft()
                index = size - i - 1 if len(res) % 2 != 0 else i
                level[index] = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res





class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:        
        '''
        Here we use normal BFS approach, when we are about to append an odd level we reverse it before appending to res
        we know if we are about to append an odd level or not based on the amount of levels already in res

        TC: O(N), SC: O(N)
        '''
        if not root:
            return []
        queue = collections.deque([root])
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if len(res) % 2 != 0:
                level.reverse()
            res.append(level)

        return res


        '''
        DFS approach, go through it level order, same approach as DFS in 102, then go through res and reverse the odd levels
        '''
        res = []

        def dfs(node, depth):
            if not node:
                return

            if len(res) == depth:
                res.append([])

            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        for i in range(len(res)):
            if i % 2 != 0:
                res[i].reverse()

        return res
