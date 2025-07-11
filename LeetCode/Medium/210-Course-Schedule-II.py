class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        Here we use the Khan Algorithm to detect if a cycle exists if it doesn't we return the topo sort array generated.

        So if the length of the topo array is not equal to the number of total courses at the end of the code, then there is a cycle and we return 
        an empty array, else we return the topo sort.

        '''
        
        adjList = {c: [] for c in range(numCourses)}
        queue = collections.deque()
        indegree = [0] * numCourses
        topo = []

        for node, neighbour in prerequisites:
            adjList[neighbour].append(node)
            indegree[node] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            topo.append(node)

            for n in adjList[node]:
                indegree[n] -= 1

                if indegree[n] == 0:
                    queue.append(n)

        return topo if len(topo) == numCourses else []


        '''
        naive way of solving this, I first check if there is a cycle, if there is I return an empty list, if there is no cycle, then I 
        do a topological sort which is what the question is about actually.

        TC: O(V + E)
        '''
        adjList = defaultdict(list)
        visited = set()
        stack = []

        visitedArr = [0] * numCourses
        path = [0] * numCourses

        for x, y in prerequisites:
            adjList[y].append(x)

        def dfsCheck(node):
            visitedArr[node] = 1
            path[node] = 1

            for n in adjList[node]:
                if visitedArr[n] == 0:
                    if dfsCheck(n):
                        return True
                elif path[n] == 1:
                    return True

            path[node] = 0
            return False

        def checkCycle():
            for i in range(numCourses):
                if visitedArr[i] == 0:
                    if dfsCheck(i):
                        return True
            return False

        if checkCycle():
            return []

        def dfs(node):
            visited.add(node)

            for n in adjList[node]:
                if n not in visited:
                    dfs(n)

            stack.append(node)

        for i in range(numCourses):
            if i not in visited:
                dfs(i)
        
        ans = []
        while stack:
            ans.append(stack.pop())
        return ans