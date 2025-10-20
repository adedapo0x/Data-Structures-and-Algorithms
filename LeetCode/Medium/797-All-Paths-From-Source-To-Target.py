class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
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

            
