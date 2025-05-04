'''
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph 
and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path
 between the source and destination nodes.
'''

def has_path(graph, src, dst):
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
  