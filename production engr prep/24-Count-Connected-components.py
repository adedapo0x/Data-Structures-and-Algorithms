from collections import defaultdict
def count_connected_components(edges):
    adjacency_list = defaultdict(list)
    
    for u, v in edges:
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)
        
    visited = set()
    def dfs(node):
        visited.add(node)
        
        for neighbour in adjacency_list[node]:
            if neighbour not in visited:
                    dfs(neighbour)
            
    components = 0
    for node in adjacency_list:
        if node not in visited:
            components += 1
            dfs(node)
            
    return components