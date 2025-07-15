class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        This question is all about cycles, we want to know if each nodes leads to a cycle, so if a node leads to a cycle, it is an unsafe node. One way to have solved this
        would be to check for each node. 
        One of the ways we could have done this is to traverse from every node and check if that node leads to a cycle, and only add those that don't lead to a cycle 
        to the list we want to return. This would be very inefficient and slow

        So here, we use a better approach, using DFS here to check, but here we already compute for if the node is a safe state once we come across it once and store it, instead 
        of having to recheck every time. 
        The approach is to use a dictionary to store if the node is safe or not. So our dfs checks, and once we have seen it before, we simply return the value that we stored in our hashmap.
        once we come across a node, we initially set it as False (that is it is not a safe state), then we go through it neighbours recursively, ie exploring all paths that that node can lead to.

        We put a check cos as we return up the recursion tree, once we get False we know that the entire path upward is False, else the path is True 

        '''
        safe = {}

        def dfs(i):
            if i in safe:
                return safe[i]
            safe[i] = False
            for n in graph[i]:
                if not dfs(n):
                    return False
            safe[i] = True
            return True

        res = []
        for i in range(len(graph)):
            if dfs(i):
                res.append(i)

        return res

        '''
        A better way of doing this: Here we reverse the graph directed link, if from A -> B, then we reverse it to B -> A, then we run the Khan Algorithm, then we sort the topo list,
        the sorting is cos the question requires it.

        the intuition behind this is 
        '''
        reverseAdj = defaultdict(list)
        indegree = [0] * len(graph)

        for i in range(len(graph)):
            for node in graph[i]:
                reverseAdj[node].append(i)
                indegree[i] += 1

        queue = collections.deque()
        for i in range(len(graph)):
            if indegree[i] == 0:
                queue.append(i)

        topo = []
        while queue:
            node = queue.popleft()
            topo.append(node)

            for n in reverseAdj[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        topo.sort()
        return topo
