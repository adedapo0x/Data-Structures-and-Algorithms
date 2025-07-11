class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        adjList = defaultdict(list)

        for node, neighbour in prerequisites:
            adjList[neighbour].append(node)

        def dfsCheck(node):
            if visited[node] == 1:
                return True
            if visited[node] == 2:
                return False

            visited[node] = 1

            for n in adjList[node]:
                if dfsCheck(n):
                    return True

            visited[node] = 2
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfsCheck(i):
                    return False
        return True





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