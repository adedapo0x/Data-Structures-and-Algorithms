class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        '''
        DFS approach we take each node then go through its neighbouurs, then when we get to n-1, we append to res, then return

        TC: O(2^N * N) , we get 2^N because each node could have multiple children, and at each juncture, we have to explore each of the multiple paths
        then for the * N this is because each path has a size of about N nodes, and when we get to target N-1 we do a copy of the elements to res, which is an O(N) operation
        SC: think this is similar to TC

        note that TC for best case, where we could have like a linear graph, is O(V + E) where we just do a normal DFS one or few choices per node
        or we could say the TC is O(P * L) for average case, where P is the multiple paths available per node, and L is the length of that path
        '''

        def backtrack(node, arr):
            arr.append(node)

            if node == len(graph) - 1:
                res.append(arr[:])
                return 

            for neighbour in graph[node]:
                backtrack(neighbour, arr)
                arr.pop()
        
        res = []
        backtrack(0, [])
        return res

        # BFS approach, we store the entire path generated each time not just the node
        queue = deque([[0]])
        res = []

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == len(graph) - 1:
                res.append(path)
            else:
                for neighbour in graph[node]:
                    queue.append(path + [neighbour])

        return res

            
