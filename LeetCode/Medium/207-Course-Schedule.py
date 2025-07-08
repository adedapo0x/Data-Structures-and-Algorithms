class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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
    

