class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        Notes on bipartite graph:
        A bipartite graph is a graph which can be coloured using 2 colours such that no adjacent nodes (nodes that connect to each other) have the same colour. 
        Any linear graph with no cycle is ALWAYS a bipartite graph. With a cycle, any graph with an EVEN cycle length can also be a bipartite graph.
        So, any graph with an odd cycle length CAN NEVER be a bipartite graph.

        The approach here is to traverse the nodes giving each node opposite colours, and making sure no two nodes that connect to each other have the same colour.
        . If at any moment of traversal, we find the adjacent nodes to have the same colour, it means that there is an odd cycle, or it cannot be a bipartite graph.

        we initialize the colors array that represents what color is in each node with -1. Then we traverse from the beginning of the graph, then put opposite colors, 0 then 1,
        0 then 1 again and again. As we traverse through the graph, should we come across a neighbour that already has the same color as the one we have already, we return False

        TC: O(V + 2E) since it is basically a DFS traversal
        SC: O(V) cos of the colors array
        '''
        color = [-1 for _ in range(len(graph))]
        # could have also done simpler way by: color = [-1] * n where n is len(graph)

        def dfs(pos, col):
            color[pos] = col

            for n in graph[pos]:
                if color[n] == -1:
                    # to convert from 0 to 1, 1 to 0. we can just do 1 - col instead of int(not col)
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
        