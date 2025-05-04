'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph 
and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path
between the source and destination nodes.
'''

def has_path(graph, src, dst):
    # BFS Approach
    import collections
    queue = collections.deque([src])
    visited = set()

    while queue:
        node = queue.popleft()
        visited.add(node)

        if dst in visited: # we could have also just compared the node with the dst we are looking for, rather than checking our visited, 
            return True       # but this still works too

        for n in graph[node]:
            if n not in visited:
                queue.append(n)
    return False

# DFS Approach
def has_path(graph, src, dst):
    # using a helper function since I need my visited set as an argument, if not, the has_path can be the recursive function itself
    visited = set()
    return dfs(graph, src, dst, visited)


def dfs(graph,src, dst, visited):
  if src == dst:
    return True
  visited.add(src)
  for n in graph[src]:
    if n not in visited:
      if dfs(graph, n, dst, visited):
        return True
  return False
  