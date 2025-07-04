from collections import deque, defaultdict
class Solution:
    '''
    Khan Algo is how we get the topological sort on a DAG (Directed Acyclic Graph) using BFS. 
    First, we will calculate the indegree of each node (ie number of nodes that is directed into each node) and store it in the indegree array.
    Note that for every graph, there is always at least one node with indegree of zero, ie no nodes enters into it

    We can iterate through the given list, and simply for every node u->v, we can increase the indegree of v by 1 in the indegree array. 
    Initially, there will be always at least a single node whose indegree is 0. So, we will push the node(s) with indegree 0 into the queue.
    Then, we will pop a node from the queue, appending it to the ans array that is to be returned, and for all its adjacent nodes, we will decrease the indegree of that node by one. 
    For example, if node u that has been popped out from the queue has an edge towards node v(u->v), we will decrease indegree[v] by 1 ie one less thing that points to it that we have to consider
    After that, if for any node the indegree becomes 0, we will push that node again into the queue.
    We will repeat until the queue is completely empty. Finally, completing the BFS we will get the linear ordering of the nodes in the answer array.

    TC: O(V + E), TC for a usual BFS algo
    SC: O(N) for the queue and indegree array
    '''
    def topoSort(self, V, edges):
        queue = deque()
        
        adj = defaultdict(list)
        
        for node, neigh in edges:
            adj[node].append(neigh)
        
        indegree = [0] * V
        
        for node, neigh in edges:
            indegree[neigh] += 1
            
        for i in range(V):
            if indegree[i] == 0:
                queue.append(i)
                
        ans = []   
        while queue:
            node = queue.popleft()
            ans.append(node)
            
            for n in adj[node]:
                indegree[n] -= 1
                
                if indegree[n] == 0:
                    queue.append(n)
                    
        return ans