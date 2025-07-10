class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        Still similar logic as the solutions below, but here I use a single array indexes to keep track of if our node has been previously visited and if it 
        is still in the traversal path. 
        We use 1 to signify if we are still in that path and 2 if we have returned from that path and do not need to consider traversing there again so we can simply return False
        if we encounter a neighbour with an index of 1 that means it is visited, and we have come across something that is still along the path we are currently at
        so this is a cycle.

        TC: O(V+E) since it is still kind of basically a DFS traversal
        '''
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
        This is basically a question that requires us to check if the directed graph that is formed from the courses relationship is cyclic.
        So, here I use dfs with two separate arrays, one for visited and one for the path we are currently visiting.
        If cycle exists, we cannot finish and we return False, else we return True
        '''
        visited = [0] * numCourses
        path = [0] * numCourses

        adjList = { c: [] for c in range(numCourses)}
        
        for course, prereq in prerequisites:
            adjList[prereq].append(course)

        def dfsCheck(node):
            visited[node] = 1
            path[node] = 1

            for n in adjList[node]:
                if visited[n] == 0:
                    if dfsCheck(n):
                        return True
                elif path[n] == 1:
                    return True
            
            path[node] = 0
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if dfsCheck(i):
                    return False

        return True
    

        '''
        Here, we use BFS approach, the Khan Algorithm, to determine if there is a cycle in the graph
        How we know this is, if at the end of it all, the number of nodes in the list we are using to keep track of the topo sort is not equal to 
        the total number of nodes in the graph

        that points to the fact that there are still nodes without indegree of 0, due to them still needing something that needs them also (ie a cycle exists)
        '''

        
        adjList = { c: [] for c in range(numCourses)}
        indegree = [0] * numCourses
        ans = []

        for course, prereq in prerequisites:
            adjList[prereq].append(course)
            indegree[course] += 1

        queue = collections.deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            ans.append(node)

            for n in adjList[node]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        return True if len(ans) == numCourses else False
    

