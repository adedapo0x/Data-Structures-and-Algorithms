class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        # could have also 

        def dfs(pos, col):
            color[pos] = col

            for n in graph[pos]:
                if color[n] == -1:
                    if dfs(n, int(not col)) == False:
                        return False
                elif color[n] == col:
                    return False

            return True

        for c in range(len(graph)):
            if color[c] == -1:
                if dfs(c, 0) == False:
                    return False
        
        return True
        